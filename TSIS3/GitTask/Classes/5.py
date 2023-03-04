
class A():
    def __init__(self, owner):
        self.owner = owner
        self.b = 0
    
    def checkB(self):
        print(f"Balance: {self.b}")

    def deposit(self, a):
        self.b += a
        print(f"{a} deposite")

    def withdraw(self, a):
        if a > self.b:
            print("Not enough")
        else:
            self.b -= a
            print(f"{a} withdraw")

q = A("Aidar")
q.checkB()
q.deposit(10000)
q.checkB()
q.withdraw(3500)
q.checkB()