class Board():
    def __init__(self):
        grid = []
        for i in range(1,16):
            grid.append([])
            for j in range(1,16):
                grid[i-1].append("")
        print(grid)
        boardDetails = open("boardTiles.txt","r")
        line = boardDetails.readline()
        print(line)
        for row in grid:
            index = 0
            for tile in row:
                row[index]=line[index]
                print("yes")
                index+=1
            boardDetails.readline()
        print(grid)
