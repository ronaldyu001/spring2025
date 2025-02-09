# libraries
import time
import random
import decorators


# binary search
def binarySearch(maxValue):

    # variables
    numOfGuesses = 0
    upperBound = maxValue
    lowerBound = 1
    secretNumber = random.randint(1, maxValue)

    # perform binary search
    while(lowerBound <= upperBound):
        guess = (lowerBound + upperBound) // 2

        if(guess < secretNumber):
            lowerBound = guess + 1 
            numOfGuesses += 1
        elif(guess > secretNumber):
            upperBound = guess -1
            numOfGuesses += 1
        else:
            return numOfGuesses


# time efficiency
def timeEfficiency(func):

    """
    takes a function as an INPUT along with its arguments.
    runs it.
    OUTPUTs the start time, end time, and duration.
    """

    # variables
    start_time = 0
    end_time = 0

    # start timer
    start_time = time.time()

    # run function
    primes = func(int(1000))

    # end timer
    end_time = time.time()

    # print start, end, and total times
    print(f'Start Time: {start_time}\nEnd Time: {end_time}\nDuration: {end_time - start_time}')
    print(f'Result: [{primes[0]}, {primes[1]}, {primes[2]}, {primes[3]}, {primes[4]}, ... \
,{primes[-5]}, {primes[-4]}, {primes[-3]}, {primes[-2]}, {primes[-1]}]')


# list prime numbers (code written by AI)
def listPrimeNumbers(maxNumber):
    """Finds all prime numbers from 2 to max_num."""
    primes = []
    for num in range(2, int(maxNumber) + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# guessing game
def guessingGame():

    # variables
    tries = 10000
    deterministicSum = 0
    randomSum = 0
    deterministicAverage = 0
    randomAverage = 0
    deterministicNumGuesses = 0
    randomNumGuesses = 0
    deterministicMaxGuesses = 0
    randomMaxGuesses = 0
    deterministicMinGuesses = tries
    randomMinGuesses = tries

    # repeat guessing game x amount of times
    for i in range(tries):

        # generate list of 3 random numbers (0-9)
        randomNumbers = [random.randint(0, 9) for i in range(3)]

        # keep track of sum of guesses
        deterministicNumGuesses = deterministicGuesser(randomNumbers)
        randomNumGuesses = randomGuesser(randomNumbers)
        deterministicSum += deterministicNumGuesses
        randomSum += randomNumGuesses

        # keep track of max guesses
        if(deterministicNumGuesses > deterministicMaxGuesses):
            deterministicMaxGuesses = deterministicNumGuesses
        elif(deterministicNumGuesses < deterministicMinGuesses):
            deterministicMinGuesses = deterministicNumGuesses
        
        if(randomNumGuesses > randomMaxGuesses):
            randomMaxGuesses = randomNumGuesses
        elif(randomNumGuesses < randomMinGuesses):
            randomMinGuesses = randomNumGuesses

    # compute guess count averages
    deterministicAverage = deterministicSum / tries
    randomAverage = randomSum / tries

    # print results
    print(f'Deterministic Brute Force approach:\n\
        Number of tries: {tries}\n\
        Max number guesses: {deterministicMaxGuesses}\n\
        Lowest number guesses: {deterministicMinGuesses}\n\
        Average number of guesses: {deterministicAverage}\n')
    
    print(
        f'Random approach:\n\
        Number of tries: {tries}\n\
        Max number guesses: {randomMaxGuesses}\n\
        Lowest number guesses: {randomMinGuesses}\n\
        Average number of guesses: {randomAverage}\n')
    

# guessing game - deterministic brute-force algorithm
def deterministicGuesser(numbers):
    """
    Guesses each combination of the three numbers until correct.
    Start at [0, 0, 0], End at [9, 9, 9]
    odds of being correct: 1/9^3
    """
    # variables
    guess = []
    guessCounter = 0

    # guess each combination of the three numbers
    for i in range(10):
        for j in range(10):
            for k in range(10):

                guess = [i, j, k]
                guessCounter += 1

                if(guess == numbers):
                    # print(f'The numbers are: {guess}')
                    return guessCounter


# guessing game - pure random algorithm
def randomGuesser(numbers):

    # variables
    guess = []
    guessCounter = 0

    # keep randomly guessing until correct
    while(guess != numbers):
        guess = [random.randint(0, 9) for i in range(3)]
        guessCounter += 1
    
    return guessCounter


def colatzGenerator(colatzSequence, number):

    # error handling: number < 1
    if(number < 1):
        print("Number must be greater than 0.")
        return
    
    # base case
    if(number == 1):
        colatzSequence.append(int(number))
        return colatzSequence
    
    # update sequence
    colatzSequence.append(int(number))
    
    # recursive calls
    if(number % 2 == 0):
        colatzGenerator(colatzSequence, number / 2)
    else:
        colatzGenerator(colatzSequence, number*3 + 1)


@decorators.timeEfficiencyDecorator
def listPrimeNumbers2(maxNumber):
    """Finds all prime numbers from 2 to max_num."""
    primes = []
    for num in range(2, int(maxNumber) + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

    