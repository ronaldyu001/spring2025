from Q1 import*
from Q2 import*
from Extra_Credit import*



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
              3) Q3: Extra Credit\n\
              4) \n' )
        
        # ask for user input
        user_input = int( input( f'Enter Menu Option: ' ) )


        # MENU OPTIONS
        # 0: Quit
        if user_input == 0:
            break


        #
        # 1: Merging k Sorted Lists
        #
        elif user_input == 1:
            # split into 100 sublists
            sublists = split_list( readFile(testFiles[5]), 100 )

            # use radix/counting sort for first 50 sublists and check if they are sorted
            sorted_flag = True
            radix_sublists = sublists[:50]
            for i in range( len(radix_sublists) ):
                radix_sublists[ i ] = radix_sort( radix_sublists[i] )
                if not sorted( radix_sublists[i] ):
                    sorted_flag = False
            print( f'Radix Sorts Successful: {sorted_flag}' )

            # use bucketsort for second 50 sublists
            sorted_flag = True
            bucket_sublists = sublists[50:]
            for i in range( len(bucket_sublists) ):
                bucket_sublists[ i ] = bucket_sort( bucket_sublists[i] )
                if not sorted( bucket_sublists[i] ):
                    sorted_flag = False
            print( f'Bucket Sorts Successful: {sorted_flag}' )

            # get combined sublists
            combined_sublists = radix_sublists + bucket_sublists

            # merge and sort the sorted sublists using O(logk)
            sorted_flag = True
            sorted_arr, duration = merge_and_sort( combined_sublists, 100 )
            if not sorted( sorted_arr ):
                sorted_flag = False
            print( f'Merge and Sort O(nlogk) Successful: {sorted_flag}' )

            # merge and sort the sorted sublists using O(nk)
            sorted_flag = True
            sorted_arr, duration = merge_and_sort_nk( combined_sublists, 100 )
            if not sorted( sorted_arr ):
                sorted_flag = False
            print( f'Merge and Sort O(nk) Successful: {sorted_flag}' )


        #
        # 2: Skiplist Performance
        #
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
            array_to_text_file( skip_search_results, 'HW4/results/skip_results' )
            array_to_text_file( binary_search_results, 'HW/results/binary_results' )

            # plot values
            plot_bar_graph( 'Skip List vs Binary Search', 
                            'Average Time (s)', 
                            'Task', 
                            [skip_avg_init_time, binary_avg_init_time, skip_avg_time, binary_avg_time],
                            ['Make Skip List', 'Sort Array', 'Skip List Search', 'Binary Search'])


        #
        # 3: Extra Credit
        #
        elif user_input == 3:
            # extract html from website
            url = 'https://catalog.ucdenver.edu/cu-denver/undergraduate/courses-a-z/csci/'
            html = get_html( url ).text

            # get elements with type=div and class=courseblock
            courses = find_elements( html, 'div', 'courseblock' )

            # get COURSE NUMBERS
            course_numbers = extract_text( courses, 'span', 'text col-3 detail-code margin--tiny text--huge' )
            
            # get COURSE NAMES
            course_names = extract_text( courses, 'span', 'text col-8 detail-title margin--tiny text--huge' )

            # get COURSE HOURS
            course_hours = extract_text( courses, 'span', 'text detail-hours_html' )

            # get COURSE BLOCKS with prerequisite information
            course_prereq_blocks = []
            element_type = 'div'
            element_class = 'courseblockextra noindent'
            for course in courses:
                course_prereq_blocks.append( course.find_all(element_type, element_class) )
            
            # get PREREQUISITE INFORMATION from blocks, enter "Not Found" if unavailable
            course_prerequisites = []
            for block in course_prereq_blocks:
                if len( block ) >= 3:
                    course_prerequisites.append( block[2].text )
                else:
                    course_prerequisites.append( 'Not Found' )

            # reformat course numbers to remove '-' at end. (EXP: CSCI 1410 - )
            for i in range( len(course_numbers) ):
                course_numbers[ i ] = course_numbers[ i ][ :-2 ]

            # filter requirements for prerequisite info only
            for i in range( len(course_prerequisites) ):
                if ( 'Prereq' not in course_prerequisites[i] ) and ( 'prereq' not in course_prerequisites[i] ):
                    course_prerequisites[ i ] = 'N/A'

            # filter for prerequisite course numbers only
            # for each course prepreq info
            for i in range( len(course_prerequisites) ):
                # filter for CSCI 1410 or 1410 formats
                text = course_prerequisites[ i ]
                match_list = re.findall( r'(?:[A-Z]{4}|\s)?\s\d{4}', text )
                # if match found and does not have CSCI format, add it
                if match_list:
                    temp = ''
                    for match in match_list:
                        if not re.findall( r'[A-Z]{4}', match ):
                            match = 'CSCI' + match
                        temp += f'{match}    '
                    course_prerequisites[ i ] = temp


            # put course numbers, course names, course credits, and coure prerequisites in text file
            course_info = [ course_numbers, course_names, course_hours, course_prerequisites ]
            arrays_to_text_file( course_info, 'HW4/results/ExtraCreditResults' )

            # convert data to html
            data = pandas.DataFrame( course_info, index=['Course Number', 'Course Name', 'Credits', 'Pre-Requirement(s)'] ).T
            with open( 'HW4/results/CS_courses.html', 'w' ) as f:
                f.write( data.to_html(border=0, justify='left') )

            # create array for each course and each course's prerequisites
            prereqs = []
            for prereq in course_prerequisites:
                prereqs.append( str(prereq).split('    ') )

            for prereq in prereqs:
                # print( prereq )
                continue

            # create array for directed graph
            directed_graph( course_numbers, prereqs )
            
