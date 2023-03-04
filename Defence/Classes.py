class Car():
    def __init__(self, engine, mark, color):
        self.engine=engine
        self.mark=mark
        self.color=color
    def printInfo(self):
        print(self.engine, self.mark, self.color)

    def set_year(self, b):
        self.year=b
    def get_year(self):
        print(self.year)

class Toyota(Car):
    def __init__(self, engine, mark, color):
        self.country="Japan"
        Car.__init__(self, engine, mark, color)
    def printInfo(self):
        print(self.country, self.engine, self.mark, self.color)

    def set_price(self, a):
        self.price=a

    def get_price(self):
        print(self.price)

v=Toyota('internal combustion engine', 'Corolla', 'Black')
l=Car('internal combustion engine', 'Corolla', 'Black')
v.set_price(2000000)
l.set_year(2019)


v.printInfo()
v.get_price()
l.get_year()
