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
        self.maxHeight: int = len(self.farm) - 1
        self.maxWidth: int = len(self.farm[0]) - 1
        self.plantable: bool = self.farm[self.y][self.x] == "."
        self.globetime: int = 0
        self.planttime: list = []
        self.growtime: int = 8

    def up(self):
        self.y -= 1
        if self.y < 0:
            self.y = self.maxHeight

    def down(self):
        self.y += 1
        if self.y > self.maxHeight:
            self.y = 0

    def right(self):
        self.x += 1
        if self.x > self.maxWidth:
            self.x = 0

    def left(self):
        self.x -= 1
        if self.x < 0:
            self.x = self.maxWidth

    def render(self):
        for row in range(0, len(self.farm)):
            for column in range(0, len(self.farm[row])):
                if self.x == column and self.y == row:
                    print("[" + self.farm[row][column] + "]", end=" ")
                else:
                    print(" " + self.farm[row][column] + " ", end=" ")
            print()
        print(self.x, self.y)

    def farmupdate(self):
        if self.farmnumber == 0:
            self.x = 0
            self.y = 0
            self.barn = "BRN"
            self.bazaar = "BZR"
            self.fence = "|  "
            self.soil = "*"
            self.farm = [[self.barn, self.soil, self.soil, self.soil, self.soil],
                         [self.bazaar, self.soil, self.soil, self.soil, self.soil],
                         [self.fence, self.soil, self.soil, self.soil, self.soil],
                         [self.fence, self.soil, self.soil, self.soil, self.soil],
                         [self.fence, self.soil, self.soil, self.soil, self.soil]]

            self.maxHeight = len(self.farm) - 1
            self.maxWidth = len(self.farm[0]) - 1
        elif self.farmnumber == 1:
            self.x = 0
            self.y = 1
            self.barn = "BRN"
            self.bazaar = "BZR"
            self.fence = "|| "
            self.soil = "+"
            self.farm = [[self.fence, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil],
                         [self.barn, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil],
                         [self.bazaar, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil],
                         [self.fence, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil, self.soil],
                         ]
            self.maxHeight = len(self.farm) - 1
            self.maxWidth = len(self.farm[0]) - 1

    def plantstuff(self):
        self.farm[self.y][self.x] = "."
        self.planttime.append([self.globetime, self.x, self.y])

    def growself(self):
        self.globetime += 1
        for plant, x, y in self.planttime:
            if plant == self.globetime - self.growtime / 2:
                self.farm[y][x] = "v"

            if plant == self.globetime - self.growtime:
                self.farm[y][x] = "V"
