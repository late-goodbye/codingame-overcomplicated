import unittest
from easy.rectangle_partition.rectangle_partition import Rectangle, Universe


class TestRectangle(unittest.TestCase):

    def test_rectangle_create(self):

        rectangle = Rectangle(0, 1, 0, 1)

        self.assertEqual(rectangle.x1, 0)
        self.assertEqual(rectangle.x2, 1)
        self.assertEqual(rectangle.y1, 0)
        self.assertEqual(rectangle.y2, 1)

    def test_rectangle_is_square(self):

        rectangles = [
            Rectangle(0, 0, 0, 0),
            Rectangle(0, 1, 0, 1),
            Rectangle(1, 1, 1, 1),
            Rectangle(2, 5, 7, 10),
            Rectangle(-4, -2, 2, 4),
        ]

        for rectangle in rectangles:
            self.assertTrue(rectangle.is_square)

    def test_rectangle_is_not_square(self):

        rectangles = [
            Rectangle(0, 0, 0, 1),
            Rectangle(1, 1, 0, 1),
            Rectangle(2, 5, 4, 6),
            Rectangle(-4, -2, -2, -1),
        ]

        for rectangle in rectangles:
            self.assertFalse(rectangle.is_square)


if __name__ == '__main__':
    unittest.main()
