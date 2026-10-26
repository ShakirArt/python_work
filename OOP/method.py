#methods are just functions in a class


class Person:
  def __init__(self, name):
    self.name = name
    self.age = 23

  def talk(self):
    print("Hello, my name is " + self.name)

p1 = Person("Shakira")
p1.talk()
print("age",p1.age)

