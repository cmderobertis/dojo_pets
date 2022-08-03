from classes.pet import Pet


class Cat(Pet):
  def __init__(self, name, tricks, health, energy) -> None:
    super().__init__(name, 'cat', tricks, health, energy)
    self.sound = 'Meeooowww...'
