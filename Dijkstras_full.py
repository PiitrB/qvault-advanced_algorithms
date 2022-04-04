# Assignment
# Complete the dijkstra and dijkstra_r functions that calculate the shortest path through a 
# weighted graph from the src to the dest node.

# dijkstra(graph, src, dest):
# Modify the dijkstra function to return the return value of a recursive dijkstra_r function call, 
# be sure to pass it all the necessary parameters

# dijkstra_r(graph, src, dest, unvisited, distances, predecessors={})
# This is the recursive portion of the algorithm.
# Inputs:
# graph: same as before
# src: the key of the current node
# dest: same as before
# unvisted: a set of the nodes that haven't been visited yet
# distances: a dictionary of the shortest known paths to the nodes in the graph
# predecessors: a dictionary that keeps track of the path we've taken by storing all the predecessors
# 
# Algorithm:
# If the given src and dest are the same, we've reached the base case.
#   Create a new empty list to hold the full path
#   Create a variable to hold the current node and set it to dest
#   While there is a predecessor to the current node in the predecessors dictionary, add all the 
#     predecessors to the path list. By the end of this, you should have the shortest path that was taken by the algorithm in reverse order
#   Use Python's reverse() function to reverse the path to the correct order and return it
# Otherwise, set the min_dist to positive infinity and the min_neighbor to the src
# For each neighbor of the source node:
#   If the neighbor hasn't been visited yet:
#       Get the distance_so_far to the src node using the distances dictionary.
#       Get the distance_to_neighbor using the graph
#       Add the distance_so_far to the distance_to_neighbor to get the total_distance_to_neighbor
#       If the total_distance_to_neighbor is less than the current known distance to the neighbor
#           Set the current known distance to the neighbor to total_distance_to_neighbor
#           Set the neighbor's predecessor to the src
#       If total_distance_to_neighbor < min_dist
#           Set min_dist to the total_distance_to_neighbor
#           Set min_neighbor to the neighbor
# Remove the source node from the unvisited set
# Recursively call the dijkstra_r and with the min_neighbor as the new src

def dijkstra(graph, src, dest):
    unvisited = set()
    for node in graph:
        unvisited.add(node)
    distances = {}
    for node in graph:
        if node == src:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    ## change this return
    return graph, src, dest, unvisited, distances


def dijkstra_r(graph, src, dest, unvisited, distances, predecessors={}):
    # ?

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    graph = {
        'a': {'b': 4, 'c': 1},
        'b': {'a': 4, 'd': 3, 'e': 8},
        'c': {'a': 1, 'd': 2, 'f': 6},
        'd': {'c': 2, 'b': 3, 'e': 4},
        'e': {'d': 4, 'b': 8, 'g': 2},
        'f': {'c': 6, 'g': 8},
        'g': {'f': 8, 'e': 2}
    }
    print(dijkstra(graph, 'a', 'g'))
    graph = {
        's': {'a': 2, 'b': 1},
        'a': {'s': 3, 'b': 4, 'c': 8},
        'b': {'s': 4, 'a': 2, 'd': 2},
        'c': {'a': 2, 'd': 7, 't': 4},
        'd': {'b': 1, 'c': 11, 't': 5},
        't': {'c': 3, 'd': 5}
    }
    print(dijkstra(graph, 's', 't'))


main() ``
