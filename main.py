# TODO get a funtioning economy 1/2
# TODO growing seeds 1/2
# TODO harvesting
# TODO buy new farms
# plant types vV, wW, oO
#
from mapfarm import FarmMap
from inv import Inv

thisFarm = FarmMap()
thisInv = Inv()


def newfarm():
    if thisInv.coins >= 25 and thisFarm.farmnumber == 0:
        thisInv.coins = 0
        thisFarm.farmnumber = 1
        thisFarm.farmupdate()
    elif thisInv.coins >= 75 and thisFarm.farmnumber == 1:
        thisInv.coins = 0
        pass


def plantseed():
    thisFarm.plantable = thisFarm.farm[thisFarm.y][thisFarm.x] == thisFarm.soil
    if thisInv.seed > 0 and thisFarm.plantable:
        thisInv.seed -= 1
        thisFarm.plantstuff()


def mony():
    thisInv.coins += 9999
    print("Cheater.")


def sed():
    thisInv.seed += 999
    print("Cheater.")


def buyseed():
    if thisFarm.x == 0 and thisFarm.y == 1:
        thisInv.coins -= 1
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
                  "upgrade": newfarm,
                  "tax evasion": mony,
                  "seedbank": sed}
    action: str = input("What do you do? ")
    action = action.lower()
    if action not in actionlist.keys():
        print("I did not get that, try again. ")
    else:
        actionlist.get(action)()


thisFarm.farmupdate()
while True:
    thisFarm.render()
    print(f"You have {thisInv.coins} coin(s) and {thisInv.seed} seed(s).")
    cmds()
    thisFarm.growself()
