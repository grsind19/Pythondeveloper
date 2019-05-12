# Static variable shared across all object

class SpaceShip():
  toughness = 0.0
  def __init__(self):
    self.callsign = ''
    self._shieldStrength = 100
  
  def fireMissile(self):
    return "Pwe@"
  
  def reduceShieldStrenth(self, amount):
    self._shieldStrength -= amount


myShip = SpaceShip()

SpaceShip.toughness = 20

# Allocate the space of the memory for the variables

# Static variables are defined with underlines

