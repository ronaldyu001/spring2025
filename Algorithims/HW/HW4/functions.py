import time
import random
import matplotlib
import matplotlib.pyplot
from pathlib import Path

"""
This file contains utility functions used across the entire HW.
"""

# time efficiency decorator
def timeEfficiencyDecorator( func ):
    def wrapper( *args, **kwargs ):
        # get start time before inner function
        startTime = time.time()
        print( f'Start Time: { startTime }' )

        # inner function
        func( *args, **kwargs )

        # get end time and calculate duration after inner function
        endTime = time.time()
        print( f'End Time: { endTime }' )
        duration = endTime - startTime
        print( f'Duration: { duration }' )
        return duration
    return wrapper


# read file into list
def readFile( file ):
    file_path = Path(file)
    with file_path.open("r") as f:
        array = [ int( num ) for line in f for num in line.split() ]
        return array


# plot
def plot(x, y, title, color):
    # graph will open in separate window
    # fig = matplotlib.pyplot.figure()
    
    # plot
    matplotlib.pyplot.plot(x, y, marker='o', linestyle='-', color=color, label='Line Plot')

    # Add text labels for each point
    for i in range(len(x)):
        matplotlib.pyplot.text(x[i], y[i], f'{y[i]})', fontsize=10, ha='right')

    # axis labels and title
    matplotlib.pyplot.xlabel('k')
    matplotlib.pyplot.ylabel('Execution Time (s)')
    matplotlib.pyplot.title(title)

    # show both graphs at the same time
    matplotlib.pyplot.show(block=False)
