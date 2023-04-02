'''
You are inside question view of Question 2

Question 2
A sewer drainage system is structured as a tree. Water enters the system at n nodes numbered from 0 to n-1 and flows through the tree to the root, which has the number 0. The tree structure is defined by an array parent, where parent[i] = j means that water flows from node i to its direct parent node j. Water exits the system after it flows through the root, so the root has no parent, represented as parent[0] = -1. The value in input[i] denotes the amount of water that enters the sewer system at node i. This excludes water that flows into i from its children. The total flow through a node is thus the flow that enters at that node, plus the sum of the total flows of all of its children.
 
Your task is to divide the system into two smaller pieces by cutting one branch so that the total flows of the resulting subtrees are as close as possible.
 
Example
parent = [-1, 0, 0, 1, 1, 2]
input = [1, 2, 2, 1, 1, 1] 
 
The structure of the system is shown in the diagram below. The nodes are labeled as <node number>/<input flow>.
 
Cut the branch between nodes 1 and 0.
The partition {0, 2, 5} has total flow input[0] + input[2] + input[5] = 1 + 2 + 1 = 4.
The partition {1, 3, 4} has total flow input[1] + input[3] + input[4] = 2 + 1 + 1 = 4.
The absolute difference between the total flows of the two new sewer systems is 4 - 4 = 0.
It's not possible for a different division to achieve a smaller difference than 0, so the final answer is 0.

 
Function Description 
Complete the function drainagePartition in the editor below.
 
The function has the following parameter(s):
    int parent[n]: each parent[i] is the parent node of node i
    int input[n]: each input[i] is the direct flow into the system at node i
 
Returns
    int: the minimum (positive) difference in total flow between the two new sewer systems
 
Constraints
* 2 ≤ n ≤ 105
* 1 ≤ input[i] ≤ 104
* parent[0] = -1
* parent[i] < i for 1 ≤ i < n
* The depth of the tree is at most 500.
 
Input Format Format for Custom Testing






Sample Case 0
Sample Input
STDIN     Function 
-----     -------- 
4     →   parent[] size n = 4
-1    →   parent[] = [ -1, 0, 1, 2 ]
0
1
2
4     →   input[] size n = 4
1     →   input[] = [ 1, 4, 3, 4 ]
4
3
4
Sample Output
2
 
Explanation
 
The structure of the system is shown in the diagram below.

The optimal value of 2 is achieved by cutting between nodes 1 and 2. The resulting subtrees {0, 1} with total flow 1 + 4 = 5 and {2, 3} with total flow 3 + 4 = 7 differ by |5 - 7| = 2.
 

To run, do python3 sewer.py



'''





#!/bin/python3

#
# Complete the 'drainagePartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY inputs
#

def drainagePartition(parent, inputs):
    # Write your code here

    # build a map of the tree
    seen_nodes = { 0 }
    hierarchy = [ 0 ]
    tree_map = {}
    NUM_VERTICES = len(parent)
    for i in range(NUM_VERTICES):
        tree_map[i] = []
    for child, parent in enumerate(parent):
        if parent == -1: # is root
            continue
        seen_nodes.add(child)
        hierarchy = [child] + hierarchy # order the children first
        tree_map[parent].append(child)
        
    TOTAL_SUM = sum(inputs) # total amount of flow in the tree
    
    flow = {} # sum of the flow of the node and its children
    for node in hierarchy:
        children = tree_map[node]
        if children == []: # leaf node
            flow[node] = inputs[node]
        elif len(children) == 1: # one child node
            flow[node] = inputs[node] + flow[children[0]]
        else: # two child nodes
            flow[node] = inputs[node] + flow[children[0]] + flow[children[1]]
            
    for parent, children in tree_map.items():
        print("parent: {}, children: {}".format(parent, children))

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
    
    # parent  = [[int(x) for x in input().split()] for _ in range(int(input()))]
    parent = [-1, 0, 0, 1, 1, 2]

    # inputs = list(map(int, input().rstrip().split()))
    inputs = [1, 2, 2, 1, 1, 1]

    result = drainagePartition(parent, inputs)

    print("min difference in flow: {}".format(result))
