import entities
import random

adj = [
    'old', 'new', 'broken-down', 'unsightly', 'beautiful', 'appealing',
    'ancient', 'sublime', 'ungodly', 'questionable'
]

noun = [
    'lodge', 'house', 'barn', 'pasture', 'waterfall', 'pigpen', 'well',
    'hillock', 'gorge', 'glade'
]


# creates rooms and assigns them random names
# if name exists, it runs again
def room_gen(x, y, name_list=[]):
    name = random.choice(adj) + ' ' + random.choice(noun)
    if name in name_list:
        room_gen(x, y)
    else:
#        print(name)
        name_list.append(name)
        room = entities.Room(name, x, y)
        return room


# create a map of x and y dimensions        
def create_map(x, y, z=0):
    for w in range(x):
        for h in range(y):
            room_gen(w, h)

    return entities.Room.index

world = create_map(10, 10)


