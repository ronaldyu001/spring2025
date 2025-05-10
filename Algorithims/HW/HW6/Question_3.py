from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray, decodetree
import math
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename


"""
This file contains code for Q3.
"""


#
#   Huffman function to match characters with binary
#
def Huffman( text ):
    # create dictionary
    char_freq_dict = {}

    # get frequency of each letter in text
    for char in text:
        if char in char_freq_dict:
            char_freq_dict[ char ] += 1
        else:
            char_freq_dict[ char ] = 1

    # **this block of code was taken from the lecture slides**
    heap = [[freq, [aChar, ""]] for aChar, freq in char_freq_dict.items()]  # build a minheap
    heapify( heap )
    while len( heap ) > 1:
        lo = heappop( heap )  # pop least frequent, then heapify
        hi = heappop( heap )  # next least frequent , then heapify
        for pair in lo[ 1: ]:
            pair[ 1 ] = '0' + pair[ 1 ]  #pair[1] is the current codeword for pair[0] char
        for pair in hi[ 1: ]:
            pair[ 1 ] = '1' + pair[ 1 ]
        heappush( heap, [lo[0] + hi[0]] + lo[1:] + hi[1:] ) #push then heapify

    return dict( sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p)) ), char_freq_dict


#
#   zip function to convert text to binary based on huffman
#
def zip( text, huffman ):
    # empty string for binary
    binary_text = ''

    # go through text and append binary to string
    for char in text:
        binary_text += huffman[ char ]

    # get padding and add to end of binary_text
    padding = 8 - len( binary_text ) % 8
    binary_text += '0' * padding

    # add binary_text to compressed_text (byte array) 8 chars at a time as binary number
    compressed_text = bytearray( int(binary_text[i:i+8], 2) for i in range(0, len(binary_text), 8) )
        
    # write to file in binary mode
    with open( 'Q3_zipped.bin', 'wb' ) as file:
        file.write( compressed_text )
    
    return file.name, padding


#
#   unzip binary file back to text
#
def unzip( file, huffman, padding ):
    with open( file, 'rb' ) as file:
        compressed_text = file.read()

    bit_string = ''
    for byte in compressed_text:  # read byte by byte
        bit_string += format( byte, '08b' )

    bit_string = bit_string[ :-padding ]

    binary_letter = ''
    original_text = ''
    swapped_huffman = { x:y  for y,x in huffman.items()  }

    for bit in bit_string:
        if binary_letter not in swapped_huffman:
            binary_letter += bit
        else:
            original_text += swapped_huffman[ binary_letter ]
            binary_letter = bit

    if binary_letter in swapped_huffman:
        original_text += swapped_huffman[ binary_letter ]


    write_file( original_text )

    return



#
#   window opens to prompt user to select text file
#
def read_file():
    # Hide the root tkinter window
    Tk().withdraw()

    # Open a file dialog and ask the user to choose a text file
    file_path = askopenfilename( title="Select a text file", filetypes=[("Text Files", "*.txt")] )

    if not file_path:
        return None

    with open( file_path, 'r' ) as file:
        text = file.read()

    return text


#
#   write to file
#
def write_file( text ):
    with open( 'Q3_unzipped', 'w' ) as file:
        file.write( text )