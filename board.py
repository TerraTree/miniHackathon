class Board():
    def __init__(self,grid):
        self.grid=grid

    def checkAdjacent(self,position):
        possibleMovements = []
        grid=self.grid
        if grid[self.position[0]][self.position[1]-1] != "-":
            possibleMovements.append("left")
        elif grid[self.position[0]][self.position[1]+1] != "-":
            possibleMovements.append("right")
        elif grid[self.position[0]-1][self.position[1]] != "-":
            possibleMovements.append("up")
        elif grid[self.position[0]+1][self.position[1]] != "-":
            possibleMovements.append("down")
        print(possibleMovements)
        return possibleMovements