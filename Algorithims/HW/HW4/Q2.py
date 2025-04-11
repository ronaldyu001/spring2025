from functions import*


"""
This file contains functions used for Q2. 
Much of this code is taken directly from ChatGPT.
"""


#
#   GENERATE LIST
#
def generate_random_integers(size):
    return [random.randint(0, 1_000_000) for _ in range(size)]


#
#   NODE CLASS FOR SKIPLIST
#
class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)


#
#   SKIPLIST CLASS
#
class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level  # Max levels allowed
        self.p = p  # Probability for level generation
        self.header = self._create_node(-1, max_level)
        self.level = 0  # Current highest level

    def _create_node(self, key, level):
        return Node(key, level)

    def _random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        # Find the position to insert the new node
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        level = self._random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level

        new_node = Node(key, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        return current and current.key == key

    def delete(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    continue
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def display(self):
        print("Skip List:")
        for i in range(self.level + 1):
            level_nodes = []
            node = self.header.forward[i]
            while node:
                level_nodes.append(str(node.key))
                node = node.forward[i]
            print(f"Level {i}: {' -> '.join(level_nodes)}")

    @timeEfficiencyDecorator
    def initialize_from_array(self, arr):
        for key in arr:
            self.insert(key)
    
    @timeEfficiencyDecorator
    def batch_search(self, arr):
        result = {}
        for key in arr:
            result[key] = self.search(key)
        return result
    

#
#   BINARY SEARCH
#
def binary_search( arr, target ):
    # variables
    left, right = 0, len(arr) - 1
    
    # while lower bound is < upper bound
    while left <= right:
        mid = ( left + right ) // 2
        
        # if target found
        if arr[ mid ] == target:
            return True
        
        # if guess is less than target
        elif arr[ mid ] < target:
            left = mid + 1

        # if guess is greater than target
        else:
            right = mid - 1
            
    return False


#
#   BINARY BATCH SORT
#
@timeEfficiencyDecorator
def binary_batch_search( arr1, arr2 ):    
    results = []
    for value in arr2:
        found = binary_search( arr1, value )
        results.append( found )
    
    return results


#
#   SORT
#
@timeEfficiencyDecorator
def sort_array( arr ):
    arr.sort()
    return arr