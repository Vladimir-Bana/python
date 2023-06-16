class Animal:
    def __init__(self,species,sound):
        self.species=species
        self.sound=sound
    def show_species(self):
        print(f"I am: {self.species}")
    def make_sound(self):
        print(f"Makes such a sound: {self.sound}")
Dog = Animal("Dog", "Gaf Gaf Gaf")
Cat = Animal("Cat", "Myau Myau Myau")
arr = ["Dog","Cat"]
def show_animal_info(name):
    if name not in arr:
        print("Book this is not an animal!")
    else:
        name=Dog
        name.show_species()
        name.make_sound()
        name=Cat
        name.show_species()
        name.make_sound()
show_animal_info("Dog")
