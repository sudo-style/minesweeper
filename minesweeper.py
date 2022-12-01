import random

class minefield():
    def __init__(self,h,w,m):        
        self.height = h
        self.width = w
        self.mines = set()
        self.grid = [[0 for height in range(h)] for width in range(w)]
        self.userGrid = [[0 for height in range(h)] for width in range(w)]
        for _ in range(m):
            self.addMines()


    # if a mine is already set, it will try again, and notify if too many nodes are set
    def addMines(self):
        x,y = (random.randint(0,self.width - 1),random.randint(0,self.height - 1))

        if len(self.mines) >= self.height * self.width:
            print("ERROR: TOO MANY MINES")
            return

        if (x,y) in self.mines:
            self.addMines()
            return 
        self.mines.add((x,y))

        # need to set the surrounding areas around the mine
        self.grid[x][y] = -1

        # check when we should do it
        # at each mine plus 1 going up down left and right
        # this shouldn't be this grid but another grid
        offset = [-1,0,1]
        for xOffset in offset:
            for yOffset in offset:
                if ((x + xOffset < self.width) and (x + xOffset >= 0) and
                    (y + yOffset < self.height) and (y + yOffset >= 0)):
                    self.userGrid[x + xOffset][y + yOffset] += 1

    def printGrid(self):
        for line in self.grid:
            print(line)
            
    def printUserGrid(self):
        for line in self.userGrid:
            print(line)

        
def main():
    # the user will select a spot
    # the minefield will check if it was a bomb
    # create the surrounding area map 
    m = minefield(3,3,3)
   
    m.printGrid()
    print()
    m.printUserGrid()

main()
