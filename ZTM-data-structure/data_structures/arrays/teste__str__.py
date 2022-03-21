class MyClass:

    def __init__(self, anyNumber, anyString):
        self.anyNumber = anyNumber
        self.anyString = anyString

    def __str__(self):
        return 'MyClass(x=' + str(self.anyNumber) + ' ,y=' + self.anyString + ')'


myObject = MyClass(12345,"Hello")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())