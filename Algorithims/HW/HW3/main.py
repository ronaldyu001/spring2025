import functions
from functions import*

if __name__ == "__main__":
    # data sets provided
    testFiles = [ "./data/rand1000.txt",\
                  "./data/rand10000.txt",\
                  "./data/rand100000.txt",\
                  "./data/rand250000.txt",\
                  "./data/rand500000.txt",\
                  "./data/rand1000000.txt",\
                  "./data/random_integers_10M.txt"\
                ]


    while True:
        # display main menu
        print( f'\
                            HW3\n\
              0) QUIT\n\
              1) Q1.1: Max Heapify\n\
              2) Q3.2.a: Quicksort, Optimizing Bubble Sort\n\
              3) Q3.2.b: Hybrid Sort, Data Visualization\n\
              4) \n' )
        
        # ask for user input
        user_input = int( input( f'Enter Menu Option: ' ) )


        # option 0 (exit)
        if user_input == 0:
            break


        # option 1 (Build Max Heap Iterative and Recursive)
        elif user_input == 1:
            # read input file into an array
            array_1 = readFile( testFiles[ 5 ] )
            array_2 = readFile( testFiles[ 5 ] )

            # build max heap iterable
            print( f'ITERABLE' )
            build_max_heap_iterable( array_1 )
            write_array_to_file( array_1, 'output_1' )
            print( f'Heapified: { verify_max_heap( array_1 ) }' )

            # build max heap recursive
            print( f'RECURSIVE' )
            build_max_heap_recursive( array_2 )
            write_array_to_file( array_2, 'output_2')
            print( f'Heapified: { verify_max_heap( array_2 ) }' )


        # option 2 (Quicksort and Optimizing Bubble Sort)
        elif user_input == 2:
            # read input file into an array
            array_1 = readFile( testFiles[ 5 ] )
            array_2 = array_1

            # quicksort
            print( f'\nQUICKSORT: ' )
            start_time = time.time()
            quicksort( array_1, 0, len( array_1 ) - 1 )
            end_time = time.time()
            duration = end_time - start_time
            # write_array_to_file( array_1, 'output_1')
            print( f'Sorted: { is_sorted( array_1 ) }' )
            print( f'Duration: {duration}' )

            # optimized bubble sort
            print( f'\nOPTIMIZED BUBBLE SORT: ' )
            start_time = time.time()
            bubblesort_optimized( array_2 )
            end_time = time.time()
            duration = end_time - start_time
            # write_array_to_file( array_2, 'output_2' )
            print( f'Sorted: { is_sorted( array_2 ) }' )
            print( f'Duration: {duration}' )


        # option 3 (Hybrid Sort and Data Visualization)
        elif user_input == 3:
            # array to store average durations for varying ks
            data = []

            # variables
            k_min = 2
            k_max = 10
            interval = 1
            k_iterations = 10

            # iterate through each k
            for k in range( k_min, k_max, interval ):
                duration = 0
                # run each k 10 times and get the average time
                for i in range( k_iterations ):
                    # print k values
                    print( f'k = { k }' )
                    # read data into array
                    array_3 = readFile( testFiles[ 4 ])
                    duration += hybridsort( array_3, 0, len( array_3 ) - 1, k )
                    # write_array_to_file( array_2, 'output_3' )
                    # print( f'Sorted: { is_sorted( array_3 ) }' )

                # add each average k time to data
                data.append( duration / k_iterations )

            # display graph
            plot( [ int for int in range( k_min, k_max, interval ) ], data, 'Hybrid Sort: k vs time', 'r' )
            