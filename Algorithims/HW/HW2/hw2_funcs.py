import math
import matplotlib.figure
import matplotlib.pyplot
import scipy.optimize
import sympy
import scipy
import time
import matplotlib

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


# read file into list
def readFile(file):
    # extract numbers from file into list
    with open(file, "r") as file:
        unsorted = [int(num) for line in file for num in line.split()]
        return unsorted


# insertion sort
@timeEfficiencyDecorator
def insertionSort(file):
    # variables
    comparisonCounter = 0
    sorted = []

    # extract numbers from file into list
    unsorted = readFile(file)
    
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
    # print(sorted, comparisonCounter)
    print(f'Comparisons: {comparisonCounter}')


# global counter for merge sort
_comparisonCounter = 0

# merge sort (merge)
def merge(left, right):
    #variables
    sorted = []
    i = j = 0
    global _comparisonCounter

    # merge left and right halves in sorted order
    while i < len(left) and j < len(right):
        _comparisonCounter += 1
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    # If any elements remain in either left or right, add them to the sorted list
    sorted.extend(left[i:])
    sorted.extend(right[j:])

    return sorted


# merge sort container
@timeEfficiencyDecorator
def mergeSortContainer(file):
    # read file into list
    global _comparisonCounter
    unsorted = readFile(file)
    _comparisonCounter = 0
    x = mergeSort(unsorted)
    print(f'{file}: {_comparisonCounter} comparisons')
    return


# merge sort
def mergeSort(unsorted):
    # DIVIDE
    # base case: return sublist when size reaches 1
    if len(unsorted) == 1:
        return unsorted[:]

    # find middle, recursively divide left and right sides
    middle = len(unsorted) // 2
    left = mergeSort(unsorted[:middle])
    right = mergeSort(unsorted[middle:])

    # merged sublists, return sorted list
    return merge(left, right)


# plot
def plot(x, y, title):
    # graph will open in separate window
    fig = matplotlib.pyplot.figure()
    
    # plot
    matplotlib.pyplot.plot(x, y, marker='o', linestyle='-', color='b', label='Line Plot')

    # Add text labels for each point
    for i in range(len(x)):
        matplotlib.pyplot.text(x[i], y[i], f'{y[i]})', fontsize=10, ha='right')

    # axis labels and title
    matplotlib.pyplot.xlabel('Data Size (n)')
    matplotlib.pyplot.ylabel('Execution Time (s)')
    matplotlib.pyplot.title(title)

    # show both graphs at the same time
    matplotlib.pyplot.show(block=False)