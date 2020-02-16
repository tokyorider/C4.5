from enum import Enum

SUN, OVERCAST, RAIN = 0, 1, 2
HOT, COLD, SWEET = 0, 1, 2
LOW, NORMAL, HIGH = 0, 1, 2

class Attribute(Enum) :
    OUTLOOK = 0
    TEMPERATURE = 1
    HUMIDITY = 2
    WIND = 3

# attributes = {
#     Attribute.OUTLOOK : {SUN, OVERCAST, RAIN},
#     Attribute.TEMPERATURE : {HOT, COLD, SWEET},
#     Attribute.HUMIDITY : {LOW, NORMAL, HIGH},
#     Attribute.WIND : {LOW, NORMAL, HIGH}
# }