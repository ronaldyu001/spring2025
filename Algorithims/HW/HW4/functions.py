import time
import random
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path


"""
This file contains utility functions used across the entire HW.
"""


#
# TIME EFFICIENCY DECORATOR
#
def timeEfficiencyDecorator( func ):
    def wrapper( *args, **kwargs ):
        # get start time before inner function
        startTime = time.time()
        print( f'Start Time: { startTime }' )

        # inner function
        result = func( *args, **kwargs )

        # get end time and calculate duration after inner function
        endTime = time.time()
        print( f'End Time: { endTime }' )
        duration = endTime - startTime
        print( f'Duration: { duration }' )

        return result, duration

    return wrapper


#
# READ FILE INTO LIST
#
def readFile( file ):
    file_path = Path(file)
    with file_path.open("r") as f:
        array = [ int( num ) for line in f for num in line.split() ]
        return array


#
# PLOT A LINE GRAPH
#
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


#
# PRINT ARRAY TO FILE
#
def array_to_text_file( arr, filename ):
    with open( filename, 'w' ) as f:
        for item in arr:
            f.write(f"{item}\n")


#
# CHECK IF ARRAY IS SORTED
#
def is_sorted( array ):
    for i in range( len(array) - 1 ):
        if array[ i ] > array[ i + 1 ]:
            return False
    return True 


#
# PLOT A BAR GRAPH
#
def plot_bar_graph( title, ylabel, xlabel, values, xlabels ):
    # if number of values doesn't match number of labels on x-axis, throw error
    if len( values ) != len( xlabels ):
        raise ValueError( "Length of values and xlabels must be the same." )

    # 
    x = list( range(len(values)) )

    # 
    plt.figure( figsize=(8, 6) )
    bars = plt.bar( x, values, color='skyblue' )

    # Title and axis labels
    plt.title( title )
    plt.ylabel( ylabel )
    plt.xlabel( xlabel )

    # Custom x-axis labels
    plt.xticks( x, xlabels, rotation=45 )

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.2f}',
            ha='center',
            va='bottom'
        )

    # 
    plt.tight_layout()
    plt.show()
