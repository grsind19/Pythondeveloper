class SpaceShip():
  def __init__(self):
    self.callsign = ''
    self._shieldStrength = 100
  
  def fireMissile(self):
    return "Pwe@"
  
  def reduceShieldStrenth(self, amount):
    self._shieldStrength -= amount


myShip = SpaceShip()

# Allocate the space of the memory for the variables
