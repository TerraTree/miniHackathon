class Character():
    def __init__(self,name,knowledge,position,aiControlled):
        self.name=name
        self.knowledge = knowledge
        self.position = position
        self.aiControlled=aiControlled
        self.cards = []

    def move(self, dir):
        direction = dir.lower()
        print(direction)
        if direction == "left":
            self.position[1]-=1
        elif direction == "right":
            self.position[1]+=1
        elif direction =="up":
            self.position[0]-=1
        elif direction == "down":
            self.position[0]+=1
        print("Y:", self.position[0])
        print("X:", self.position[1])

    def findClosestRoom(self,grid,roomDistances):

        return location