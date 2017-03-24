import unittest

import numpy as np

from images import remove_boundary


class TestImage(unittest.TestCase):
    def test_remove_boundary(self):
        image_input = np.ones((3, 5), np.uint8)
        image_input = image_input * 255
        image_input[1, 2] = 0
        expected = np.zeros((1, 1), np.uint8)
        self.assertEqual(expected, remove_boundary(image_input))


if __name__ == '__main__':
    unittest.main()
