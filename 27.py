# class Human:
#     def __init__ (self,name,surname,age,birth):
#         self.name=name
#         self.susrname=surname
#         self.age=age
#         self.birth=birth
#         print("Human created")
#     def info(self):
#         print(f"Name:{self.name} , Surname:{self.susrname}, Age:{self.age}, Birth:{self.birth}")
# class Student(Human):
#     def study(self):
#         print(f"Student:{self.name} studing")
# class Teacher(Human):
#     def teach(self):
#         print(f"Name:{self.name} teaches")
# new_s=Student("Vova","Nedb",15,"19.04.06")
# new_s.info()
# new_s.study()

# №2
class Animal:
    def __init__(self,vid,name,birth,color,time):
        self.vid=vid
        self.name=name
        self.birth=birth
        self.color=color
        self.time=time
    def info(self):
        print(f"Vid:{self.vid} , Name:{self.name} , Surname:{self.susrname}, Birth:{self.birth}")
class dog(Animal):
    def bark(self):
        print(f"Vid:{self.vid} , Name: {self.name}, bark")
    def eat(self):
        print(f"Eating: {self.time}")
    def dr(self):
        print(f"birth: {2021-self.birth}")
class cat(Animal):
    def wash(self):
        print(f"Vid:{self.vid} , Name: {self.name}, washing")
    def sit(self):
        print(f"Cat sit on the window {2021-self.birth}")
class Frog(Animal):
    def kvakaet(self):
        print(f"Vid:{self.vid} , Name: {self.name} , Frog kvakaet: {2021-self.birth}")

a1= dog("Dog", "Dodi" , 2007 , "Darck" , "14:16")
a2= cat("Cat", "Larsik" , 2009 , "Purple" , "14:16")
a3= Frog("Frog", "Kvaka" , 2010 , "Green" , "14:16")
a1.bark()
a1.eat()
a1.dr()
a2.wash()
a2.sit()
a3.kvakaet()