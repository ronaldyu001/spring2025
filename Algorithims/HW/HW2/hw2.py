import hw2_funcs
import webbrowser
import os

if __name__ == "__main__":
    # variables for Q1
    oneSec = 1e6
    oneMin = oneSec*60
    oneHr = oneMin*60
    oneDay = oneHr*24
    oneMonth = oneDay*30
    oneYr = oneDay*365
    oneCen = oneYr*100
    times = [oneSec, oneMin, oneHr, oneDay, oneMonth, oneYr, oneCen]

    # variables for Q2
    testFiles = ["rand1000.txt", "rand10000.txt", "rand100000.txt", "rand250000.txt", "rand500000.txt", "rand1000000.txt"]


    # keep showing menu until user enters "0"
    choice = 1
    while(choice != 0):
        # display menu
        print("\n0. QUIT\n1. Q1\n2. Q2\n")
        # get user choice
        choice = int(input("Enter menu option: "))

        # Q1
        if(choice == 1):
            # ------------- #
            #   log(n)      #
            # ------------- #
            print("log(n):")
            for time in times:
                hw2_funcs.log_n(time)
            print()

            # ------------- #
            #   sqrt(n)     #
            # ------------- #
            print("sqrt(n):")
            for time in times:
                hw2_funcs.sqrt_n(time)
            print()

            # ------------- #
            #   n           #
            # ------------- #
            print("n")
            for time in times:
                hw2_funcs.n(time)    
            print()

            # ------------- #
            #   n*log(n)    #
            # ------------- #
            print("nlog(n)")
            for time in times:
                hw2_funcs.n_log_n(time)
            print()

            # ------------- #
            #   n^2         #
            # ------------- #
            print("n^2")
            for time in times:
                hw2_funcs.n_exp(2, time)  
            print()

            # ------------- #
            #   n^3         #
            # ------------- #
            print("n^3")
            for time in times:
                hw2_funcs.n_exp(3, time)  
            print()

            # ------------- #
            #   2^n         #
            # ------------- #
            print("2^n")
            for time in times:
                hw2_funcs.two_exp_n(time)
            print()

            # ------------- #
            #   n!          #
            # ------------- #
            print("n!")
            for time in times:
                hw2_funcs.n_fact(time)  
            print()

            continue

        # Q2
        elif(choice == 2):
            subChoice = 1
            while(subChoice != 0):
                # display sub menu
                print("\n0. BACK\n1. Insertion Sort\n2. Merge Sort\n3. Plot\n4. Extra Credit\n")
                subChoice = int(input("Enter option: "))

                # go back to main menu
                if(subChoice == 0):
                    break
                
                # insertion sort
                elif(subChoice == 1):
                    subChoice_2 = 1
                    while(subChoice_2 != 0):
                        # ask which test file to run
                        print("\nWhich test file to run?\n\
                            0. BACK\n\
                            1. 1000\n\
                            2. 10000\n\
                            3. 100000\n\
                            4. 250000\n\
                            5. 500000\n\
                            6. 1000000\n\
                            7. All\n")
                        # get user choice
                        subChoice_2 = int(input("Enter choice: "))
                        
                        # BACK
                        if(subChoice_2 == 0):
                            break

                        # all
                        elif(subChoice_2 == 7):
                            for file in testFiles:
                                hw2_funcs.insertionSort(file)
                        
                        # if a single file is selected
                        else:
                            hw2_funcs.insertionSort(testFiles[subChoice_2 - 1])

                # merge sort
                elif(subChoice == 2):
                    subChoice_2 = 1
                    while(subChoice_2 != 0):
                        # ask which test file to run
                        print("\nWhich test file to run?\n\
                            0. BACK\n\
                            1. 1000\n\
                            2. 10000\n\
                            3. 100000\n\
                            4. 250000\n\
                            5. 500000\n\
                            6. 1000000\n\
                            7. All\n")
                        # get user choice
                        subChoice_2 = int(input("Enter choice: "))
                        
                        # BACK
                        if(subChoice_2 == 0):
                            break

                        # all
                        elif(subChoice_2 == 7):
                            for file in testFiles:
                                hw2_funcs.mergeSortContainer(file)
                        
                        # if a single file is selected
                        else:
                            hw2_funcs.mergeSortContainer(testFiles[subChoice_2 - 1])


                elif(subChoice == 3):
                    # insertion sort plot
                    hw2_funcs.plot(['1000', '10,000', '100000', '250000', '500000', '1000000'],
                                    [.01, .43, 42.01, 276.81, 1144.23, 5424.95], 'Insertion Sort')
                    
                    # merge sort plot
                    hw2_funcs.plot(['1000', '10,000', '100000', '250000', '500000', '1000000'],
                                    [.004, .035 ,.149, .321, .688, 1.459], 'Merge Sort')
                    
                elif(subChoice == 4):
                    print("Extra Credit output using html file.")
                    print("hw2ExtraCredit.html must be in same folder as hw2.py in order to open.")
                    # get html relative path, absolute path, open in browser
                    html = './hw2ExtraCredit.html'
                    absPath = os.path.abspath(html)
                    webbrowser.open(f'file://{absPath}')