import time

class Ninja:
  def __init__(self, first_name, last_name, pet, treats, pet_food) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.pet = pet
    self.treats = treats
    self.pet_food = pet_food
  
  def walk(self):
    print(f"{self.first_name} {self.last_name} and {self.pet.name} are out for a walk...")
    time.sleep(1)
    self.pet.play()

  def feed(self):
    print(f"{self.first_name} is feeding the {self.pet_food} to {self.pet.name}...")
    time.sleep(1)
    self.pet.eat()

  def bathe(self):
    print(f"{self.first_name} is bathing their {self.pet.type}...")
    time.sleep(1)
    self.pet.noise()