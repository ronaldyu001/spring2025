import math
import scipy.optimize
import sympy
import scipy
import time

# --------- #
#   Q1      #
# --------- #
#log(n)
def log_n(time):
    n = sympy.Pow(2, time).evalf()
    print(n)


# sqrt(n)
def sqrt_n(time):
    n = time ** 2
    print(n)


# n
def n(time):
    n = time
    print(n)


# n*log(n)
def n_log_n(time):
    def equation(n):
        return n*math.log2(n) - time
    print(scipy.optimize.fsolve(equation, time/100))


# n^x
def n_exp(exponent, time):
    newExp = 1/exponent
    n = time ** (newExp)
    print(n)


# 2^n
def two_exp_n(time):
    n = math.log2(time)
    print(n)


# n!
def n_fact(time):
    n = 1
    while(math.factorial(n) < time):
        n += 1
    if math.factorial(n) == time:
        print(n - 1)
    else:
        print(f'~{n - 1} = {math.factorial(n)}')


# --------- #
#   Q2      #
# --------- #
# time efficiency decorator
def timeEfficiencyDecorator(func):
    def wrapper(*args, **kwargs):
        # get start time before inner function
        startTime = time.time()
        print(f'Start Time: {startTime}')

        # inner function
        func(*args, **kwargs)

        # get end time and calculate duration after inner function
        endTime = time.time()
        print(f'End Time: {endTime}')
        duration = endTime - startTime
        print(f'Duration: {duration}')
    return wrapper


# insertion algorithm
@timeEfficiencyDecorator
def insertionSort(file):
    # variables
    comparisonCounter = 0
    sorted = []

    # extract numbers from file into list
    with open(file, "r") as file:
        unsorted = [int(num) for line in file for num in line.split()]
    
    # add first unsorted value to sorted list
    sorted.append(unsorted[0])

    # go through each value in unsorted list
    for i in range(1, len(unsorted)):
        for j in range(len(sorted)):
            comparisonCounter += 1
            if(unsorted[i] <= sorted[j]):
                sorted.insert(j, unsorted[i])
                inserted = True
                break
        if not inserted:
            sorted.append(unsorted[i])
    print(sorted, comparisonCounter)