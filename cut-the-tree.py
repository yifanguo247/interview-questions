'''
https://www.hackerrank.com/challenges/cut-the-tree/problem

There is an undirected tree where each vertex is numbered from  to , and each contains a data value. The sum of a tree is the sum of all its nodes' data values. If an edge is cut, two smaller trees are formed. The difference between two trees is the absolute value of the difference in their sums.

Given a tree, determine which edge to cut so that the resulting trees have a minimal difference between them, then return that difference.

Example


In this case, node numbers match their weights for convenience. The graph is shown below.

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#


def cutTheTree(data, edges):
    # Write your code here
    # build a map of the tree
    seen_nodes = { 1 }
    hierarchy = [ 1 ]
    tree_map = {}
    NUM_VERTICES = len(data)
    for i in range(1, NUM_VERTICES + 1):
        tree_map[i] = []
    for edge in edges:
        node_1 = edge[0]
        node_2 = edge[1]
        if node_1 in seen_nodes:
            parent = node_1
            child = node_2
        elif node_2 in seen_nodes:
            parent = node_2
            child = node_1
        else: # neither vertex has been seen yet, move edge to the end of edges
            edges.append(edge)
            continue
        seen_nodes.add(child)
        hierarchy = [child] + hierarchy # order the children first
        tree_map[parent].append(child)
        
    print(hierarchy)
    TOTAL_SUM = sum(data) # total amount of flow in the tree
    
    flow = {} # sum of the flow of the node and its children
    for node in hierarchy:
        data_idx = node - 1
        children = tree_map[node]
        print(children)
        if children == []: # leaf node
            flow[node] = data[data_idx]
        elif len(children) == 1: # one child node
            flow[node] = data[data_idx] + flow[children[0]]
        else: # two child nodes
            flow[node] = data[data_idx] + flow[children[0]] + flow[children[1]]
            
    # find the minimum difference in two trees
    min_diff = 999999999999999
    for parent, children in tree_map.items():
        # cut the edge between parent and child
        for child in children:
            child_tree =  flow[child]
            parent_tree = TOTAL_SUM - child_tree
            min_diff = min(min_diff, abs(parent_tree - child_tree))
    
    return min_diff
            
        


if __name__ == '__main__':
    fptr = open(os.environ['cut-the-tree.txt'], 'r')

    fptr.read()
    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    print("result: {}".format(result))

    # fptr.write(str(result) + '\n')

    # fptr.close()
