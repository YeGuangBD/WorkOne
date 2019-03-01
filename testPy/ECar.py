from Car import Car

class ECar(Car):
    """docstring for ClassName"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        

myECar=ECar("audi","a4",2018)
print(myECar.get_descriptive_name())