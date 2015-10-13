import unittest

from bag_queue_stack import Queue


class TestQueue(unittest.TestCase):

    """
    Test Stack implemenation
    """
    def setUp(self):
        self.my_queue = Queue()

    def test_empty_stack(self):
        self.assertTrue(self.my_queue.is_empty())
        self.assertEqual(self.my_queue.size(), 0)

    def test_enqueue_stack(self):
        self.assertTrue(self.my_queue.is_empty())
        self.my_queue.enqueue("1")
        self.assertFalse(self.my_queue.is_empty())
        self.assertEqual(self.my_queue.size(), 1)
        self.my_queue.enqueue("2")
        self.assertEqual(self.my_queue.dequeue(), "1")

    def test_iterable(self):
        self.my_queue.enqueue("1")
        self.my_queue.enqueue("2")
        self.my_queue.enqueue("3")
        string = ""
        while not self.my_queue.is_empty():
            string += self.my_queue.dequeue()
        self.assertEqual(string, "123")


if __name__ == "__main__":
    unittest.main()
