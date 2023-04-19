class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price, power):
        self.make = make
        self.price = price
        self.power = power
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99, 2.5)
print(kenwood.make)
print(kenwood.price)
print(kenwood.power)

kenwood.price = 1299
print(kenwood.price)

fujiwara = Kettle("Fujiwara", 123, 1.5)
print(fujiwara.make)

print("Models: {} = {} Power: {}, {} = {} Power: {}".format(kenwood.make, kenwood.price, kenwood.power, fujiwara.make, fujiwara.price, fujiwara.power))

print("Models: {0.make} = {0.price}, Power: {0.power},  {1.make} = {1.price}, Power: {1.power}".format(kenwood, fujiwara))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(fujiwara.on)
fujiwara.switch_on()
print(fujiwara.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

print(kenwood.power)
print(fujiwara.power)

print("Switch to atomic Power")
Kettle.power_source = "atomic Power"

print(Kettle.power_source)
print("Switch to Co2")
kenwood.power_source = "Co2"
print(kenwood.power_source)
print(fujiwara.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(fujiwara.__dict__)