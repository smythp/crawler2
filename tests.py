import unittest
import entities


class CrawlerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        entities.Room('barn', 5, 5)
        entities.Room('room', 40, 12, contents=['hat'])


class RunCrawlerTests(CrawlerTestCase):
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
        self.assertEqual(room.contents, ['hat'])
        self.assertEqual(room.coordinates, (40, 12, 0))

    def test_player_instantiation(self):
        player = entities.Mob('Player', entities.Room.lookup('barn'))



if __name__ == '__main__':
    unittest.main()
