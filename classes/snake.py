from classes.pet import Pet

class Snake(Pet):
  def __init__(self, name, tricks, health, energy) -> None:
    super().__init__(name, 'snake', tricks, health, energy)
    
    self.sound = 'Sssss....'