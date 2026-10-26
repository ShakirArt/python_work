class student:
    def __init__(self, name, sub_mark,id):
        self.name=name
        self.sub_mark=sub_mark
        self.__id=id    #private attribute, can not be accessed outside the class. we can access it using getter and setter methods

    @staticmethod       #decorator
    def intro():
        print("Avarage marks of students")


    def avg(self):
        #sum= 0
        #for i in self.sub_mark:
        #    sum += i
        add= sum(self.sub_mark)             #in short we can write sum(self.sub_mark)/len(self.sub_mark) to get average mark
        n= len(self.sub_mark)
        avg_mark= add/n
        return avg_mark

student.intro()
s1=student("Shakira", [90,80,70])
print(s1.name, "Average mark:", s1.avg())
s2=student("Samiha", [90,98,91])
print(s2.name, "Average mark:", s2.avg())