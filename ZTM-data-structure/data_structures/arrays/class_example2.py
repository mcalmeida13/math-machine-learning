class Player():

    def __init__(self,name, type):
        # Constructor
        print('player',self)
        self.name = name
        self.type = type

    
    def introduce(self):
        print(f"Hi, my name is {self.name}, I'm a {self.type}")

class Wizard(Player):

    def __init__(self,name,type):
        # Constructor
        super().__init__(name,type)
        print('wizard',self)
    
    def play():
        print("WEEEEEE")


knight = Wizard('Manuela','Knight')

knight.introduce()