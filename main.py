import board
import character
import random
import card


def investigate(room, programAsked, programAsking, malware, programGrid):
    cardRequest = input("Enter player to ask about if they know anything")
    for program in programGrid:
        if program.name == cardRequest:
            matches = []
            for card in program.cards:
                if card.name == room or malware or programAsked.name:
                    matches.append(card)
            if program.aiControlled:
                choice = random.choice(matches)
            else:
                print("Cards to reveal")
                for match in matches:
                    print(match.name)
                check = int(input("Enter card to reveal"))
                if 0 < check - 1 < len(matches):
                    choice = match[check - 1]
            programAsking.knowledge.append(choice)
            if not programAsking.aiControlled:
                print("You took "+choice.name)
            break
    # programAsked is moved into room
    # ask another player if they know anything
    # they reveal one of their "cards"


grid = []
for i in range(1, 16):
    grid.append([])
    for j in range(1, 16):
        grid[i - 1].append("")
    print(grid)
    boardDetails = open("boardTiles.txt", "r")
    line = boardDetails.readline()
    print(line)
    for row in grid:
        index = 0
        for tile in row:
            row[index] = line[index]
            index += 1
        line = boardDetails.readline()
    print(grid)
newBoard = board.Board(grid)
char = character.Character("Colonel Chrome", [""], [0, 0], False)
char2 = character.Character("General Github", [""], [0, 0], True)
programGrid = [char, char2]
programGrid[0].cards.append(card.Card("virus", "malware"))
programGrid[0].cards.append(card.Card("CPU", "room"))
programGrid[0].cards.append(card.Card("Colonel Chrome", "program"))
programGrid[1].cards.append(card.Card("trojan", "malware"))
programGrid[1].cards.append(card.Card("RAM", "room"))
programGrid[1].cards.append(card.Card("General Github", "program"))
# location = char.findClosestRoom(grid,[])
while True:
    possibleMovement = newBoard.checkAdjacent(char.position)
    if (char.aiControlled):
        pass
    else:
        movement = input("Enter direction: ")
    for word in possibleMovement:
        if word == movement.lower():
            print(movement)
            oldLocation = grid[char.position[0]][char.position[1]]
            print("loc: " + oldLocation)
            char.move(movement)
            newLocation = grid[char.position[0]][char.position[1]]
            print("loc: " + newLocation)
            if oldLocation == "p" and newLocation != "p":
                print("event time!")

                accused = input("enter suspect: ")
                room = input("what room are you in? ")
                malware = input("what malware do you suspect? ")
                for program in programGrid:
                    if program.name == accused:
                        accusedProgram = program
                investigate(room, accusedProgram, char, malware, programGrid)
            break
