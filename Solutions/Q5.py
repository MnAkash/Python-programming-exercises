class String(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s)


obj = String()
obj.getString()
obj.printString()
