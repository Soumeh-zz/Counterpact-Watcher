# Counterpact Watcher

A Python library to get the Counterpact lobby and watch for changes.

# Installation

`pip install https://github.com/Soumeh/Counterpact-Watcher.git`

# Usage

```py
from time import sleep

from cpact_watcher import Counterpact_Lobby

lobby = Counterpact_Lobby(
    url = 'http://127.0.0.1:8000', # The URL address of the lobby server (Contact The Developer to get it)
    timeout = 30 # The time (in seconds) between when the lobby can be refreshed
)
print(lobby.servers) # Returns a list of servers
sleep(30)
lobby.reload()
print(lobby.servers) # Returns a newly populated list of servers
```

## `Counterpact_Lobby`
|attributes|description|
|-|-|
|`total_players`|The number of online players|

|function|description
|-|-|
|`refresh()`|Refresh the lobby object's data (on a timeout)|


## `Counterpact_Server`
|attribute|description|
|-|-|
|`name`|Server's display name.
|`players`|Number of players online.|
|`max_players`|Maximum number of players.|
|`mods`|???|
|`ip`|IP address of the server.|
|`wsip`|???|
|`port`|Port of the server.|
|`wsport`|???|
|`map`|Map file that the server is playing.|
|`version`|What version of the game the server is running.|
|`passkey`|???|
|`full_up`|The full, connectable IP address of the server.|
|`map_name`|The display name of the server's map.|

###### Not to be confused with the Watcher from Counterpact...
