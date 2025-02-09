import functions_HW1b
import random

if(__name__ == "__main__"):
    choice = 0

    while(choice != 6):
        # display menu and ask for menu option
        print(f'\
              1) Binary Search Number Guessing Game\n\
              2) Time Efficiency Function\n\
              3) Guessing Game\n\
              4) Collatz Sequence Generator\n\
              5) Extra Credit: Time Efficiency using decorator\n\
              6) Quit\n')
        choice = int(input('Enter Menu Option: '))

        if(choice == 1):
            # binary search guessing game
            max = 1000
            sum = 0
            average = 0
            for i in range(10000):
                sum += functions_HW1b.binarySearch(max)
            average = sum / 10000
            print(f'Numbers 1 - 1000: Total Guesses: {sum} Avg: {average}')

            max = 1000000
            sum = 0
            average = 0
            for i in range(10000):
                sum += functions_HW1b.binarySearch(max)
            average = sum / 10000
            print(f'Numbers 1 - 1000000: Total Guesses: {sum} Avg: {average}')


        elif(choice == 2):
            # time efficiency
            functions_HW1b.timeEfficiency(functions_HW1b.listPrimeNumbers)
        
        elif(choice == 3):
            # guessing game
            functions_HW1b.guessingGame()

        elif(choice == 4):
            # Colatz generator
            colatzLengths = []

            for i in range(1, 10000001):
                colatzSequence = []
                functions_HW1b.colatzGenerator(colatzSequence, i)
                colatzLengths.append([i, len(colatzSequence), max(colatzSequence)])

            sortedLengths = sorted(colatzLengths, key=lambda x: x[1])
            topTen = sortedLengths[-10:]
            topTen.reverse()

            print(f'\nTop Ten Sequences:')
                  
            for i in range(1, len(topTen) + 1):
                print(f'{i}. Collatz sequence for {topTen[i - 1][0]} has {topTen[i - 1][1]} values, whose largest value is {topTen[i - 1][2]}')
            print()

        elif(choice == 5):
            # time efficiency extra credit
            functions_HW1b.listPrimeNumbers2(1000)
