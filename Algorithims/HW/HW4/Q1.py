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
#   RADIX SORT
#
def radix_sort( arr ):
    # variables
    max_value = max( arr )
    digit = 1

    # if array empty print error
    if not arr:
        print( 'array is empty.' )
        return arr
    
    # process each digit from least to most significant
    while max_value // digit > 0:
        counting_sort( arr, digit )
        digit *= 10

    return arr


#
#   COUNTING SORT
#
def counting_sort( arr, digit ):
    # variables
    length = len( arr )
    counts = [0] * 10
    output = [0] * length

    # count frequency of each number
    for number in arr:
        index = ( number // digit ) % 10
        counts[ index ] += 1

    # get cumalative count
    for i in range( 1, 10 ):
        counts[ i ] = counts[ i - 1 ]

    # make output array
    for i in range( length - 1, -1, -1 ):
        index = ( arr[i] // digit ) % 10
        output[ counts[index] - 1 ] = arr[ i ]
        counts[ index ] -= 1

    # copy output array to arr
    for i in range( length ):
        arr[ i ] = output[ i ]


#
#   BUCKET SORT
#
def bucket_sort( arr ):
    # variables
    num_of_buckets = 50
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
#   MERGE AND SORT O(nlogk)
#
@timeEfficiencyDecorator
def merge_and_sort( arr, num_of_arrs ):
    # variables
    min_heap = MinHeap( num_of_arrs )
    sorted = []

    # initialize min heap
    for i in range( len(arr) ):
        min_heap.insert( arr[ i ][ 0 ], i, 0 )

    # while min heap is not empty
    while len( min_heap.heap ) > 0:
        # get smallest info from min heap
        value, parent, parent_index = min_heap.get_min()
        sorted.append( value )

        # if the parent of smallest is not empty
        if parent_index + 1 < len( arr[parent] ):
            min_heap.insert( arr[parent][parent_index + 1], parent, parent_index + 1 )

    return sorted


#
#   MIN HEAP CLASS
#
class MinHeap():
    # constructor
    def __init__( self, max_size ):
        self.heap = []  # [ value, parent, parent index ]
        self.max_size = max_size

    # get parent index
    def get_parent( self, index ):
        return (index - 1) // 2
    
    # get left child index
    def get_left_child( self, index ):
        return index * 2 + 1

    # get right child index
    def get_right_child( self, index ):
        return index * 2 + 2
    
    # add element to end of heap
    def insert( self, value, parent, parent_index ):
        # if heap is already at max size, throw error
        if len( self.heap ) == self.max_size:
            print( 'ERROR: Min Heap is already at max size.' )
            return

        # append value to end of min heap
        self.heap.append( tuple([value, parent, parent_index]) )

        # heapify up from inserted element
        self.bubble_up( len(self.heap) - 1 )
    
    # min heapify
    def min_heapify( self, index ):
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

    # bubble up
    def bubble_up( self, index ):
        # variables
        parent = (index - 1) // 2

        # bubble up from index
        if index > 0 and self.heap[ index ][ 0 ] < self.heap[ parent ][ 0 ]:
            self.heap[ index ], self.heap[ parent ] = self.heap[ parent ], self.heap[ index ]
            self.bubble_up( parent )

    # get min (root)
    def get_min( self ):
        # if heap is empty, return None
        if len( self.heap ) == 0:
            return None
        
        # swap root (smallest value) and last element
        self.heap[ 0 ], self.heap[ -1 ] = self.heap[ -1 ], self.heap[ 0 ]

        # return the smallest element and min heapify root
        min_value = self.heap.pop()
        self.min_heapify( 0 )
        return min_value


#
#   MERGE AND SORT O(nk)
#
@timeEfficiencyDecorator
def merge_and_sort_nk( arr, num_of_arrs ):
    # variables
    sorted = []
    index_tracker = [1] * len(arr)

    # merge and sort
    while True:
        # variables
        min_value = float('inf')
        min_index = -1

        for i in range( len(arr) ):
            if index_tracker[ i ] < len( arr[i] ):
                if arr[ i ][ index_tracker[i] ] < min_value:
                    min_value = arr[ i ][ index_tracker[i] ]
                    min_index = i

        if min_index == -1:
            break

        sorted.append( min_value )
        index_tracker[ min_index ] += 1

    return sorted