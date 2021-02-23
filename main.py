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
        print("You got a new and better farm! The next one costs 200 coins.")
    elif thisInv.coins >= 200 and thisFarm.farmnumber == 2:
        thisInv.coins -= 75
        thisFarm.farmnumber += 1
        thisFarm.farmupdate()
        print("You got a new and better farm! The next one costs 450 coins, once it is built. (W.I.P)")


def mony():
    thisInv.coins += 9999
    print("Cheater.")


def plant():
    thisInv.Vstalks += 999
    thisInv.Wstems += 999
    print("Cheater.")


def sed():
    thisInv.Vseed += 99
    thisInv.Wseed += 99
    print("Cheater.")


def maxfarm():
    thisFarm.farmnumber = 2
    thisFarm.farmupdate()
    print("Cheater.")


def buy():
    if thisFarm.farm[thisFarm.y][thisFarm.x] == thisFarm.bazaar:
        plnttype = input("Which type of plant do you want to buy? ")
        plnttype = plnttype.lower()
        plntmulti = thisInv.plntcost.get(plnttype)
        amount = int(input("How many seeds do you want to buy? "))
        if thisInv.coins >= plntmulti * amount >= 0:
            if plnttype == "v":
                thisInv.Vseed += amount
                thisInv.coins -= plntmulti * amount
                print("Cha-ching!")

            elif plnttype == "w":
                thisInv.Wseed += amount
                thisInv.coins -= plntmulti * amount
                print("Cha-ching!")

            elif plnttype == "o":
                thisInv.Oseed += amount
                thisInv.coins -= plntmulti * amount
                print("Cha-ching!")

            else:
                print("You can not find anyone who sells that.")
        else:
            print("You can't go into debt! (or sell seeds that you dont have.)")
    else:
        print("Go to the bazaar (BZR) to buy seeds.")


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
        elif thisInv.Wseed > 0 and plnttype == "w":
            thisInv.Wseed -= 1
            thisFarm.planttype = plnttype
            thisFarm.plantstuff()
            print("Planted!")
        elif thisInv.Oseed > 0 and plnttype == "o":
            thisInv.Oseed -= 1
            thisFarm.planttype = plnttype
            thisFarm.plantstuff()
            print("Planted!")
        else:
            print("You don't have that seed.")
    else:
        print("This does not look like a good place for seeds. (plant in soil)")


def reap():
    if thisFarm.harvest():
        if thisFarm.farm[thisFarm.y][thisFarm.x] == "V":
            thisInv.Vstalks += 1
        elif thisFarm.farm[thisFarm.y][thisFarm.x] == "W":
            thisInv.Wstems += 1
        elif thisFarm.farm[thisFarm.y][thisFarm.x] == "O":
            thisInv.Onectar += 1
        print("*Slice!*")
        thisFarm.farm[thisFarm.y][thisFarm.x] = thisFarm.soil
    else:
        print("It doesnt look ready to harvest, or did you plant it? (wait until it is fully grown.)")


def profits():
    if thisFarm.farm[thisFarm.y][thisFarm.x] == thisFarm.bazaar:
        plnttype = input("Which type of crop do you want to sell? (use the plant it came from, AKA 'v' for V stalks.)")
        plnttype = plnttype.lower()
        plntmulti = thisInv.plntprofit.get(plnttype)
        amount = int(input("How many crops do you want to sell? "))
        if amount <= thisInv.Vstalks and plnttype == "v":
            thisInv.Vstalks -= amount
            thisInv.coins += plntmulti * amount
            print("Cha-ching!")
        elif amount <= thisInv.Wstems and plnttype == "w":
            thisInv.Wstems -= amount
            thisInv.coins += plntmulti * amount
            print("Cha-ching!")
        elif amount <= thisInv.Wstems and plnttype == "o":
            thisInv.Onectar -= amount
            thisInv.coins += plntmulti * amount
            print("Cha-ching!")

        else:
            print("You can't sell what you don't have!")
    else:
        print("Go to the bazaar (BZR) to sell crops.")


def nothing():
    pass


def cropinfo():
    print("""╔═THE═CROP═BOOK!═══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║(.vV), V is the first crop people recommend for newbie farmers such as yourself.                                    ║
║[Grows in 6 turns, costs 1, crop is worth 2 coins.]                                                                 ║
║(.wW), W is often confused with a bush of V, but is actually a slower growing species of it, thus it has more value.║
║[Grows in 10 turns, costs 3, crop is worth 5 coins.]                                                                ║
║(.oO), O is a pitcher like plant which makes nectar inside, the nectar is very sweet. It is very valueable to chefs.║
║[Grows in 19 turns, costs 8, crop is worth 13 coins.]                                                               ║
╚═THE═CROP═BOOK!═════════════════════════════════════════════════════════════════════════════════════════════════════╝""")


def inputs():
    print("""═════════════════════════════════════════════════════════════════════════════
You are [].
You have three important things, coins, seeds, and crops.
Coins are money, they allow you to buy things such as farms and seeds.
Seeds are what you put in the ground, they can grow into things such as crops.
Crops are what you sell for coins, they are harvested from fully grown seeds.
If you bring crops into the bazaar, you will get a price.
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
'' or 'wait', does nothing, it just passes the time.
═════════════════════════════════════════════════════════════════════════════""")


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
                  "p": inputs,
                  "crop book": cropinfo,
                  "o": cropinfo,
                  "tax evasion": mony,
                  "seedy place": sed,
                  "harvest day": plant,
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
    print("")
    thisFarm.render()
    print(f"""═══════Finance═══════════V═Plant══════W=Plant═════O Plant
You have {thisInv.coins} coin(s).    │ {thisInv.Vseed} seed(s). │ {thisInv.Wseed} seed(s).│ {thisInv.Wseed} seed(s).           │ 
Your farm is tier {thisFarm.farmnumber + 1}.   │ {thisInv.Vstalks} stalk(s).│ {thisInv.Wstems} stem(s).│  {thisInv.Onectar} pint(s) of nectar.│ 
══════════════════════════════════════════════════""")
    cmds()
    thisFarm.growself()
