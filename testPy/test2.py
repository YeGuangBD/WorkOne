from Car import Car
from ECar import ECar

myCar=Car("audi","a4",2018)
myECar=ECar("audi","a4",2018)
a= myCar.get_descriptive_name()
b=myECar.get_descriptive_name()
print(a)
print(b)