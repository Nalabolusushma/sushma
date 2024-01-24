class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printname(self):
    print(self.name,self.age)

class Student(Person):
  pass

x = Student("Mike", 10)
x.printname()