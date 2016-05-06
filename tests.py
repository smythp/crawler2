import unittest
import entities


class crawler_tests(unittest.TestCase):
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
        self.assertEqual(entities.Room.index[0]['name'], 'house')
        self.assertEqual(entities.Room.index[0]['x'], 10)
        self.assertEqual(entities.Room.index[0]['y'], 15)


if __name__ == '__main__':
    unittest.main()
