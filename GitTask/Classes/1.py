class Upper:
    def getString(self):
        self.a=input()
    def printString(self):
        print(self.a.upper())

v=Upper()
v.getString()
v.printString()