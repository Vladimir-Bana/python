class Animal:
    def __init__(self, name, sound, job):
        self.name = name
        self.sound = sound
        self.job=job
    def species(self):
        print(f"Животное зовут: {self.name}")

    def song(self):
        print(f"Животное говорит {self.sound}")

    def work(self):
        print(f"Животное часто {self.job}")

class Dog(Animal):
    def __init__(self, name, sound,job):
        super().__init__(name, sound,job)


class Cat(Animal):
    def __init__(self, name, sound,job):
        super().__init__(name, sound,job)

class Parrot(Animal):
    def __init__(self, name, sound,job):
        super().__init__(name, sound,job)

class Frog(Animal):
    def __init__(self, name, sound,job):
        super().__init__(name, sound,job)
        

arr = ["dog", "cat","parrot","frog"]


def show_animal_info(a1, name, sound,job):
    if a1 not in arr:
        print("Такої тварини не має!")
    else:
        a1 = Dog(name, sound, job)
        a1.species()
        a1.song()
        a1.work()

show_animal_info("dog", "Jojo", "Woof","running")

def show_animal_info2(a2, name, sound,job):
    if a2 not in arr:
        print("Такої тварини не має!")
    else:
        a2 = Cat(name, sound, job)
        a2.species()
        a2.song()
        a2.work()
show_animal_info2("cat", "Liza", "Moew","sleeping")


def show_animal_info3(a3, name, sound,job):
    if a3 not in arr:
        print("Такої тварини не має!")
    else:
        a3 = Cat(name, sound, job)
        a3.species()
        a3.song()
        a3.work()
show_animal_info3("parrot", "Zhora", "Chik-chirik","flies")

def show_animal_info4(a4, name, sound,job):
    if a4 not in arr:
        print("Такої тварини не має!")
    else:
        a4 = Cat(name, sound, job)
        a4.species()
        a4.song()
        a4.work()
show_animal_info4("frog", "Frad", "Kva-kva","jumping")