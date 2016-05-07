import unittest
import entities


class InstantiationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
#        print('setup for instant')
        entities.Room('room', 40, 12)
        entities.Room('barn', 5, 5)
        entities.Room('pasture', 6, 5)
        entities.Mob('P', entities.Room.lookup('barn'))

    @classmethod        
    def tearDownClass(self):
#        print('instant teardown')
        for room in entities.Room.index:
            del room
        entities.Room.index = []
        entities.Room.name_index = {}
        entities.Room.loc_index = {}
        entities.Mob.index = []
        entities.Mob.name_index = {}
        entities.Mob.loc_index = {}



class MovementTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
#        print('setup for move')
        entities.Room('lake', 10, 10)
        entities.Room('boathouse', 11, 10)
        entities.Mob('Player', entities.Room.lookup('lake'))

    @classmethod        
    def tearDownClass(self):
#        print('movement teardown')
        for room in entities.Room.index:
            del room
        entities.Room.index = []
        entities.Room.name_index = {}
        entities.Room.loc_index = {}
        entities.Mob.index = []
        entities.Mob.name_index = {}
        entities.Mob.loc_index = {}
       

class InstantiationTests(InstantiationTestCase):
    def test_get_direction_function(self):
        self.assertEqual(
            entities.get_direction_loc(
                (5, 5, 5), 'north'), (5, 6, 5))
        self.assertEqual(
            entities.get_direction_loc(
                (5, 5, 5), 'east'), (6, 5, 5))
        self.assertEqual(
            entities.get_direction_loc(
                (5, 5, 5), 'south'), (5, 4, 5))
        self.assertEqual(
            entities.get_direction_loc(
                (5, 5, 5), 'west'), (4, 5, 5))
        self.assertEqual(
            entities.get_direction_loc(
                (5, 5, 5), 'up'), (5, 5, 6))
        self.assertEqual(
            entities.get_direction_loc(
                (5, 5, 5), 'down'), (5, 5, 4))

    def test_room_instatiation(self):
        entities.Room('house', 10, 15)
        self.assertEqual(entities.Room.name_index['house'].name, 'house')
        self.assertEqual(entities.Room.name_index['house'].x, 10)
        self.assertEqual(entities.Room.name_index['house'].y, 15)

    def test_room_lookup(self):
        room = entities.Room.lookup('room')
        self.assertEqual(room.name, 'room')
        self.assertEqual(room.coordinates, (40, 12, 0))

    def test_player_instantiation(self):
        p = entities.Mob.lookup('P')[0]
        self.assertEqual(p.name, 'P')
        self.assertEqual(p.health, 10)
        room_inhabitants = entities.Room.lookup('barn').inhabitants
        self.assertEqual('P', room_inhabitants[0].name)


class MovementTests(MovementTestCase):
    def test_player_movement(self):
        player = entities.Mob.lookup('Player')[0]
        player.move('east')
        self.assertEqual(player.loc.name, 'boathouse')

    def test_update_indexes_on_move(self):
        player = entities.Mob.lookup('Player')[0]
        self.assertEqual(player, player.loc.inhabitants[0])
        self.assertEqual(entities.Room.lookup('lake').inhabitants, [])


if __name__ == '__main__':
    unittest.main()
