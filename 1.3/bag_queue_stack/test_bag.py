import unittest

from bag_queue_stack import Bag


class TestBag(unittest.TestCase):

    """
    Test Bag implemenation
    """
    def setUp(self):
        self.my_bag = Bag()

    def test_empty_bag(self):
        self.assertTrue(self.my_bag.is_empty())
        self.assertEqual(self.my_bag.size(), 0)

    def test_add(self):
        self.assertTrue(self.my_bag.is_empty())
        self.my_bag.add("1")
        self.assertFalse(self.my_bag.is_empty())
        self.assertEqual(self.my_bag.size(), 1)

    def test_iterable(self):
        self.my_bag.add("1")
        self.my_bag.add("2")
        self.my_bag.add("3")
        counter = 0
        for item in self.my_bag:
            counter += 1
        self.assertEqual(counter, self.my_bag.size())

if __name__ == "__main__":
    unittest.main()
