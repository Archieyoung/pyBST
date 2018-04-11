#!/usr/bin/env python3
"""
test perfomance of unbananced search tree and red black tree
"""
import BST
import red_black_tree
import time

def main():
    #init test
    a = [i for i in range(10000)]
    #bst init time
    t1 = time.time()
    bst = BST.binary_search_tree(a)
    t2 = time.time()
    print("It takes {:.2f}s for binary_search_tree init".format(t2-t1))
    t1 = time.time()
    rbt = red_black_tree.red_black_tree(a)
    t2 = time.time()
    print("It takes {:.2f}s for red_black_tree init".format(t2-t1))

    #test query
    t1 = time.time()
    if bst.iterative_query(50).key != None:
        print("Founded")
    t2 = time.time()
    print("It takes {:.6f}s for query 5000 in binary_search_tree".format(t2-t1))
    t1 = time.time()
    if rbt.iterative_query(50).key != None:
        print("Founded")
    t2 = time.time()
    print("It takes {:.6f}s for query 5000 in red_black_tree".format(t2-t1))

if __name__ == "__main__":
    main()
