import unittest

import numpy as np

from images import (get_lines_with_color, identify_paragraphs_in_image,
                    remove_boundary)


class TestImage(unittest.TestCase):
    def setUp(self):
        self.image_input = np.ones((3, 5), np.uint8)
        self.image_input = self.image_input * 255
        self.image_input[1, 2] = 0

    def test_remove_boundary(self):
        expected = np.zeros((1, 1), np.uint8)
        self.assertEqual(expected, remove_boundary(self.image_input))

    def test_lines_0_and_2_have_color_white(self):
        expected = [0, 2]
        self.assertEqual(expected, get_lines_with_color(self.image_input))

    def test_have_one_paragraph(self):
        paragraphs, image = identify_paragraphs_in_image(self.image_input)
        self.assertEqual(1, paragraphs)

    def test_have_two_paragraphs(self):
        image = np.ones((3, 5), np.uint8)
        image = image * 255
        image[0, 2] = 0
        image[2, 3] = 0
        paragraphs, image = identify_paragraphs_in_image(image)
        self.assertEqual(2, paragraphs)

    def test_have_three_paragraphs(self):
        image = np.ones((5, 5), np.uint8)
        image = image * 255
        image[0, 2] = 0
        image[2, 3] = 0
        image[4, 4] = 0
        paragraphs, image = identify_paragraphs_in_image(image)
        self.assertEqual(3, paragraphs)

if __name__ == '__main__':
    unittest.main()
