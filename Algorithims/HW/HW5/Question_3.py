import re
from collections import Counter


"""
This file contains functions used in Question 3.
These functions pertain to the spell checker implemented in main.py.
"""


# memoization function (from slides)
def editDistanceDP(s1, s2, m, n, memo):

    if memo[m][n] > -1: return memo[m][n]
    if m == 0 : memo[m][n] = n; return memo[m][n]
    if n == 0 : memo[m][n] = m; return memo[m][n]    
    if s1[m-1] == s2[n-1] : 
        memo[m][n] = editDistanceDP(s1, s2, m-1, n-1, memo)
        return memo[m][n]
    memo[m][n] = 1 + min(editDistanceDP(s1, s2, m, n-1, memo),\
                    editDistanceDP(s1, s2, m-1, n, memo),\
                    editDistanceDP(s1, s2, m-1, n-1, memo))
    return memo[m][n]


# function to build dictionary from text file
# each pair contains text and frequency
def build_dictionary( input_text ):
    with open( input_text, 'r' ) as file:
        words = re.findall( r'[a-z]+', file.read().lower() )
    return Counter( words )


# function to build list of words from text file
def build_list( input_text ):
    with open( input_text, 'r') as file:
        words = re.findall( r'[a-z]+', file.read().lower() )
    return words


# generate suggestions
def generate_suggestions( mispelled_word, dictionary, max_suggestions, min_word_length, max_edit_distance ):
    # variables
    suggestions = []

    # return empty suggestions if the word is not mispelled
    if mispelled_word in dictionary:
        return suggestions

    # come up with suggestions with edit distance and frequency
    for word, frequency in dictionary.items():
        # initialize table
        memo = [[-1 for i in range( len(mispelled_word)+1 )]   for j in range( len(word)+1 )]
        if len( mispelled_word ) >= min_word_length:
            edit_distance = editDistanceDP( word, mispelled_word, len(word), len(mispelled_word), memo)
            # print( f'comparing {mispelled_word} with {word}' )
            if edit_distance <= max_edit_distance:
                suggestions.append( (word, (edit_distance, frequency)) )

    # sort suggestions based on edit distance then frequency
    suggestions.sort( key=lambda x: (x[1][0], -x[1][1]) )

    # return maximum amount of sorted suggestions
    return suggestions[ :max_suggestions ]