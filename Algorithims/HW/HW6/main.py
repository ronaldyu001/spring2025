from Question_1_2 import *
from Question_3 import *
from math import ceil, log2
import os


"""
This file contains the implementation of Questions 1 and 2.
"""


if __name__ == "__main__":
    while True:

        # menu
        print( f'\n\n----------------------------------------\n' )
        print( f'   HW 6:' )
        print( f'   0) Exit' )
        print( f'   1) Dijkstras' )
        print( f'   2) MST' )
        print( f'   3) Zip' )
        print( f'\n----------------------------------------\n' )
        choice = int(input( f'Enter menu choice: ' ))
        

        # 0)
        if choice == 0:
            break

        # 1)
        elif choice == 1:
            # set nodes and edges
            nodes = ["A", "B", "C", "D", "E"]
            edges = [   ["A", "B", 4],
                        ["A", "C", 2],
                        ["B", "C", 3],
                        ["B", "D", 2],
                        ["B", "E", 3],
                        ["C", "B", 1],
                        ["C", "D", 4],
                        ["C", "E", 5],
                        ["E", "D", 1] ]
            
            # build and confirm graph
            my_graph = build_graph( nodes, edges )
            print( f'Graph Info:' )
            print( f'   Nodes: {my_graph.nodes}' )
            print( f'   Edges: {my_graph.edges}' )
            print( f'   Distances: {my_graph.distances}' )

            # run Dijkstra's
            print( f'\nShortest Distance to Each Node:\n    {Dijkstra( my_graph, "A" )}' )

        
        # 2)
        elif choice == 2:
            # set nodes from distance table (would have been better to use code provided)
            nodes = [   "Atlanta",  "Boston",   "Chicago",
                        "Dallas",   "Denver",   "Houston",
                        "LA",       "Memphis",  "Miami",
                        "NY",       "Philly",   "Phoenix",
                        "SF",       "Seattle",  "W DC"      ]
            
            # set edges from distance table (would have been better to use code provided)
            edges = [   ["Atlanta", "Boston", 1505],    ["Atlanta", "Dallas", 1157],    ["Atlanta", "Miami", 973],  ["Atlanta", "SF", 3434],
                        ["Boston", "Atlanta", 1505],    ["Boston", "Chicago", 1367],    ["Boston", "Denver", 2839], ["Boston", "NY", 306],
                        ["Chicago", "Boston", 1367],    ["Chicago", "Denver", 1474],    ["Chicago", "NY", 1145],    ["Chicago", "Phoenix", 2332],
                        ["Dallas", "Atlanta", 1157],    ["Dallas", "Denver", 1064],     ["Dallas", "Houston", 362], ["Dallas", "Memphis", 675],     ["Dallas", "Phoenix", 1422],    ["Dallas", "W DC", 1900],
                        ["Denver", "Boston", 2839],     ["Denver", "Chicago", 1474],    ["Denver", "Dallas", 1064], ["Denver", "LA", 1335],         ["Denver", "Memphis", 1411],    ["Denver", "W DC", 2395],
                        ["Houston", "Dallas", 362],     ["Houston", "LA", 2205],
                        ["LA", "Denver", 1335],         ["LA", "Houston", 2205],        ["LA", "Miami", 3755],      ["LA", "NY", 3933],             ["LA", "SF", 559],              ["LA", "Seattle", 1544],
                        ["Memphis", "Dallas", 675],     ["Memphis", "Denver", 1411],    ["Memphis", "Philly", 1413],
                        ["Miami", "Atlanta", 973],      ["Miami", "LA", 3755],          ["Miami", "Phoenix", 3182], ["Miami", "W DC", 1487],
                        ["NY", "Boston", 306],          ["NY", "Chicago", 1145],        ["NY", "LA", 3933],         ["NY", "Phoenix", 3441],
                        ["Philly", "Memphis", 1413],    ["Philly", "Phoenix", 3342],    ["Philly", "W DC", 199],
                        ["Phoenix", "Chicago", 2332],   ["Phoenix", "Dallas", 1422],    ["Phoenix", "Miami", 3182], ["Phoenix", "NY", 3441],        ["Phoenix", "Philly", 3342],
                        ["SF", "Atlanta", 3434],        ["SF", "LA", 559],              ["SF", "Seattle", 1092],
                        ["Seattle", "LA", 1544],        ["Seattle", "SF", 1092],
                        ["W DC", "Dallas", 1900],       ["W DC", "Denver", 2395],       ["W DC", "Miami", 1487],    ["W DC", "Philly", 199]  ]
            
            # build graph
            my_graph = build_graph( nodes, edges )

            # run Dijkstra's
            start = "Denver"
            distances, paths = Dijkstra( my_graph, start )

            # reconstruct shortest paths for each location
            print( f'\nDistances from {start} to each location:' )
            for node in my_graph.nodes:
                path, distance = rebuild_paths_Dijkstra( paths, distances, start, node )
                for location in path:
                    # don't include path to itself
                    if node is start:
                        continue
                    elif location is node:
                        print( f'   {location}: {distance}' )
                        continue
                    else:
                        print( f'   {location}    -> ', end='' )


            # run MST
            print( '\n' )
            mst, cost = my_graph.Prim( start )

            print('\n')
            print( f'Departure:'.ljust(10), f'Arrival:'.ljust(27) , f'Weight'.ljust(10), end='\n\n' )
            for edge in mst:
                print( f'{edge[0]}'.ljust(10), f'{edge[1]}'.ljust(7), f'....................', f'{edge[2]}'.ljust(20) )

        
        # 3)
        elif choice == 3:
            # ask user for file
            text = read_file()
            # huffman
            huffman, frequencies = Huffman( text )
            # zip
            zipped_text, padding = zip( text, huffman )
            # unzip
            unzip( zipped_text, huffman, padding )

            # print info
            print( f'Character'.ljust(20), f'Frequency'.ljust(20), f'Huffman Code'.ljust(20) )
            total_huffman_cost = 0
            total_ASCII_cost = 0
            huffman_ASCII_efficiency = 0

            # calculate huffman and ASCII costs
            for key in huffman:
                print( f'{repr(key)}'.ljust(20), f'{frequencies[key]}'.ljust(20), f'{huffman[key]}'.ljust(20) )
                total_huffman_cost += int( frequencies[key] ) * len( huffman[key] )
                total_ASCII_cost += int( frequencies[key] ) * 8
            
            # Huffman cost
            print()
            print( f'Expected Huffman cost: {total_huffman_cost}', f'\n' )

            # ASCII cost and comparison
            print( f'Expected ASCII cost: {total_ASCII_cost}' )
            huffman_ASCII_efficiency = (total_ASCII_cost - total_huffman_cost) / total_huffman_cost * 100
            print( f'Huffman efficiency over ASCII: {huffman_ASCII_efficiency: .2f}%', f'\n' )

            # FCL cost and comparison
            total_FCL_cost =  ceil( log2(len(huffman)) ) * len( text )
            print( f'Expected FCL cost: {total_FCL_cost}' )
            huffman_FCL_efficiency = (total_FCL_cost - total_huffman_cost) / total_FCL_cost * 100
            print( f'Huffman efficiency over FCL: {huffman_FCL_efficiency: .2f}%' )

            # zip/unziipped size comparison
            original_file_size = os.path.getsize( './Q3.txt' )
            zipped_file_size = os.path.getsize( './Q3_zipped.bin' )
            unzipped_file_size = os.path.getsize( './Q3_unzipped' )
            print( f'Original file size: {original_file_size}' )
            print( f'Zipped file size: {zipped_file_size}' )
            print( f'Unzipped file size: {unzipped_file_size}' )
