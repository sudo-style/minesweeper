import random

states = ['⬜️','🚩','❔','💣']
gameMode = ['keepPlaying','Won','Lost']

class minefield():
    def __init__(self,h,w,m):
        self.gameModeState = gameMode[0]
        self.height = h
        self.width = w
        self.mines = set()
        self.grid = [[False for height in range(h)] for width in range(w)]
        self.userGrid = [[0 for height in range(h)] for width in range(w)]
        self.displayGrid = [[states[0] for height in range(h)] for width in range(w)]
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
        self.grid[x][y] = True

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

    def printDisplayGrid(self):
        for line in self.displayGrid:
            print(line)

    def userPicks(self):
        print("input x,y one at a time")
        y = int(input())
        x = int(input())

        #if it was a bomb display all bombs
        if (self.grid[x][y]):
            self.displayGrid[x][y] = states[-1]
            self.gameModeState = gameMode[2]
        elif (self.displayGrid != 0):
            self.displayGrid[x][y] = str(self.userGrid[x][y])
        else:
            # if it was 0 then unpack all zeros
            self.foundZero(x,y)
            
        #self.displayGrid[x][y]
        self.printDisplayGrid()

    def foundZero(self,x,y):
        self.displayGrid[x][y] = 0
        # display sourrounding neighbors
        offset = [-1,0,1]
        for xOffset in offset:
            for yOffset in offset:
                if ((x + xOffset < self.width) and (x + xOffset >= 0) and
                    (y + yOffset < self.height) and (y + yOffset >= 0)):
                    self.displayGrid[x + xOffset][y + yOffset] = str(self.userGird[x + xOffset][y + yOffset])
    def isWinner(self):
        # count the white squares on the display grid
        # if it is equal to how many mines they won
        total = 0
        for line in self.displayGrid:
            total += sum([block == states[0] for block in line])
        return total == len(self.mines)
def main():
    # the user will select a spot
    # the minefield will check if it was a bomb
    # create the surrounding area map 
    m = minefield(3,3,3)
   
    m.printGrid()
    print()
    m.printUserGrid()
    while(m.gameModeState == gameMode[0]):
        m.userPicks()
        if (m.isWinner()):
            m.gameModeState = gameMode[1]
            break
    print("player " + m.gameModeState)

if __name__ == "__main__":
    main()
