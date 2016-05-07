class Room(object):
    index = []
    name_index = {}
    loc_index = {}

    # instantiate object and add to class-level indexes
    def __init__(self, name, x, y, z=0, ):
        if name in Room.name_index:
            raise KeyError('That name is already in use for another room')
        if (x, y, z) in Room.loc_index:
            raise KeyError('That location is already in use for another room')
        self.contents = []
        self.inhabitants = []
        self.name = name
        self.x, self.y, self.z = x, y, z
        self.index = len(Room.index)
        self.coordinates = x, y, z
        self.loc = x, y, z
        Room.index.append(self)
        Room.name_index[name] = self
        Room.loc_index[(x, y, z)] = self
        Mob.loc_index[self] = []

        # self.north = get_room_from_direction(self.loc, 'north')
        # self.east = get_room_from_direction(self.loc, 'east')

        # return a dictionary based on a query
        # can take name (str), loc (tuple, or index (int)
    def lookup(query):
        if isinstance(query, str):
            out = Room.name_index[query]
            return out
        if isinstance(query, int):
            out = Room.index[query]
            return out
        if isinstance(query, tuple):
            out = Room.loc_index[query]
            return out

    def __repr__(self):
        return "<%s: Room object located at x=%s, y=%s, z=%s,\
 inhabitants=%s, contents=%s>" % (self.name, self.x, self.y, self.z,
                                  self.inhabitants, self.contents)

    def __str__(self):
        return "<Room: %s>" % self.name


# class for creatures in the world
class Mob(object):
    index = []
    name_index = {}
    loc_index = {}

    def __init__(self, name, loc, inventory=[], health=10, ducats=0):
        self.name = name
        self.loc = loc
        self.inventory = inventory
        self.health, self.ducats = health, ducats
        self.index = len(Mob.index)
        Mob.index.append(self)
        if name in Mob.name_index:
            Mob.name_index.append(self)
        else:
            Mob.name_index[name] = [self]
        Mob.loc_index[loc].append(self)
        Mob.index.append(self)
        self.loc.inhabitants.append(self)

    def lookup(query):
        if isinstance(query, str):
            out = Mob.name_index[query]
            return out
        if isinstance(query, int):
            out = Mob.index[query]
            return out
        if isinstance(query, tuple):
            out = Mob.loc_index[query]
            return out

    # return the room in a given direction
    def get_room_in_direction(self, direction):
        if direction not in Constants.valid_directions:
            raise LookupError('Not a valid direction')
        new_loc = get_direction_loc(self.loc.loc, direction)
        if new_loc not in Room.loc_index:
            return False
        else:
            return Room.loc_index[new_loc]

    def move(self, direction):
        intended_location = self.get_room_in_direction(direction)
        if intended_location:
            self.loc.inhabitants.remove(self)
            self.loc = intended_location
            self.loc.inhabitants.append(self)
        return intended_location

    def __repr__(self):
        return "<%s: Mob object located at %s,\
 inventory=%s, ducats=%s, health=%s>" % (self.name, self.loc, self.inventory,
                                         self.ducats, self.health)

    def __str__(self):
        return "<Mob: %s>" % self.name


class Constants(object):
    valid_directions = ('n',
                        's',
                        'e',
                        'w',
                        'u',
                        'd',
                        'north',
                        'south',
                        'east',
                        'west',
                        'up',
                        'down',
                        'ne',
                        'se',
                        'nw',
                        'sw',
                        'northeast',
                        'southeast',
                        'northwest',
                        'southwest', )


# takes location tuple and string for direction, i.e. "north"
# returns new location
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


def debug_indexes():
    print('''Room location index:
    ''')
    print(Room.loc_index)
    print('''Room index:
    ''')
    print(Room.index)
    print('''Room name index:
    ''')
    print(Room.name_index)
    print('''Mob location index
    ''')
    print(Mob.loc_index)
    print('''Mob index:
    ''')
    print(Mob.index)
    print('''Mob name index:
    ''')
    print(Mob.name_index)


# if __name__ == '__main__':
house = Room('house', 10, 10)
barn = Room('barn', 10, 11)
player = Mob('Player', Room.lookup('house'))



