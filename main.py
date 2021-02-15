# TODO get a funtioning economy
# TODO growing seeds
# TODO harvesting
# TODO buy new farms
# plant types vV, wW, oO
#
from mapfarm import FarmMap
from inv import Inv

thisFarm = FarmMap()
thisInv = Inv()


def plantseed():
    thisFarm.plantable = thisFarm.farm[thisFarm.y][thisFarm.x] == "."
    if thisInv.seed > 0 and thisFarm.plantable:
        thisInv.seed -= 1
        thisFarm.plantstuff()


def mony():
    thisInv.coin += 9999
    print("Cheater.")

def sed():
    thisInv.seed += 999
    print("Cheater.")

def buyseed():
    if thisFarm.x == 0 and thisFarm.y == 1:
        thisInv.coin -= 1
        thisInv.seed += 1



def cmds():
    actionlist = {"up": thisFarm.up,
                  "w": thisFarm.up,
                  "down": thisFarm.down,
                  "s": thisFarm.down,
                  "left": thisFarm.left,
                  "a": thisFarm.left,
                  "right": thisFarm.right,
                  "d": thisFarm.right,
                  "buy": buyseed,
                  "plant": plantseed,
                  "tax evasion": mony,
                  "seedbank": sed}
    action: str = input("What do you do? ")
    action = action.lower()
    if action not in actionlist.keys():
        print("I did not get that, try again. ")
    else:
        actionlist.get(action)()


while True:
    thisFarm.render()
    print(f"You have {thisInv.coin} coin(s) and {thisInv.seed} seed(s).")
    cmds()
