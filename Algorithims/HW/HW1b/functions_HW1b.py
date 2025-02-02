# libraries
import time
import random


# binary search
def binarySearch(maxValue, secretNumber):
    """
    Uses binary search to guess a number.

    Input: secret number to be guessed
    Output: total guesses, average of guesses
    """

    # variables
    numOfGuesses = 1
    guess = maxValue
    upperBound = maxValue
    lowerBound = 1
    sumOfGuesses = 0
    averageOfGuesses = 0

    # check secret number
    if(secretNumber < 1 or secretNumber > maxValue):
        print(f'secret number entered is out of given range')
        return 0, 0, 0

    # perform binary search
    while(guess != secretNumber):
        # if guess is lower than secret number:
        # - guess becomes the new lower bound
        # - update sumOfGuesses
        if(guess < secretNumber):
            lowerBound = guess
            sumOfGuesses += guess

        # if guess is higher than secret number:
        # - guess becomes the new upper bound
        # - update sumOfGuesses
        elif(guess > secretNumber):
            upperBound = guess
            sumOfGuesses += guess

        # else the number has been guessed
        else:
            break

        # update the guess based on the new bounds, increment guess counter
        guess = (lowerBound + upperBound)//2
        numOfGuesses += 1

    # compute the average
    averageOfGuesses = sumOfGuesses / numOfGuesses
    
    return guess, numOfGuesses, averageOfGuesses


# time efficiency
def timeEfficiency(funcName, args):
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
    funcName(*args)

    # end timer
    end_time = time.time()

    # print start, end, and total times
    print(f'Start Time: {start_time}\nEnd Time: {end_time}\nDuration: {end_time - start_time}s')


# timeEfficiency input function
def random_duration(min_duration, max_duration):
    """
    sleeps a random amount of seconds between the
    min_duration and max_duration
    """
    random_duration = random.uniform(min_duration, max_duration)
    time.sleep(random_duration)