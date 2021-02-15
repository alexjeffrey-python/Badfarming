class FarmMap:

    def __init__(self):
        self.x = 0
        self.y = 0

        self.farm = [["BRN", "·", "·", "·", "·"],
                     ["BZR", "·", "·", "·", "·"],
                     ["   ", "·", "·", "·", "·"],
                     ["   ", "·", "·", "·", "·"],
                     ["   ", "·", "·", "·", "·"]]

        self.maxHeight = len(self.farm) - 1
        self.maxWidth = len(self.farm[0]) - 1

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
                    print(" " + self.farm[row][column]  + " ", end=" ")
            print()
        print(self.x, self.y)
