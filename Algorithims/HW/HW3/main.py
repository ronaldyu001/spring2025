import functions
from functions import*

if __name__ == "__main__":
    # data sets provided
    testFiles = ["data/rand1000.txt",\
                 "data/rand10000.txt",\
                 "data/rand100000.txt",\
                 "data/rand250000.txt",\
                 "data/rand500000.txt",\
                 "data/rand1000000.txt"]


    while True:
        # display main menu
        print(f'\
                            HW3\n\
              0) QUIT\n\
              1) Q1.1: Max Heapify (iterative)\n\
              2) Q3.2.a: Quicksort, Optimizing Bubble Sort\n\
              3) Q3.2.b: Hybrid Sort, Data Visualization\n\
              4) \n')
        
        # ask for user input
        user_input = int(input(f'Enter Menu Option: '))


        # option 0
        if user_input == 0:
            break


        # option 1
        elif user_input == 1:
            # read input file into an array
            array_1 = readFile( testFiles[ 5 ] )
            array_2 = array_1

            # build max heap iterable
            build_max_heap( array_1 )
            write_array_to_file( array_1, 'output_1' )
            print( f'Heapified: { verify_max_heap( array_1 ) }' )

            # build max heap recursive
            build_max_heap_recursive( array_2 )
            write_array_to_file( array_2, 'output_2')
            print( f'Heapified: { verify_max_heap( array_2 ) }' )


        # option 2
        elif user_input == 2:
            # read input file into an array
            array_1 = readFile( testFiles[ 0 ] )
            array_2 = array_1

            # quicksort
            print( f'\nQUICKSORT: ' )
            quicksort( array_1, 0, len( array_1 ) - 1 )
            # write_array_to_file( array_1, 'output_1')
            print( f'Sorted: { is_sorted( array_1 ) }' )

            # optimized bubble sort
            print( f'\nOPTIMIZED BUBBLE SORT: ' )
            bubblesort_optimized( array_2 )
            # write_array_to_file( array_2, 'output_2' )
            print( f'Sorted: { is_sorted( array_2 ) }' )


        # option 3
        elif user_input == 3:
            # array to store average durations for varying ks
            data = []

            # iterate through each k (2 - 20)
            for k in range( 2, 200, 30 ):
                duration = 0
                # run each k 10 times and get the average time
                for i in range(3):
                    # read data into array
                    array_3 = readFile( testFiles[ 5 ])
                    duration += hybridsort( array_3, 0, len( array_3 ) - 1, k)
                    # write_array_to_file( array_2, 'output_3' )
                    # print( f'Sorted: { is_sorted( array_3 ) }' )

                # add each average k time to data
                data.append( duration / 3 )

            # display graph
            plot( [ int for int in range( 2, 200, 30 ) ], data, 'Hybrid Sort: k vs time', 'r' )
            