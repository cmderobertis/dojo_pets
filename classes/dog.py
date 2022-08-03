from classes.pet import Pet


class Dog(Pet):
  def __init__(self, name, tricks, health, energy) -> None:
    super().__init__(name, 'dog', tricks, health, energy)
    self.sound = 'Woof! Woof!'
