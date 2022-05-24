from datetime import datetime, timedelta
from json import loads
import socket

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

    def __init__(self, ip: str, port: int, update_timeout: int = 30):
        self._tcp_ip = ip
        self._tcp_port = port
        self._update_timeout = update_timeout

        self.last_check = datetime.now() - timedelta(seconds=update_timeout+1)
        self.refresh()

    def _read_lobby(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self._tcp_ip, self._tcp_port))
        s.sendall(b"GET / HTTP/0.9\r\nLobby: True\r\n\r\n")
        data = s.recv(2048)
        s.close()
        json = loads(data.decode())
        self.servers = []
        for server_json in json:
            self.servers.append(Counterpact_Server(server_json))
    
    def _misc_data(self):
        self.total_players = sum([server.players for server in self.servers])
