#!/usr/bin/env python3
"""
python implement of red black tree
"""
import collections

class Node(object):
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.color = None
        self.key = key

class NIL(object):
    def __init__(self):
        #NIL can be son of leafs in a red black tree
        #NIL can be parent of root in a red black tree
        #But NIL don't know neigther who his parent is nor
        #who his son is
        #What a poor guy!
        self.color = 0 #all NILs are black
        self.key = None

class red_black_tree(object):
    def __init__(self, *args):
        self.nil = NIL()
        self.root = self.nil
        if len(args) == 1:
            if isinstance(args,collections.Iterable):
                for k in args[0]:
                    #print("inserting {}".format(k))
                    self.insert(k)
            else:
                raise TypeError("Input for binary_search_tree is not iterable!")
        else:
            pass

    def insert(self, z):
        #to node
        z = Node(z)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 1 #1 represent red, 0 repesent black
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.parent.color == 1:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self._left_rotate(z)
                else:
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self._right_rotate(z)
                else:
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self._left_rotate(z.parent.parent)
        self.root.color = 0

    def delete(self, z):
        z = self.iterative_query(z)
        if z == self.nil:
            raise RuntimeError("{} is not in the tree".format(z.key))
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self._rb_delete_fixup(x)

    def _rb_delete_fixup(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 0 and w.right.color == 0:
                    w.color = 1
                    x = x.parent
                elif w.right.color == 0:
                    w.left.color = 0
                    w.color = 1
                    self._right_rotate(w)
                    w = x.parent.right
                else:
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.right.color = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == 0 and w.right.color == 0:
                    w.lolor = 1
                    x = x.parent
                elif w.left.color == 0:
                    w.right.color = 0
                    w.color = 1
                    self._left_rotate(w)
                    w = x.parent.left
                else:
                    w.color = x.parent.color
                    x.parent.color  = 0
                    w.left.color = 0
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def _rb_transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def iterative_query(self, z):
        x = self.root
        while x != self.nil and z != x.key:
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
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, *args):
        if len(args) == 0:
            x = self.root
        elif len(args) == 1:
            x = args[0]
        while x.right != self.nil:
            x = x.right
        return x

    def successor(self, x):
        #find x
        x = self.iterative_query(x)
        if x == self.nil:
            raise RuntimeError("Failed to found the successor of {0}, because {0} is not in the tree".format(x))
        if x.right != self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        #find x
        x = self.iterative_query(x)
        if x == self.nil:
            raise RuntimeError("Failed to found the successor of {0}, because {0} is not in the tree".format(x))
        if x.left != self.nil:
            return self.maximum(x.left)
        y = x.parent
        while y != self.nil and x == y.left:
            x = y
            y = y.parent
        return y

    def get_keys(self):
        self.keys = []
        self._inorder_walk()

    def _inorder_walk(self, *args):
        if len(args) == 0:
            x = self.root
        elif len(args) == 1:
            x = args[0]
        if x != self.nil:
            self._inorder_walk(x.left)
            self.keys.append(x.key)
            self._inorder_walk(x.right)

def main():
    test_list = [i for i in range(100)]
    test_bst = red_black_tree(test_list)
    test_bst.get_keys()
    print(test_bst.keys)
    print("test deletion:\n=======")
    for i in range(10,20):
        print("deleting {}".format(i))
        test_bst.delete(i)
    test_bst.get_keys()
    print(test_bst.keys)

if __name__ == "__main__":
    main()

