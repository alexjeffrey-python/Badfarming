class FarmMap:

    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.farmnumber: int = 0
        self.soil: str = "*"
        self.farm: list = [[self.soil]]
        self.barn: str = ""
        self.bazaar: str = ""
        self.fence: str = ""
        self.gate: str = ""
        self.maxheight: int = len(self.farm) - 1
        self.maxwidth: int = len(self.farm[0]) - 1
        self.plantable: bool = self.farm[self.y][self.x] == "."
        self.globetime: int = 0
        self.planttime: list = []
        self.growtime: int = 8
        self.planttype: str = ""

    def up(self):
        self.y -= 1
        if self.y < 0:
            self.y = self.maxheight

    def down(self):
        self.y += 1
        if self.y > self.maxheight:
            self.y = 0

    def right(self):
        self.x += 1
        if self.x > self.maxwidth:
            self.x = 0

    def left(self):
        self.x -= 1
        if self.x < 0:
            self.x = self.maxwidth

    def render(self):
        print("╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼")
        for row in range(0, len(self.farm)):
            for column in range(0, len(self.farm[row])):
                if self.x == column and self.y == row:
                    print("[" + self.farm[row][column] + "]", end=" ")
                else:
                    print(" " + self.farm[row][column] + " ", end=" ")
            print()
        print(f"Your coords are ({self.x}, {self.maxheight - self.y}).")
        print("╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼")
        print("")

    def harvest(self):
        if self.farm[self.y][self.x] == ("V" or "W" or "O"):
            return True
        else:
            return False

    def farmupdate(self):
        if self.farmnumber == 0:
            self.x = 0
            self.y = 0
            self.barn = "BRN"
            self.bazaar = "BZR"
            self.fence = " │ "
            self.gate = " ╳ "
            self.soil = "*"
            self.farm = [[self.barn, self.soil, self.soil, self.soil, self.soil],
                         [self.bazaar, self.soil, self.soil, self.soil, self.soil],
                         [self.fence, self.soil, self.soil, self.soil, self.soil],
                         [self.gate, self.soil, self.soil, self.soil, self.soil],
                         [self.fence, self.soil, self.soil, self.soil, self.soil]]

            self.maxheight = len(self.farm) - 1
            self.maxwidth = len(self.farm[0]) - 1
        elif self.farmnumber == 1:
            self.x = 0
            self.y = 1
            self.barn = "BRN"
            self.bazaar = "BZR"
            self.fence = "|╳|"
            self.gate = "I-I"
            self.soil = "+"
            self.farm = [[self.gate, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil],
                         [self.barn, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil],
                         [self.bazaar, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil],
                         [self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil]]

        elif self.farmnumber == 2:
            self.x = 0
            self.y = 4
            self.barn = "BIGBRN"
            self.bazaar = "BAZAAR"
            self.fence = "|+)(+|"
            self.gate = "|-()-|"
            self.soil = "÷"
            self.farm = [[self.fence, self.soil, self.soil, self.soil, self.soil, self.soil, self.fence],
                         [self.gate, self.soil, self.soil, self.soil, self.soil, self.soil, self.fence],
                         [self.fence, self.soil, self.soil, self.soil, self.soil, self.soil, self.fence],
                         [self.bazaar, self.soil, self.soil, self.soil, self.soil, self.soil, self.bazaar],
                         [self.barn, self.soil, self.soil, self.soil, self.soil, self.soil, self.fence],
                         [self.fence, self.soil, self.soil, self.soil, self.soil, self.soil, self.gate],
                         [self.fence, self.soil, self.soil, self.soil, self.soil, self.soil, self.fence]]

        self.maxheight = len(self.farm) - 1
        self.maxwidth = len(self.farm[0]) - 1

    def plantstuff(self):
        self.farm[self.y][self.x] = "."
        self.planttime.append([self.globetime, self.x, self.y, self.planttype])

    def growself(self):
        self.globetime += 1
        for plant, x, y, breed in self.planttime:
            if plant == self.globetime - self.growtime / 2:
                self.farm[y][x] = breed.lower
            elif plant == self.globetime - self.growtime:
                self.farm[y][x] = breed.upper
