# Assignment
# Complete the dijkstra function. Its job is to initialize the values that the recursive dijkstra_r function 
# will need to perform the meat of the algorithm in the next exercise.

# dijkstra(graph, src, dest)
# Inputs
# graph: an adjacency list of the vertices in the graph. graph[node1][node2] = weight_of_edge
# src: the key of the source node
# dest: the key of the destination node
# Outputs
# graph: the unmodified graph it was given
# src: the unmodified source it was given
# dest: the unmodified destination it was given
# unvisited: a set of all the nodes in the graph
# distances: a dictionary of node -> distance. The source node's entry should have a distance of 0 and all other 
#             distances should start at positive infinity.
# Algorithm
# Create a new empty Python set called unvisted
# Add each node in the graph to the unvisted set
# Create an empty dictionary called distances. The keys will be nodes and the values will be the "distance so far" to that node from the src
# Initialize the distance of the src node to 0 and all other nodes to positive infitity. Use float('inf') syntax to do so.
# Return everything as a tuple. For example, return graph, src, dest, unvisited, distances

def dijkstra(graph, src, dest):
    unvisited = set()
    distances = {}
    for vertice in graph:
        unvisited.add(vertice)
        if vertice == src:
            distances[vertice] = 0
        else:
            distances[vertice] = float("inf")
    return graph, src, dest, unvisited, distances
    


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
    print(dijkstra(graph, 'a', 'g')[0])
    print(dijkstra(graph, 'a', 'g')[1])
    print(dijkstra(graph, 'a', 'g')[2])
    print(sorted(dijkstra(graph, 'a', 'g')[3]))
    print(dijkstra(graph, 'a', 'g')[4])
    graph = {
        's': {'a': 2, 'b': 1},
        'a': {'s': 3, 'b': 4, 'c': 8},
        'b': {'s': 4, 'a': 2, 'd': 2},
        'c': {'a': 2, 'd': 7, 't': 4},
        'd': {'b': 1, 'c': 11, 't': 5},
        't': {'c': 3, 'd': 5}
    }
    print("-----")
    print(dijkstra(graph, 's', 't')[0])
    print(dijkstra(graph, 's', 't')[1])
    print(dijkstra(graph, 's', 't')[2])
    print(sorted(dijkstra(graph, 's', 't')[3]))
    print(dijkstra(graph, 's', 't')[4])


main()
