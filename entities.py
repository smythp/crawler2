class Room(object):
    list = []

    def __init__(self, name, x, y, z=0):
        self.name = name
        self.x, self.y, self.z = x, y, z
        self.info = {}
        self.info['obj'] = self
        self.info['name'] = name
        self.info['x'] = x
        self.info['y'] = y
        self.info['z'] = z
        self.info['loc'] = (x, y, z)
        Room.list.append(self.info)
        self.dir = {}


def get_direction_loc(loc, direction):
    loc = list(loc)
    if direction == 'n' or direction == 'north':
        modified_loc = loc[0], loc[1] + 1, loc[2]
        return modified_loc
    if direction == 'e' or direction == 'east':
        modified_loc = loc[0] + 1, loc[1], loc[2]
        return modified_loc
    if direction == 's' or direction == 'south':
        modified_loc = loc[0], loc[1] - 1, loc[2]
        return modified_loc
    if direction == 'w' or direction == 'west':
        modified_loc = loc[0] - 1, loc[1], loc[2]
        return modified_loc
    if direction == 'u' or direction == 'up':
        modified_loc = loc[0], loc[1], loc[2] + 1
        return modified_loc
    if direction == 'd' or direction == 'down':
        modified_loc = loc[0], loc[1], loc[2] - 1
        return modified_loc

