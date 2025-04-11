# Q1) Merging *k **sorted* lists into one sorted list (25 points)**

## Psuedocode

In order to merge k sorted lists into one sorted list:

- Initialize new empty sorted list, "sorted"
- Place smallest element of each k sorted lists into a min-heap
- Move top element (smallest) of min-heap to "sorted"
- Replace the element moved to "sorted" with the next value from the k sorted list it was taken from
- Repeat this for each n elements

## Asymptotic Analysis

This meets **O(n log k)** because:

- Inserting an element into a min-heap with height of log k is O(log k)
- Taking the top element from min-heap is O(1)
- A new element is inserted and popped for each of n elements, so total time is O( n(log k + 1) ), which is O(n log k)

## Implementation

### Split 1,000,000 integers into 100 groups of 10,000 integers

- Divide original[ 0 : 999,999 ] into sub-lists so that: sub_list_1[ 0 : 9999 ] ... sub_list_100[ 990,000 : 999,999 ] are generated.

### Sort 50 groups with Radix + Counting Sort

- Sort 50 of the sublists using Radix Sort, with counting sort as the underlying sort for each digit.
- Results in 50 of the 100 sorted sub-lists to merge.

### Sort 50 groups with Bucket sort

- Sort 50 of the sublists uing Bucket sort.
- Results in 50 of the 100 sorted sub-lists to merge.

### Merge 100 groups

- Merge the 100 sorted sub-lists into one sorted list, "sorted", using the algorithm described in the Psuedocode section.

## Discussion: O(n log k) vs O(n k)

# Q2) Use AI to compare Skip List Search vs Binary Search

# Q3) Answer the following BST questions

## a) Assign keys to a blank, predetermined BST structure

![1744316956174](image/README/1744316956174.png)

## b) Describe an algorithm to fill a BST

In order to systematically insert keys into a BST to match a predetermined structure, the BST properties can be used.

1. Sort the keys into ascending order.
2. Do an in-order traversal of the tree (left, root, right).
3. Insert each of the sorted keys at each node.

This works because in-order traversal reads the nodes in ascending order, which matches the sorted keys.

## c) Describe an algorithm to generate key order for a BST

In order to generate a key order for a BST to match a predetermined structure, properties used from Part b can be used.

1. Sort the keys into ascending order.
2. Do an in-order traversal of the BST (left, root, right).
3. Map the keys to the node order resulting from the in-order traversal.
   1. For example, a resulting 2x2 array could look like this: [ [key1, node2], [key2, node 1], [key3, node 3] ].
4. Do a level-order traversal of the BST, replacing the node with its mapped key.
   1. The resulting list of keys will be in the correct order.

This works because by mapping the sorted keys to the in-order traversal, each key is correctly assigned to its corresponding node. The level-order traversal gives the nodes in order of insertion. By replacing each of the nodes in the level-order traversal with it's corresponding key, a list of keys with correct insertion order is generated.

## d) Describe why the given BST can't be colored to form a RB Tree

Given the empty BST structure, it is impossible to be converted to a RB Tree due to one of the subtrees on the left side of the BST. More specifically, Node 4 has 3 consecutive right descendants. This produces the largest depth of 6, and has a minimum black-height of 4. This is problematic, as there are other paths from the root that have a maximum black-height of 3. This conflict makes it impossible to satisfy the black-height rule for the given BST.

## e) Describe rotations and Show final RB Tree

Right Rotation:

- Use Case
  - When the left side of the subtree's height exceeds the right side's by more than 1.
  - Also known as LL imbalance, because the imbalance is due to the node to the left of the node to the left of the subtree's root.
- Action
  - Rotate the subtree one node to the right so that the difference in height does not exceed 1.

Left Rotation:

- Use Case
  - When the left side of the subtree's height exceeds the right side's by more than 1.
  - Also known as RR imbalance, because the imbalance is due to the node to the right of the node to the right of the subtree's root.
- Action
  - Rotate the subtree one node to the left so that the difference in height does not exceed 1.

Right-Left Rotation:

- Use Case
  - When the imbalance is due to the node to the left of the node to the right of the subtree's root.
- Action:
  - Rotate the subtree to the right of the subtree's root to the right by one node.
  - Rotate the root's subtree to the left by one node.

Left-Right Rotation:

- Use Case
  - When the imbalance occurs to the right of the node to the left of the subtree's root.
- Action:
  - Rotate the subtree to the left of the subtree's root to the left by one.
  - Rotate the root's subtree to the right by one node.


To convert the BST to a RB Tree, two rotations will be needed.

Initial BST:

![1744389678168](image/README/1744389678168.png)
