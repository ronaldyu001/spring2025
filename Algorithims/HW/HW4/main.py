from Q1 import*
from Q2 import*


if __name__ == "__main__":
    # DATA
    testFiles = [ "data/rand1000.txt",\
                  "data/rand10000.txt",\
                  "data/rand100000.txt",\
                  "data/rand250000.txt",\
                  "data/rand500000.txt",\
                  "HW4/data/rand1000000.txt"]


    # MENU
    while True:
        # display main menu
        print( f'\
                            HW4\n\
              0) QUIT\n\
              1) Q1: Merging k Sorted Lists\n\
              2) Q2: Skiplist Performance\n\
              3) Q3: \n\
              4) \n' )
        
        # ask for user input
        user_input = int( input( f'Enter Menu Option: ' ) )


        # MENU OPTIONS
        # 0: Quit
        if user_input == 0:
            break


        # 1: Merging k Sorted Lists
        elif user_input == 1:
            # split into 100 sublists
            sublists = split_list( readFile(testFiles[5]), 100 )

            # use radix/counting sort for first 50 sublists
            radix_sublists = sublists[:50]

            # use bucketsort for second 50 sublists
            bucket_sublists = sublists[50:]
            for i in range( len(bucket_sublists) ):
                bucket_sublists[ i ] = bucket_sort( bucket_sublists[ i ] )

            # merge and sort the sorted sublists
            sorted = merge_and_sort( bucket_sublists, 50 )
            print( sorted )


        # 2: Skiplist Performance
        elif user_input == 2:
            # variables
            repititions = 10
            skip_search_time, binary_search_time = 0, 0
            skip_initialize_time, binary_initialize_time = 0, 0

            # repeate process 10 times
            for i in range( repititions ):
                # create two lists of 1000000 integers
                print( f'\nGenerating Lists' )
                search_in = generate_random_integers( 1000000 )
                search_for = generate_random_integers( 1000000 )

                # initialize skiplist
                print( f'\nInitializing Skip List' )
                my_skip = SkipList( 20, .5 )    # ( max level, prob of moving up a level )
                temp, skip_initialize_duration = my_skip.initialize_from_array( search_in )
                skip_initialize_time += skip_initialize_duration

                # skip list search
                print( f'\nSearching skip list' )
                skip_search_results, skip_search_duration = my_skip.batch_search( search_for )
                skip_search_time += skip_search_duration

                # sort array for binary search
                print( f'\nSorting List for Binary Search' )
                sorted_search_in, binary_initialize_duration = sort_array( search_in )
                binary_initialize_time += binary_initialize_duration

                # binary search
                print( f'\nPerforming Binary Search' )
                binary_search_results, binary_search_duration = binary_batch_search( sorted_search_in, search_for )
                binary_search_time += binary_search_duration

            # get average times
            skip_avg_time = skip_search_time / repititions
            binary_avg_time = binary_search_time / repititions
            skip_avg_init_time = skip_initialize_time / repititions
            binary_avg_init_time = binary_initialize_time / repititions

            # print average times
            print( f'Skip Avg Time: {skip_avg_time}\n\
                    Binary Avg Time: {binary_avg_time}\n\
                    Skip Avg Init Time: {skip_avg_init_time}\n\
                    Binary Avg Init Time: {binary_avg_init_time}')

            # write results to text files
            array_to_text_file( skip_search_results, 'skip_results' )
            array_to_text_file( binary_search_results, 'binary_results' )

            # plot values
            plot_bar_graph( 'Skip List vs Binary Search', 
                            'Average Time (s)', 
                            'Task', 
                            [skip_avg_init_time, binary_avg_init_time, skip_avg_time, binary_avg_time],
                            ['Make Skip List', 'Sort Array', 'Skip List Search', 'Binary Search'])

        # 3:
        elif user_input == 3:
            continue
