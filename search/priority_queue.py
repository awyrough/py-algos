class BinaryHeap:

    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def build_heap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self._sink(i)
            i = i - 1

    def _swim(self, i=None):
        """
        Swim the ith element in the heap to restore order
        """
        if not i:
            i = self.currentSize
        while i // 2 > 0:
            # swim up if necessary
            # if current value is less than parent value
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def _min_child(self, i):
        """
        Return the smaller child of the ith element.

        Elements are in 2*i, 2*i+1
        """
        if 2 * i + 1 > self.currentSize:
            return 2 * i
        left_child = self.heaplist[2 * i]
        right_child = self.heaplist[2 * i + 1]
        if left_child <= right_child:
            return 2 * i
        else:
            return 2 * i + 1

    def _sink(self, i=None):
        """
        Sink the ith element until order is restored.
        """
        if not i:
            i = 1
        while (i * 2) < self.currentSize:
            min_child_index = self._min_child(i)
            if self.heaplist[i] > self.heaplist[min_child_index]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[min_child_index]
                self.heaplist[min_child_index] = tmp
            i = min_child_index

    def insert(self, key):
        """
        Insert key into binary heap.
        """
        # add it to bottom
        self.heaplist.append(key)
        self.currentSize += 1

        # swim up
        self._swim(i=self.currentSize)

    def deleteMin(self):
        """
        Return and delete min. Then reorder by taking the last value at the root, then sinking
        until order is restored.
        """
        if self.currentSize == 0:
            raise ValueError("Bin heap is empty")
        current_min = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.heaplist.pop()
        self.currentSize -= 1

        self._sink(i=1)

        return current_min

my_binheap = BinaryHeap()
my_binheap.build_heap([6, 9, 5, 3, 2])
print(my_binheap.heaplist)
my_binheap.deleteMin()
print(my_binheap.heaplist)
my_binheap.deleteMin()
print(my_binheap.heaplist)
my_binheap.deleteMin()
print(my_binheap.heaplist)
my_binheap.deleteMin()
print(my_binheap.heaplist)
my_binheap.deleteMin()
print(my_binheap.heaplist)
my_binheap.deleteMin()
print(my_binheap.heaplist)
