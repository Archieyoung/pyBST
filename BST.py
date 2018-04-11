#!/usr/bin/env python3
"""
python implement of unbananced binary search tree
"""
import collections
import sys

class Node(object):
    #here key is a special structure which support operations(may be overloaded)
    #like lesser than(<), lesser or equal(<=), equal(==), larger than(>)
    #langer or equal(>=) and may cantain satellite datas
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key

class binary_search_tree(object):
    def __init__(self, keys):
        self.root = None
        if isinstance(keys,collections.Iterable):
            for k in keys:
                #print("inserting {}".format(k))
                self.insert(k)
        else:
            raise TypeError("Input for binary_search_tree is not iterable!")

    def insert(self, z):
        #to Node
        z = Node(z)
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z #tree is empty befor insert z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def delete(self, z):
        #find z in the tree
        z = self.query(z)
        if z.left == None:
            #if z don't have left child, than replace z with its right child
            #hold when z also don't have right child
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y

    def query(self, z, *args):
        if len(args) == 0:
            x = self.root
        elif len(args) == 1:
            x = args[0]
        if x == None or z == x.key:
            return x
        if z < x.key:
            return self.query(z, x.left)
        else:
            return self.query(z, x.right)

    def iterative_query(self, z):
        x = self.root
        while x != None and z != x.key:
            if z < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, *args):
        if len(args) == 0:
            x = self.root
        elif len(args) == 1:
            x = args[0]
        while x.left != None:
            x = x.left
        return x

    def maximum(self, *args):
        if len(args) == 0:
            x = self.root
        elif len(args) == 1:
            x = args[0]
        while x.right != None:
            x = x.right
        return x

    def successor(self, x):
        if self.iterative_query(x) == None:
            raise RuntimeError("Failed to found the successor of {0}, because {0} is not in the tree".format(x))
        #find x
        x = self.iterative_query(x)
        if x.right != None:
            return self.minimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if self.iterative_query(x) == None:
            raise RuntimeError("Failed to found the successor of {0}, because {0} is not in the tree".format(x))
        #find x
        x = self.iterative_query(x)
        if x.left != None:
            return self.maximum(x.left)
        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

    def inorder_walk(self, *args):
        if len(args) == 0:
            x = self.root
        elif len(args) == 1:
            x = args[0]
        if x != None:
            self.inorder_walk(x.left)
            print(x.key)
            self.inorder_walk(x.right)

def main():
    test_list = [7,5,10,1,6,8,12]
    test_bst = binary_search_tree(test_list)
    test_bst.inorder_walk()
    test_bst.insert(2)
    test_bst.inorder_walk()
    #test query
    if test_bst.iterative_query(int(sys.argv[1])) != None:
        print("yes we found {}".format(int(sys.argv[1])))
    else:
        print("sorry {} is not found".format(int(sys.argv[1])))
    if test_bst.successor(2):
        print(test_bst.successor(2).key)
    if test_bst.predecessor(2):
        print(test_bst.predecessor(2).key)
    test_bst.delete(2)
    test_bst.inorder_walk()

if __name__ == "__main__":
    main()
