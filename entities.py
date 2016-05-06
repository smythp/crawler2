class Room(object):
    index = []
    name_index = {}
    loc_index = {}

    # instatiate object and add to class-level indexes
    def __init__(self, name, x, y, z=0, inhabitants=[], contents=[]):
        if name in Room.name_index \
           or (x, y, z) in Room.loc_index:
            raise KeyError('Key already in use')
        self.name = name
        self.x, self.y, self.z = x, y, z
        self.contents, self.inhabitants = contents, inhabitants
        self.index = len(Room.index)
        self.coordinates = x, y, z
        Room.index.append(self)
        Room.name_index[name] = self
        Room.loc_index[(x, y, z)] = self
        Mob.loc_index[self] = []

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
 inhabitants=%s, contents=%s>" % (
            self.name, self.x, self.y, self.z,
            self.inhabitants, self.contents)

    def __str__(self):
        return "<Room: %s>" % self.name


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

    def __repr__(self):
        return "<%s: Mob object located at %s,\
 inventory=%s, ducats=%s, health=%s>" % (
            self.name, self.loc,
            self.inventory, self.ducats, self.health)

    def __str__(self):
        return "<Mob: %s>" % self.name
        
        
        
        


    
        
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

        # Room('house', 10, 12)
        # Room('barn', 11, 12)
        # Room('lake', 40, 12, contents=['hat'])

        # for room in Room.index:
        #     print(room['index'])

        # #print(Room.lookup('lake'))

# Room('house', 10, 12, contents=['football'])
# print(Mob.loc_index)
# patrick = Mob('Patrick', Room.lookup('house'))
# print(Mob.loc_index)
# print(patrick.loc.contents)        
# print(patrick.index)
