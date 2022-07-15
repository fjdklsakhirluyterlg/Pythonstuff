class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

class Teacher(Person):
    def __init__(self, fname, lname):
  	    Person.__init__(fname, lname)

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

foo = Teacher("John", "Smith", "PHD")
print(foo.printname())