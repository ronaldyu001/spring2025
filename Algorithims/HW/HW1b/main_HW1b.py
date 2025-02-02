import functions_HW1b

if(__name__ == "__main__"):
    choice = 0

    while(choice != 4):
        # display menu and ask for menu option
        print(f'1) Binary Search Number Guessing Game\n2) Time Efficiency Function\n3) Guessing Game\n4) Quit\n')
        choice = int(input('Enter Menu Option: '))

        if(choice == 1):
            # binary search guessing game
            guess, numOfGuesses, avgOfGuesses = functions_HW1b.binarySearch(int(input("Number is between 1 and ?: ")), int(input("Enter secret number: ")))
            print(f'The number is: {guess}\nNumber of Guesses: {numOfGuesses}\nAverage of Guesses: {avgOfGuesses}\n')
        
        elif(choice == 2):
            # time efficiency
            functions_HW1b.timeEfficiency(functions_HW1b.random_duration, [1, 5])
        
        elif(choice == 3):
            print("WIP")