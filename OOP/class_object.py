class human:
    name="Shakira"      #here constructor function __init__ run by default when object is created
    age=23              

h1=human()
print(h1.name)
print(h1.age)
h2=human()
print(h2.name)

class home:
    country= "Bangladesh"       #class attribute is shared by all objects of the class. every home object will have the same country 
    def __init__(self):         #self is just reference to the object that is being created
        self.color="red"        #every class has a constructor method called __init__ which is called when an object is created 
        self.rooms=3            #self.atrribute means diffierent objects can have different values for the same attribute
        self.bathrooms=2

home1=home()
print(home1.color)
print(home1.rooms)
print(home1.bathrooms)
print(home1.country)        #obj call
print(home.country)         #class attribute call

class hobby:
    def __init__(self, name):           #parameterized constructor
        self.name=name              #here self.attribute is assigned the value of the parameter passed during object creation

h3=hobby("Reading")
print(h3.name)