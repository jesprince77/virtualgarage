class Vehicle:

  def __init__(self):
    #dictionary of options
    self.vehicle_options = {'make': '', 'model': ''}

  def setMake(self, make):
    self.vehicle_options['make'] = make

  def setModel(self, model):
    self.vehicle_options['model'] = model

  def getMake(self):
    return self.vehicle_options['make']

  def getModel(self):
    return self.vehicle_options['model']


class Car(Vehicle):

  def setCarDoors(self, doors):
    self.str_doors = doors

  def getCarDoors(self):
    return self.str_doors


class Truck(Vehicle):

  def setBedLength(self, bedLength):
    self.str_bedlength = bedLength

  def getBedLength(self):
    return self.str_bedlength


print(f"Welcome to Bellevue University Virtual Garage")
print(f"")
selection = 0
while int(selection) < int(3):
  selection = input("Enter 1 to make a car, 2 to make a truck, or 3 to quit: ")
  print("")
  if (selection == '1'):
    new_car = Car()
    strMake = input("Please enter the car make:")
    new_car.setMake(strMake)
    strModel = input("Please enter the car model:")
    new_car.setModel(strModel)
    strDoors = input("Please enter the number of doors:")
    new_car.setCarDoors(strDoors)
    print("")
    print(f"The number of doors: {new_car.getCarDoors()}")
    print(f"The make is: {new_car.getMake()}")
    print(f"The model is: {new_car.getModel()}")
    print(f"You car has been added to the Garage.")
  elif (selection == '2'):
    new_truck = Truck()
    strMake = input("Please enter the truck make:")
    new_truck.setMake(strMake)
    strModel = input("Please enter the truck model:")
    new_truck.setModel(strModel)
    strDoors = input("Please enter the bed length:")
    new_truck.setBedLength(strDoors)
    print("")
    print(f"The bed length is: {new_truck.getBedLength()}")
    print(f"The make is: {new_truck.getMake()}")
    print(f"The model is: {new_truck.getModel()}")
    print(f"Your truck has been added to the Garage.")
  else:
    print("")
    print("Thank you for using the Bellevue University Virtual Garage.")
  print("")
