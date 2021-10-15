import board
import character

class Player():
    # location
    # movement
    pass

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
        line = boardDetails.readline()
    print(grid)
newBoard = board.Board(grid)
char = character.Character("Colonel Chrome",[],[0,0])
while True:
    possibleMovement = newBoard.checkAdjacent(char.position)
    movement = input("Enter direction: ")
    for word in possibleMovement:
        if word == movement.lower():
            print(movement)
            char.move(movement)
            break
