import unittest

def intersection(rect_0, rect_1):

    left_x = rect_1['left_x']
    bottom_y = rect_1['bottom_y']
    width = rect_0['left_x'] + rect_0['width'] - rect_1['left_x']
    height = rect_0['bottom_y'] + rect_0['height'] - rect_1['bottom_y']

    if rect_0['bottom_y'] > rect_1['bottom_y']:
        bottom_y = rect_0['bottom_y']
        height = rect_1['bottom_y'] + rect_1['height'] - rect_0['bottom_y']


    if left_x > rect_0['left_x'] + rect_0['width'] or bottom_y > rect_0['bottom_y'] + rect_0['height']:
        return None

    return {
        'left_x': left_x,
        'bottom_y': bottom_y,
        'width': width,
        'height': height
    }

class TestIntersection(unittest.TestCase):

    def test_bottom_right(self):
        rect_0 = {
            'left_x': 0,
            'bottom_y': 1,
            'width': 10,
            'height': 4,
        }

        rect_1 = {
            'left_x': 5,
            'bottom_y': 0,
            'width': 10,
            'height': 4,
        }

        rect_int = intersection(rect_0, rect_1)

        self.assertIsNotNone(rect_int)
        self.assertEqual(rect_int['left_x'],5)
        self.assertEqual(rect_int['bottom_y'],1)
        self.assertEqual(rect_int['width'], 5)
        self.assertEqual(rect_int['height'], 3)


    def test_same_rect(self):
        rect_0 = {
            'left_x': 1,
            'bottom_y': 5,
            'width': 10,
            'height': 4,
        }

        rect_int = intersection(rect_0, rect_0)

        self.assertIsNotNone(rect_int)
        self.assertEqual(rect_int['left_x'], rect_0['left_x'])
        self.assertEqual(rect_int['bottom_y'], rect_0['bottom_y'])
        self.assertEqual(rect_int['width'], rect_0['width'])
        self.assertEqual(rect_int['height'], rect_0['height'])
    #
    # ____________
    # |    |_____|
    # |    (5,8) |
    # |          |
    # |__________|
    # (1,5)
    #
    #
    #
    # (0,0)
    def test_top_right_corner_intersection(self):
        rect_0 = {
            'left_x': 1,
            'bottom_y': 5,
            'width': 10,
            'height': 4,
        }

        rect_1 = {
            'left_x': 5,
            'bottom_y': 8,
            'width': 10,
            'height': 4,
        }

        rect_int = intersection(rect_0, rect_1)

        self.assertIsNotNone(rect_int)
        self.assertEqual(rect_int['left_x'],5, 'left_x')
        self.assertEqual(rect_int['bottom_y'],8, 'bottom_y')
        self.assertEqual(rect_int['width'], 6)
        self.assertEqual(rect_int['height'], 1, 'height')

    def test_no_intersection(self):
        rect_0 = {
            'left_x': 1,
            'bottom_y': 5,
            'width': 10,
            'height': 4,
        }

        rect_1 = {
            'left_x': 100,
            'bottom_y': 500,
            'width': 10,
            'height': 4,
        }

        assert intersection(rect_0, rect_1) is None


if __name__ == '__main__':
    unittest.main()