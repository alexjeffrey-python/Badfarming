# plant types vV, wW, oO
from mapfarm import FarmMap
from inv import Inv

thisFarm = FarmMap()
thisInv = Inv()


def newfarm():
    if thisInv.coins >= 25 and thisFarm.farmnumber == 0:
        thisInv.coins -= 25
        thisFarm.farmnumber += 1
        thisFarm.farmupdate()
        print("You got a new and better farm! The next one costs 75 coins.")
    elif thisInv.coins >= 75 and thisFarm.farmnumber == 1:
        thisInv.coins -= 75
        thisFarm.farmnumber += 1
        thisFarm.farmupdate()
        print("You got a new and better farm!")


def plantseed():
    thisFarm.plantable = thisFarm.farm[thisFarm.y][thisFarm.x] == thisFarm.soil
    if thisFarm.plantable:
        plnttype = input("Which seed do you want to plant? ")
        plnttype = plnttype.lower()
        if thisInv.Vseed > 0 and plnttype == "v":
            thisInv.Vseed -= 1
            thisFarm.planttype = plnttype
            thisFarm.plantstuff()
            print("Planted!")
        else:
            print("You don't have that seed.")
    else:
        print("This does not look like a good place for seeds, or did you not have any? (plant in *)")


def mony():
    thisInv.coins += 9999
    print("Cheater.")


def sed():
    thisInv.Vseed += 999
    print("Cheater.")


def maxfarm():
    thisFarm.farmnumber = 1
    thisFarm.farmupdate()
    print("Cheater.")


def buy():
    if thisFarm.farm[thisFarm.y][thisFarm.x] == thisFarm.bazaar:
        plnttype = input("Which type of plant do you want to buy? ")
        plnttype = plnttype.lower()
        if plnttype == "v":
            amount = int(input("How many seeds do you want to buy? "))
            if thisInv.coins >= amount >= 0:
                thisInv.Vseed += amount
                thisInv.coins -= amount
                print("Cha-ching!")
            else:
                print("You can't go into debt! (or sell seeds that you dont have.)")
    else:
        print("Go to the bazaar (BZR) to buy seeds.")


def reap():
    if thisFarm.harvest():
        thisInv.Vstalks += 1
        print("*Slice!*")
    else:
        print("It doesnt look ready to harvest, or did you plant it? (wait until it is fully grown.)")


def profits():
    if thisFarm.farm[thisFarm.y][thisFarm.x] == thisFarm.bazaar:
        amount = int(input("How many crops do you want to sell? "))
        if amount <= thisInv.Vstalks:
            thisInv.Vstalks -= amount
            thisInv.coins += 2 * amount
            print("Cha-ching!")
        else:
            print("You can't sell what you don't have!")
    else:
        print("Go to the bazaar (BZR) to sell crops.")


def nothing():
    pass


def cropinfo():
    print("""(.vV), V is the first crop people recommend for newbie farmers such as yourself.\
[Grows in 6 turns, costs 1, crop is worth 2.]""")


def inputs():
    print("""You are [].
You have three important things, coins, seeds, and crops.
Coins are money, they allow you to buy things such as farms and seeds.
Seeds are what you put in the ground, they can grow into things such as crops.
Crops are what you sell for coins, they are harvested from fully grown seeds, if you bring crops into the bazaar,\
you will get a price.
COMMANDS:
'p' or 'help', brings up this menu.
'o' or 'crop book', tells you what each seed/crop is and what it does.
'w' or 'up', moves you up.
'a' or 'left', moves you left.
's' or 'down', moves you down.
'd' or 'right', moves you right.
'f' or 'harvest', harvests the crop you are on.
'e' or 'plant', plants a seed of type X on the tile you are on. (X is any crop type)
'c' or 'sell', sells crop(s) of type X. (X is any crop type)
'v' or 'buy', buys seed(s) of type X. (X is any crop type)
'g' or 'upgrade', upgrades your farm. (hint, the next farm costs 25 coins)
'' or 'wait', does nothing, it just passes the time.""")


def cmds():
    actionlist = {"up": thisFarm.up,
                  "w": thisFarm.up,
                  "down": thisFarm.down,
                  "s": thisFarm.down,
                  "left": thisFarm.left,
                  "a": thisFarm.left,
                  "right": thisFarm.right,
                  "d": thisFarm.right,
                  "harvest": reap,
                  "f": reap,
                  "buy": buy,
                  "v": buy,
                  "sell": profits,
                  "c": profits,
                  "plant": plantseed,
                  "e": plantseed,
                  "upgrade": newfarm,
                  "g": newfarm,
                  "": nothing,
                  "wait": nothing,
                  "help": inputs,
                  "crop book": cropinfo,
                  "o": cropinfo,
                  "tax evasion": mony,
                  "seedy place": sed,
                  "tricked out": maxfarm}
    action: str = input("What do you do? ")
    action = action.lower()
    if action not in actionlist.keys():
        print("I did not get that, try again. ")
    else:
        actionlist.get(action)()


inputs()
thisFarm.farmupdate()
while True:
    print("\n")
    thisFarm.render()
    print(f"You have {thisInv.coins} coin(s), {thisInv.Vseed} seed(s), and {thisInv.Vstalks} V stalk(s).")
    cmds()
    thisFarm.growself()
