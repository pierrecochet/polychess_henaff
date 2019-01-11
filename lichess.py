# =============================================================================
# IMPORTS 
# =============================================================================

import requests
import polychess


def lichessAPI():
#   Call the API to start a new game
    r = requests.get("https://lichess.org/api/account -H \"Authorization: Bearer zBQqzUqktFFfTZbl\"")
#    r2 = requests.get("https://lichess.org/api/stream/event")
    print(r.text)
    
    
lichessAPI()