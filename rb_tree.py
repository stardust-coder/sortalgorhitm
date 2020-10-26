class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def tree_minimum(self, node):
        while(node.left != None):
            node = node.left
        return node

    def tree_maximum(self, node):
        while node.right != None:
            node = node.right
        return node

    def tree_insert(self,data):
        z = Node(data)
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key<x.key:
                x = x.left
            else:
                x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key<y.key:
            y.left = z
        else:
            y.right = z

    def tree_search(self,node,k):#x:node, k:data
        x = node
        if x == None or k == x.key:
            return x
        elif k < x.key:
            return self.tree_search(x.left,k)
        else:
            return self.tree_search(x.right,k)

if __name__ == '__main__':
    bst = BinarySearchTree()
    
