class Kettle(object):

    power_source = "Electricity"

    def __init__(self, make, price):  # __init__ is the constructor in python
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All object created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("=" * 40)

kenwood.power = 1.5
print(kenwood.power)  # python allows dynamic attribution at the instance level
# print(hamilton.power)  # however you need to be careful when doing so

print("Switch to atomic power")
Kettle.power_source = "atomic"  # changing attribute values at the class level changes all instances
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = 'gas'
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)