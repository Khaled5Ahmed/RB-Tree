from node import Node

class RBTree:
    def __init__(self):
        self.NIL = Node(None, None)
        self.NIL.color = "black"
        self.NIL.right = self.NIL.left = self.NIL.parent = self.NIL
        self.root = self.NIL


    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def insert(self, key,write_to_file = True):
        if self.search(key) != self.NIL:
            print("ERROR: Word already in the dictionary!")
            return

        newNode = Node(key, self.NIL)
        x = self.root
        y = self.NIL

        while x != self.NIL:
            y = x
            if newNode.key < x.key:
                x = x.left
            else:
                x = x.right

        newNode.parent = y
        if y == self.NIL:
            self.root = newNode
        elif newNode.key < y.key:
            y.left = newNode
        else:
            y.right = newNode

        newNode.left = self.NIL
        newNode.right = self.NIL
        newNode.color = "red"

        self.fix_insert(newNode)


        if write_to_file:
            with open("Dictionary.txt", "a") as file:
                file.write(key + "\n")



    def fix_insert(self, z):
        while z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotate_right(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.rotate_left(z.parent.parent)

        self.root.color = "black"


    def search(self, key):
        return self.search_helper(self.root, key)


    def search_helper(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        elif key < node.key:
            return self.search_helper(node.left, key)
        return self.search_helper(node.right, key)


    def get_tree_height(self, node=None):
        if node is None:
            node = self.root
        if node == self.NIL:
            return -1
        left_size = self.get_size(node.left) if node.left != self.NIL else 0
        right_size = self.get_size(node.right) if node.right != self.NIL else 0
        return 1 + max(left_size, right_size)


    def get_black_height(self, node=None):
        if node is None:
            node = self.root
        height = 0
        node = node.left
        while node != self.NIL:
            if node.color == "black":
                height += 1
            node = node.left
        height += 1     
        return height


    def get_size(self, node=None):
        if(node is None):
            node = self.root 
        if(node == self.NIL):
            return 0
        left_size = self.get_size(node.left) if node.left != self.NIL else 0
        right_size = self.get_size(node.right) if node.right != self.NIL else 0
        return 1 + left_size + right_size



    def load_dictionary(self, filename = "Dictionary.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    word = line.strip()
                    if word:
                        self.insert(word,write_to_file = False)
        except FileNotFoundError:
            print("File not found!")


    def check_word(self, word):
        if self.search(word) != self.NIL:
            print("YES")
        else:
            print("NO")
