import sys
from Question_3 import *


"""
This file contains the implementation of the spell checker.

"""


def main():
    # accept command line arguments
    max_suggestions = int( sys.argv[1] )

    # set constraints
    min_word_length = 2
    max_edit_distance = 5

    # input files
    input_text = './Q3/Data/dictionary.txt'
    mispelled_text = './Q3/Data/misspelled.txt'

    # build dictionary (words in text) and list (mispelled words)
    my_dictionary = build_dictionary( input_text )
    my_list = build_list( mispelled_text )

    # go through mispelled words
    for misspelled_word in my_list:
        if len( misspelled_word ) < min_word_length:
            continue
        print( f'Suggestions for "{misspelled_word}":' )
        suggestions = generate_suggestions( misspelled_word, my_dictionary, max_suggestions, min_word_length, max_edit_distance )
        if len( suggestions ) == 0:
            print(f'No suggestions available.')
        else:
            for suggestion, (edit_distance, frequency) in suggestions:
                print( f'Word: {suggestion}, Edit Distance: {edit_distance}, Frequency: {frequency}' )
        print()


if __name__ == "__main__":
    main()