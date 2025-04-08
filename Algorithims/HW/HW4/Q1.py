from functions import*

"""
This file contains functions used for Q1.
"""
#
#   SPLIT LIST
#
def split_list( arr, num_of_sublists ):
    # variables
    length = len( arr )
    length_of_sublists = length / num_of_sublists
    sublists_container = []
    index = 0
    
    # split arr into sublists
    while index < length:
        sublists_container.append( arr[int(index) : int(index + length_of_sublists)] )
        index += length_of_sublists

    # return container of sublists
    return sublists_container


#
#   RADIX/COUNTING SORT
#
def radix_counting_sort():
    print()


#
#   BUCKET SORT
#
def bucket_sort( arr ):
    # variables
    num_of_buckets = 10
    max_value = max( arr )
    min_value = min( arr )
    bucket_range = (max_value - min_value + 1) / num_of_buckets
    sorted = []

    # create empty buckets
    buckets = [ [] for _ in range(num_of_buckets) ]

    # throw each value in a bucket
    for value in arr:
        # figure out correct bucket for value
        index = int((value - min_value + 1) / bucket_range)

        # edge case: value = max_value
        if index == num_of_buckets:
            index -= 1

        # add value to correct bucket
        buckets[ index ].append( value )

    # sort each bucket using INSERTION SORT
    for bucket in buckets:
        insertion_sort( bucket )

    # merge buckets
    for bucket in buckets:
        for i in range( len(bucket) ):
            sorted.append( bucket[i] )

    return sorted


#
#   INSERTION SORT
#
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


#
#   MERGE AND SORT SORTED SUBLISTS
#
def merge_and_sort( arr, num_of_arrs ):
    # variables
    min_heap = MinHeap( num_of_arrs )
    sorted = []

    for sub_arr in arr:
        min_heap.insert( sub_arr[0] )

    min_heap.build_min_heap()
    print(min_heap.heap)
    print(min_heap.get_min())


#
#   MIN HEAP CLASS
#
class MinHeap():
    # constructor
    def __init__( self, max_size ):
        self.heap = []
        self.max_size = max_size

    # GET parent index
    def get_parent( self, index ):
        return (index - 1) // 2
    
    # GET left child index
    def get_left_child( self, index ):
        return index * 2 + 1

    # GET right child index
    def get_right_child( self, index ):
        return index * 2 + 2
    
    # min heapify
    def min_heapify( self , index ):
        # variables
        smallest = index
        left = self.get_left_child( index )
        right = self.get_right_child( index )

        # if left child is in array and less than parent
        if left < len( self.heap ) and self.heap[ left ] < self.heap[ smallest ]:
            smallest = left

        # if right child is in array and less than parent
        if right < len( self.heap ) and self.heap[ right ] < self.heap[ smallest ]:
            smallest = right

        # if index was not the smallest, swap with smallest
        # and heapify for value swapped
        if smallest != index:
            self.heap[ smallest ], self.heap[ index ] = self.heap[ index ], self.heap[ smallest ]
            self.min_heapify( smallest )

    # build min heap
    def build_min_heap( self ):
        for i in range( len(self.heap) // 2 - 1, -1, -1 ):
            self.min_heapify( i )

    # get min (root)
    def get_min( self ):
        # if heap is empty, return None
        if not self.heap:
            return None
        
        # swap root (smallest value) and last element
        self.heap[ 0 ], self.heap[ -1 ] = self.heap[ -1 ], self.heap[ 0 ]

        # return the last element (smallest value)
        return self.heap.pop()


    # add element to end of heap
    def insert( self, value ):
        # if heap is already at max size, throw error
        if len( self.heap ) == self.max_size:
            print( 'ERROR: Min Heap is already at max size.' )
            return

        # append value to end of min heap
        self.heap.append( value )