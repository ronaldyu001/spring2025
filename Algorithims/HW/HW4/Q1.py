from functions import*

"""
This file contains functions used for Q1.
"""

# SPLIT LIST
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


# RADIX/COUNTING SORT
def radix_counting_sort():
    print()


# BUCKET SORT
def bucket_sort( arr ):
    # variables
    num_of_buckets = 10
    max_value = max( arr )
    min_value = min( arr )
    bucket_range = (max_value - min_value + 1) / num_of_buckets
    buckets = [ [] for _ in range(num_of_buckets) ]

    # throw each value in a bucket
    for value in arr:
        index = int((value - min_value + 1) / bucket_range)

        # if max value, make sure it is placed in last bucket
        if index == num_of_buckets:
            index -= 1

        buckets[ index ].append( value )

    # sort each bucket using INSERTION SORT
    for bucket in buckets:
        insertion_sort( bucket )
        print( bucket )


# INSERTION SORT
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