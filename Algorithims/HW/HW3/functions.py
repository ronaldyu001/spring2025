import time
import random
import matplotlib
import matplotlib.pyplot

#--------------------
#   PREVIOUSLY USED
#--------------------
# time efficiency decorator
def timeEfficiencyDecorator( func ):
    def wrapper( *args, **kwargs ):
        # get start time before inner function
        startTime = time.time()
        print( f'Start Time: { startTime }' )

        # inner function
        func( *args, **kwargs )

        # get end time and calculate duration after inner function
        endTime = time.time()
        print( f'End Time: { endTime }' )
        duration = endTime - startTime
        print( f'Duration: { duration }' )
        return duration
    return wrapper


# read file into list
def readFile( file ):
    # extract numbers from file into list
    with open( file, 'r' ) as file:
        array = [ int( num ) for line in file for num in line.split() ]
        return array


# plot
def plot(x, y, title, color):
    # graph will open in separate window
    # fig = matplotlib.pyplot.figure()
    
    # plot
    matplotlib.pyplot.plot(x, y, marker='o', linestyle='-', color=color, label='Line Plot')

    # Add text labels for each point
    for i in range(len(x)):
        matplotlib.pyplot.text(x[i], y[i], f'{y[i]})', fontsize=10, ha='right')

    # axis labels and title
    matplotlib.pyplot.xlabel('k')
    matplotlib.pyplot.ylabel('Execution Time (s)')
    matplotlib.pyplot.title(title)

    # show both graphs at the same time
    matplotlib.pyplot.show(block=False)

#--------------------
#   QUESTION 1.1
#--------------------
# max heapfiy (iterable)
def maxHeapify_iterable( array, index ):
    # keep running until heap property is restored
    while True:
        # variables
        parent = index
        largest = parent    # assume parent is the largest
        left_child = index * 2 + 1
        right_child = index * 2 + 2

        # if left child exists and greater than largest, it is now largest
        if left_child < len( array ) and array[ left_child ] > array[ largest ]:
            largest = left_child

        # if right child exists and is greater than largest, it is now largest
        if right_child < len( array ) and array[ right_child ] > array[ largest ]:
            largest = right_child

        # if parent is already largest, break
        if parent == largest:
            break

        # swap parent and largest
        array[ parent ], array[ largest ] = array[ largest ], array[ parent ]

        # move down heap
        index = largest


# build max heap
@timeEfficiencyDecorator
def build_max_heap_iterable( array ):
    n = len( array )
    # Start from the last non-leaf node and heapify each node
    for i in range( n // 2 - 1, -1, -1 ):
        maxHeapify_iterable( array , i)


# verify max heap (checks if build max heap works)
def verify_max_heap( array ):
    n = len( array )
    for i in range( n // 2 ):  # Only need to check the non-leaf nodes
        left = 2 * i + 1
        right = 2 * i + 2
        # Check if the current node is greater than or equal to both children
        if left < n and array[ i ] < array[ left ]:
            print( f'{ i  }: { array[ left ] } greater than { array[ i ] } ')
            return False
        if right < n and array[ i ] < array[ right ]:
            print(f'{ i }: { array[ right ] } greater than { array [ i ] }')
            return False
    return True


# max heapify (recursive)
def max_heapify_recursive(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1  # for termination condition \
    largest = i
    if left <= length and array[i] < array[left]:
        largest = left
    if right <= length and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify_recursive(array, largest)   # largest == new i


# build max heapify recursive
@timeEfficiencyDecorator
def build_max_heap_recursive( array ):
    n = len( array )
    # Start from the last non-leaf node and heapify each node
    for i in range( n // 2 - 1, -1, -1 ):
        max_heapify_recursive( array , i)


# write array to file
def write_array_to_file( array, filename ):
    # Open the file in write mode
    with open( filename, 'w' ) as file:
        # Write each element of the array on a new line
        for element in array:
            file.write( str( element ) + '\n' )

#--------------------
#   QUESTION 3.2
#--------------------
# quick sort partion
def quicksort_partition( array, low, high ):
    # randomly choose pivot and move to right end of array
    pivot = random.randint( low, high )
    array[ pivot ], array[ high ] = array[ high ], array[ pivot ]
    pivot = array[ high ]

    # index to track where to move numbers smaller than pivot
    i = low - 1

    # go through list. if element j smaller than pivot, increment i and swap with array[ i ]
    for j in range( low, high ):
        if array[ j ] <= pivot:
            i += 1
            array[ i ], array[ j ] = array[ j ], array[ i ]

    # place pivot between smaller (left) and larger elements (right)
    array[ i + 1 ], array[ high ] = array[ high ], array[ i + 1 ]

    # return pivot index
    return i + 1


# quick sort
def quicksort( array, low, high ):
    if low < high:
        # find pivot and place between smaller and larger elements
        pivot = quicksort_partition( array, low, high )
        # sort elements left of pivot
        quicksort( array, low, pivot - 1 )
        # sort elements right of pivot
        quicksort( array, pivot + 1, high)


# optimized bubble sort
def bubblesort_optimized( array ):
    # 
    array_size = len( array ) - 1
 
    # iterate 'number of elements in array' times
    for i in range( array_size ):
        swapped = False

        # for each element in array, not including those already sorted
        for j in range( array_size - i ):

            # if the element is larger than the next, swap
            if array[ j ] > array[ j + 1 ]:
                array[ j ], array[ j + 1 ] = array[ j + 1 ], array[ j ]
                swapped = True

        # if no swap, largest element sorted for this iteration, stop early and go to next iteration
        if not swapped:
            break


# verify sorted array
def is_sorted( array ):
    for i in range( len( array ) - 1):
        if array[ i ] > array[ i + 1 ]:
            return False
    return True 


# hybrid sort (optimizing bubble sort and quicksort)
@timeEfficiencyDecorator
def hybridsort( array, low, high, k ):
    # 
    if low < high:
        # 
        if high - low + 1 < k:
            bubblesort_optimized( array )

        # 
        else:
            pivot = quicksort_partition( array, low, high )
            quicksort( array, low, pivot - 1)
            quicksort( array, pivot + 1, high )