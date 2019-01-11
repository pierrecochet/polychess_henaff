# =============================================================================
# IMPORTS 
# =============================================================================

import requests
import polychess

class Lichess:
    
    def __init__(self):
        self.token = "zBQqzUqktFFfTZbl"
        self.header = {
            "Authorization": "Bearer {}".format(self.token)
        }
        self.gameId = "RpVnmjWT"
    
    def lichessAPI():
    #   Call the API to start a new game
    #    r = requests.get("https://lichess.org/api/account", headers=header)
    #    print(r.text)
    #    r2 = requests.get("https://lichess.org/api/stream/event", headers=header)
    #    print(r2.text)
        r = requests.post("https://lichess.org/api/bot/game/RpVnmjWT/move/h7h5", headers=self.header)
        print(r.text)
        
        
    def move(self, moveUCI):
        r = requests.post("https://lichess.org/api/bot/game/" + self.gameId + "/move/" + moveUCI, headers=self.header)
        print("retour play move : " + str(r.text))
        
    def getStatusGame(self):
        r = requests.get("https://lichess.org/api/bot/game/stream/" + self.gameId, headers=self.header, stream=True)
        print("Status : ")
        print(r.text)
        

lich = Lichess()
mov = "d8c7"
lich.getStatusGame()



# =============================================================================
#                   token : zBQqzUqktFFfTZbl 
# =============================================================================
