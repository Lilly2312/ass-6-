

"""=========================================================================================================="""

"""Assignment 2:-"""
#Task-1: Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

class Dog:
    def __init__(self,name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"name : {self.name} \nage : {self.age}")

    def get_info(self):
        print(f"coat_color : {self.coat_color}")

class JackRussellTerrier(Dog):
    
    def origin_country(self,country):
        self.country = country
        print(f"origin country : {self.country}")
    def max_weight(self,weight):
        self.weight = weight
        print(f"Max weight of dog : {self.weight}")

class Bulldog(JackRussellTerrier):

    def Breed(self,breed):
        self.breed = breed
        print(f"Breed of dog : {self.breed}")
    def Size(self,size):
        self.size = size
        print(f"size of dog : {self.size}")

print("dog-1:- ")
jack = Bulldog("JackRussellTerrier", "2years", "white")
jack.description()
jack.get_info()
jack.origin_country("England")
jack.max_weight("8Kgs")

print("\ndog-2:- ")
bull = Bulldog("Labrode", "3.5Years", "Golden")
bull.description()
bull.get_info()
bull.Breed("mastiff")
bull.Size("Medium")
