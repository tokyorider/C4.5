from model.attributes import *

parse_table = {
    'SUN': SUN, 'OVERCAST': OVERCAST, 'RAIN': RAIN, 'HOT': HOT, 'SWEET': SWEET, 'COLD': COLD, 'LOW': LOW,
    'NORMAL': NORMAL, 'HIGH': HIGH
}

def parse_data():
    return tuple(parse_table.get(input().upper()) for attr in Attribute)