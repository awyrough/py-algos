from node import Node


class LinkedList(object):

    def __init__(self, first=None):
        self.first = first  # point to first
        self.last = first   # pointer to last

    def insert_front(self, node):
        if not self.first or not self.last:
            self.first = node
            self.last = self.first
        else:
            node.next = self.first
            self.first = node

    def insert_back(self, node):
        if not self.first or not self.last:
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            self.last = node

    def remove_front(self):
        self.first = self.first.next


class LinkedListWithGenerator(LinkedList):

    def traverse(self):
        current = self.first
        while current:
            yield current
            current = current.next


class LinkedListIterator(object):

    def __init__(self, current):
        self.__current = current

    def next(self):
        if not self.__current:
            raise StopIteration
        else:
            node = self.__current
            self.__current = self.__current.next
            return node


class LinkedListWithIter(LinkedList):

    def __iter__(self):
        return LinkedListIterator(self.first)


def main():
    ll = LinkedListWithGenerator()

    ll.insert_front(Node("1"))
    ll.insert_front(Node("0"))
    ll.insert_front(Node("-1"))
    ll.insert_front(Node("-2"))
    ll.remove_front()

    print("---------GENERATOR OUTPUT-----------")
    generator = ll.traverse()
    for node in generator:
        print(node)

    ll = LinkedListWithIter()

    ll.insert_front(Node("1"))
    ll.insert_front(Node("0"))
    ll.insert_front(Node("-1"))
    ll.insert_front(Node("-2"))
    ll.remove_front()

    print("---------ITERATOR OUTPUT------------")
    for node in ll:
        print(node)


if __name__ == "__main__":
    main()
