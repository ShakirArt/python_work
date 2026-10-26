class car:
    def __init__(self,numbr):
        self.numbr= numbr

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


class bmw(car):  #inheritance, child class
    def __init__(self, model, numbr):
        super().__init__(numbr)  #super() is used to call the constructor of the parent class
        self.model = model

bmw1 = bmw("X5", 123)
bmw1.start()  #inherited method from parent class   
bmw2 = bmw("X6")
bmw2.stop()  #inherited method from parent class