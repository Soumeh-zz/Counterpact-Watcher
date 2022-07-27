from datetime import datetime, timedelta
from requests import get

class Counterpact_Server():
    """Counterpact server object.

    Arguments:
        json (dict) - A Dictionary object from the lobby JSON data.

    Attributes:
        name: Server's display name.
        players: Number of players online.
        max_players: Maximum number of players.
        mods: ???
        ip: IP address of the server.
        wsip: ???
        port: Port of the server.
        wsport: ???
        map: Map file that the server is playing.
        version: What version of the game the server is running.
        passkey: ???
        full_up: The full, connectable IP address of the server.
        map_name: The display name of the server's map.
    """

    def __init__(self, json: dict):
        self.name = json['serverName']
        self.players = json['serverPlayers']
        self.max_players = json['serverMax']
        self.mods = json['serverMods']
        self.ip = json['serverIp']
        self.wsip = json['serverWSIp']
        self.port = json['serverPort']
        self.wsport = json['serverWSPort']
        self.map = json['serverMap']
        self.version = json['serverVersion']
        self.passkey = json['serverPasskey']

        self.full_ip = self.ip + ':' + str(self.port)
        self.map_name = self.map.rsplit('.', 1)[0]

class Counterpact_Lobby():
    """Counterpact lobby object.

    Arguments:
        ip (str) - The IP address of the lobby server.
        port (int) - The port of the lobby server.
        update_timeout (int) - The time (in seconds) between when the lobby can be refreshed.

    Attributes:
        total_players: 
    """

    def refresh(self) -> bool:
        """Refresh the lobby object's data (on a timeout.)

        Returns:
            Whether or not the lobby was refreshed.
        """
        now = datetime.now()
        difference = (now - self.last_check).total_seconds()
        if difference < self._update_timeout:
            return False
        self._read_lobby()
        self._misc_data()
        self.last_check = datetime.now()
        return True

    def __init__(self, url: str, update_timeout: int = 30):
        self.url = url
        self._update_timeout = update_timeout

        self.last_check = datetime.now() - timedelta(seconds=update_timeout+1)
        self.refresh()

    def _read_lobby(self):
        resp = get(self.url, headers={"Lobby":"True"})
        self.servers = []
        for server_json in resp.json():
            self.servers.append(Counterpact_Server(server_json))
    
    def _misc_data(self):
        self.total_players = sum([server.players for server in self.servers])
