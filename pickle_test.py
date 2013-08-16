import unittest
import os
from pickler import list_pickler, unpickler

class PickleTest(unittest.TestCase):

    def setUp(self):
        self.my_list = ['a','b','c','d','e']
        self.file_path = os.path.join('temp.p')

    def test_pickled_then_unpickled_lists_are_equal(self):

        list_pickler(self.file_path, self.my_list)
        another_list = unpickler(self.file_path)
        self.assertEqual(self.my_list,another_list)

    def tearDown(self):
        os.remove(self.file_path)

