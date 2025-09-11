class Temperature:
    unit = "Celsius"
    def __init__(self, value):
        self.__value = value

    def display(self):
        print(str(self.__value) + self.unit)

    def change_unit(cls, unit):
        cls.unit = unit

    def to_fahrenheit(celsius):
        return celsius * (9/5) + 32
    
t1 = Temperature(100)
t1.display()
print(Temperature.to_fahrenheit(100))
t1.change_unit("Kelvin")
t1.display()