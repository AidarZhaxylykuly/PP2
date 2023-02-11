class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#John Doe


class Student(Person):
  pass


x = Student("Mike", "Olsen")
x.printname()
#Mike Olsen


class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    pass
#overrides parent's init


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
#inherits parent's init


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
#inherits parent's methods


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
#adding graduationyear variable(property)


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)