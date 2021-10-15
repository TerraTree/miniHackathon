class Board():
    def __init__(self,grid):
        self.grid=grid

    def checkAdjacent(self,position):
        possibleMovements = []
        grid=self.grid
        if grid[position[0]][position[1]-1] != "-":
            possibleMovements.append("left")
        if grid[position[0]][position[1]+1] != "-":
            possibleMovements.append("right")
        if grid[position[0]-1][position[1]] != "-":
            possibleMovements.append("up")
        if grid[position[0]+1][position[1]] != "-":
            possibleMovements.append("down")
        return possibleMovements