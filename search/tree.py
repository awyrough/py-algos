class BST():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert_left(self, key):
        if not self.left:
            self.left = BST(key)
        else:
            new = BST(key)
            new.left = self.left
            self.left = new

    def insert_right(self, key):
        if not self.right:
            self.right = BST(key)
        else:
            new = BST(key)
            new.right = self.right
            self.right = new

    def get_val(self):
        return self.key

    def set_val(self, key):
        self.key = key
