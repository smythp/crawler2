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
        self.info = {}
        self.info['index'] = len(Room.index)
        self.info['obj'] = self
        self.info['name'] = name
        self.info['contents'] = contents
        self.info['inhabitants'] = inhabitants
        self.info['x'], self.info['y'], self.info['z'] = x, y, z
        self.info['loc'] = (x, y, z)
        Room.index.append(self.info)
        Room.name_index[name] = self.info
        Room.loc_index[(x, y, z)] = self.info

    # return a dictionary based on a query
    # can take name (str), loc (tuple, or index (int)
    def lookup(query):
        if isinstance(query, str):
            info = Room.name_index[query]
            return info
        if isinstance(query, int):
            info = Room.index[query]
            return info
        if isinstance(query, tuple):
            info = Room.loc_index[query]
            return info

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
