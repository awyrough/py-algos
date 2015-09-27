class JavaPythonIterator():

    """
    Generic functions for adapter to list objects
    """

    def is_empty(self):
        return len(self.underlying_list) == 0

    def size(self):
        return len(self.underlying_list)

    def __iter__(self):
        return self.underlying_list.__iter__()


class Bag(JavaPythonIterator):

    """
    Implements Bag collection
    """

    def __init__(self):
        self.underlying_list = list()

    def add(self, item):
        self.underlying_list.append(item)


class Queue(JavaPythonIterator):

    """
    Implements a FIFO Queue
    """

    def __init__(self):
        self.underlying_list = list()

    def enqueue(self, item):
        self.underlying_list.append(item)

    def dequeue(self):
        item = self.underlying_list[0]
        self.underlying_list = self.underlying_list[1:]
        return item

    def is_empty(self):
        return len(self.underlying_list) == 0

    def __iter__(self):
        return self.underlying_list.__iter__()


class Stack(JavaPythonIterator):

    """
    Implements a LIFO Stack
    """

    def __init__(self):
        self.underlying_list = list()

    def push(self, item):
        self.underlying_list.append(item)

    def pop(self):
        item = self.underlying_list[len(self.underlying_list) - 1]
        self.underlying_list = self.underlying_list[:len(self.underlying_list) - 1]
        return item
