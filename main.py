
# TODO get a funtioning economy
# TODO growing seeds
# TODO harvesting
# TODO buy new farms

from mapfarm import FarmMap
from inv import Inv
thisFarm = FarmMap()
thisInv = Inv()

def buyseed():
    if thisFarm.x == 0 and thisFarm.y == 1:
        thisInv.coin -= 1
        thisInv.seed += 1
        print(f" you did it, you get a gold star. also you have {thisInv.coin} coin(s) and {thisInv.seed} seed(s).")

def cmds():
    actionlist = {"up": thisFarm.up,
                  "w": thisFarm.up,
                  "down": thisFarm.down,
                  "s": thisFarm.down,
                  "left": thisFarm.left,
                  "a": thisFarm.left,
                  "right": thisFarm.right,
                  "d": thisFarm.right,
                  "buy": buyseed
                  }
    action: str = input("What do you do? ")
    action = action.lower()
    if action not in actionlist.keys():
        print("I did not get that, try again. ")
    else:
        actionlist.get(action)()


while True:
    thisFarm.render()
    cmds()
