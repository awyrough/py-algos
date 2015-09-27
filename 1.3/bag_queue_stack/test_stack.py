import unittest

from bag_queue_stack import Stack


class TestStack(unittest.TestCase):

    """
    Test Stack implemenation
    """
    def setUp(self):
        self.my_stack = Stack()

    def test_empty_stack(self):
        self.assertTrue(self.my_stack.is_empty())
        self.assertEqual(self.my_stack.size(), 0)

    def test_push_stack(self):
        self.assertTrue(self.my_stack.is_empty())
        self.my_stack.push("1")
        self.assertFalse(self.my_stack.is_empty())
        self.assertEqual(self.my_stack.size(), 1)
        self.my_stack.push("2")
        self.assertEqual(self.my_stack.pop(), "2")

    def test_iterable(self):
        self.my_stack.push("1")
        self.my_stack.push("2")
        self.my_stack.push("3")
        string = ""
        while not self.my_stack.is_empty():
            string += self.my_stack.pop()
        self.assertEqual(string, "321")


if __name__ == "__main__":
    unittest.main()
