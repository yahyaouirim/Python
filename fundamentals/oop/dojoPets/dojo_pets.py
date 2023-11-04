class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, noise):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=50
        self.energy=20
        self.noise=noise
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy+=25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy+=5
        self.health+=10
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health+=5
        self.energy-=10
        return self
# noise() - prints out the pet's sound
    def noise(self):
        return self.noise
# class Ninja
class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet

# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if (len(self.pet_food)>0):
            food=self.pet_food.pop()
            print(f"Feeding, {self.pet.name} {food}")
            self.pet.eat()
        else:
            print("Oh no, your pet need more food!!!")
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()

# call the methods
pet_food1=["food1", "food2", "food3"]
treats1=["treat1","treat2", "treat3"]
my_pets=Pet("MrsBird", "bird",["fly", "hide"], "ziw ziw")
my_ninja=Ninja("Rim", "Yahyaoui", treats1, pet_food1, my_pets)
my_ninja.feed()
my_ninja.feed()
my_ninja.feed()
my_ninja.feed()




        

