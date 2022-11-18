#Composition --> House with 3 rooms

class House:
  def __init__(self, address, room_one, room_two, room_three):
    self.address = address
    self.room_one = room_one
    self.room_two = room_two
    self.room_three = room_three

  def getAddress(self):
    return self.address
  
  def getTotalDimension(self):
    result = self.room_one.getRoomDimension() + self.room_two.getRoomDimension() + self.room_three.getRoomDimension()
    return print(f"The total dimension od the house is: {result} square meters")
  
  def getRoomTypes(self):
    return print(f"The current house has a {self.room_one.getRoomType()} a {self.room_two.getRoomType()} and a {self.room_three.getRoomType()}")

class Room:
  def __init__(self, type, dimension):
    self.type = type
    self.dimension = dimension
  
  def getRoomType(self):
    return self.type

  def getRoomDimension(self):
    return self.dimension


room_one = Room("Toilet", 4)
room_two = Room("Kitchen", 9)
room_three = Room("Living Room", 10)
room_four = Room("Bedroom", 6)
room_five = Room("Toilet + Sauna", 12)
room_six = Room("Kitchen", 8)


house_one = House("Jyväskylä", room_one, room_two, room_three)
house_two = House("Tampere", room_six, room_three, room_four)
house_three = House("Helsinki", room_four, room_five, room_two)

print(f"The address of the house is: {house_one.getAddress()}")
house_one.getRoomTypes()
house_one.getTotalDimension()

print(f"The address of the house is: {house_two.getAddress()}")
house_two.getRoomTypes()
house_two.getTotalDimension()

print(f"The address of the house is: {house_three.getAddress()}")
house_three.getRoomTypes()
house_three.getTotalDimension()