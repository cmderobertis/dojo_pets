class Pet:
  def __init__(self, name, type, tricks, health, energy) -> None:
    self.name = name
    self.type = type
    self.tricks = tricks
    self.health = health
    self.energy = energy
  
  def sleep(self):
    self.energy += 25
  
  def eat(self):
    self.energy += 5
    self.health += 10
    print(f"{self.name} is happily eating.")
  
  def play(self):
    self.health += 5
    print(f"{self.name} is playing! How exciting.")
  
  def noise(self):
    print(self.sound)