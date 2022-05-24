# Counterpact Watcher

A Python library to get the Counterpact lobby and watch for changes.

# Usage

```py
from time import sleep

from cpact-watcher import Counterpact_Lobby

lobby = Counterpact_Lobby()
print(lobby.servers) # Returns a list of servers
sleep(30)
lobby.reload()
print(lobby.servers) # Returns a newly populated list of servers
```

###### Not to be confused with the Watcher from counterpact...