from functions import*
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
            # split into sublists
            sublists = split_list( readFile(testFiles[5]), 100 )

            # use radix/counting sort for first 50 sublists


            # use bucketsort for second 50 sublists
            bucket_sublists = sublists[50::]
            for arr in bucket_sublists:
                print(bucket_sort( arr ))


        # 2: Skiplist Performance
        elif user_input == 2:
            continue

        # 3:
        elif user_input == 3:
            continue
