import unittest
from utils import arrs


class UtilsTest(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, 'test'), 2)
        self.assertEqual(arrs.get([], 0, 'test'), 'test')
        self.assertEqual(arrs.get([2, 1], -2, 'test'), 'test')

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 1, 2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -6, 1), [1])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
