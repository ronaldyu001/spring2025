from functions import*
import requests
import webbrowser
from bs4 import BeautifulSoup
import networkx as nx
import re
import unicodedata


"""
This file contains the functions used for the Extra Credit.
"""

#
#   extract html
#
def get_html( url ):
    # get reponse from url
    response = requests.get( url )

    # if response status code not valid, print error
    if response.status_code != 200:
        print( 'Response Status Code invalid.' )
        return
    
    # if reponse status code valid, return html
    return response


#
#   find elements based on its type and class
#
def find_elements( html, _type, _class ):
    # get soup object using Python's parser
    soup = BeautifulSoup( html, 'html.parser' )

    # extract list of desired elements as a list of BeautifulSoup Tag objects
    return soup.find_all( _type, class_=_class )


#
#   extract text from a nested element
#
def extract_text( elements, _type, _class ):
    # list for extracted elements
    extracted_elements = []

    # add each element's text with maatching type and class
    for element in elements:
        extracted_elements.append( element.find(_type, _class).text )

    return extracted_elements


#
#   create directed graph
#
def directed_graph( course_numbers, prereqs ):
    import matplotlib.pyplot as plt 
    # Create a graph object
    G = nx.DiGraph()

    # populate graph
    for i in range( len(course_numbers) ):
            for j in range( len(prereqs[i]) ):
                temp = str( re.findall( r'(?:[A-Z]{4}|\s)?\s*\d{4}', str(prereqs[i][j]) ) )
                # trying to replace '\wa0\' with ' '
                # not working
                temp = re.sub( r'\s+', ' ', temp )

                # if temp not empty, add edge to graph
                if temp:
                    G.add_edges_from([( str(course_numbers[i]), temp )])

    # layout
    pos = nx.spring_layout( G, k=.7 )

    # draw graph
    nx.draw(G, pos, with_labels=True, arrows=True, node_color='skyblue', edge_color='gray', node_size=800, font_size=4)

    # Show the graph
    plt.title('CS_courses')
    plt.show()