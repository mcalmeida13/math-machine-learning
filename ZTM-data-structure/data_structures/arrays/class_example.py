class ClassExample:

    def __init__(self,name, type):
        # Constructor
        self.name = name
        self.type = type

    
    def introduce(self):
        print(f"Hi, my name is {self.name}, I'm a {self.type}")



knight = ClassExample('Manuela','Knight')
wizard = ClassExample('Rebecca','Wizard')

knight.introduce()
wizard.introduce()