            # №3
# class Human:
#     def __init__ (self,name,surname,place_of_birth,year_of_birth):
#         self.name=name
#         self.surname=surname
#         self.place_of_birth=place_of_birth
#         self.year_of_birth=year_of_birth
#     def hello(self):
#         print(F"says hello {self.name}")
#     def info_age(self,years):
#         return print(years-self.year_of_birth)
# Den=Human("Den","Dmiteiev","UA",1997)
# Den.hello()
# Den.info_age(2022)
            # №3
class Human:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        print("Peraason created")
    def hello(self):
        print(F"{self.name} says hello")
class student(Human):
    def __init__ (self,name,age,course,mark):
        Human.__init__(self,name,age)
        self.course=course
        self.mark=mark
    def study(self):
        print(F"{self.name} studing")
    def hello(self):
        print(F"Student created, {self.name} not says hello")
    def info_universal(self):
        print(f"student {self.name} , studing {self.course} , have grade {self.mark}")
class Teacher(Human):
    def teach(self):
        print(F"{self.name}-teachs, age:{self.age}")
s1=student("Zheka",17,1,5)
t1=Teacher("Den",24)
s1.hello()
# t1.hello()
# s1.study()
# t1.teach()
s1.info_universal()