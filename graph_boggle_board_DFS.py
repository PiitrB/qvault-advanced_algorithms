# Depth First Search
# Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
# The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and 
# explores as far as possible along each branch before backtracking.

# Assignment
# Given a list of words to find and a Boggle board of characters (represented by a graph), find the 
# maximum number of words that can be formed by a sequence of adjacent characters on the board.
# You can move in any direction but you cannot skip letters or go twice through the same one.
# You'll need to complete the following functions:

# find_words:
# Inputs
# words_to_find: a list of words we're trying to find on the Boggle graph
# graph: an adjacency list of the vertices in the graph. This graph has vertex ids, not characters
# Algorithm:
# Create an empty found_words list
# Loop over each vertex in the graph
# Call dfs for the vertex
# return found_words
# Keep in mind that since arrays are passed by reference, dfs doesn't need to return anything. found_words will be mutated within the calls to dfs.

# dfs:
# Inputs
# words_to_find: a list of words we're trying to find on the Boggle graph
# graph: an adjacency list of the vertices in the graph. This graph has vertex ids, not characters
# visited: the list of vertex ids visted so far
# vertex: the next vertex to visit
# found_words: the words found so far
# Algorithm:
# Visit the given vertex by appending it to the visited list
# Use the provided ids_to_word function to get the string value of the visited list, we'll call this the "current subword"
# Check if the current subword is in the words_to_find list using the provided is_word_in_list function. If it is, append the current subword to the found_words list.
# For each neighboring vertex:
#   If the neighbor has not yet been visited, call dfs on the neighbor
# Remove the last vertex from the visited list (the one we just visited)

def find_words(words_to_find, graph):
    found_words = []
    visited = []
    for vertex in graph:
        dfs(words_to_find, graph, visited, vertex, found_words)
    return found_words



def dfs(words_to_find, graph, visited, vertex, found_words):
    visited.append(vertex)
    subword = ids_to_word(visited)
    if is_word_in_list(subword, words_to_find):
        found_words.append(subword)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(words_to_find, graph, visited, neighbor, found_words)
    visited.pop()


    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def is_word_in_list(word, words):
    for w in words:
        if w == word:
            return True
    return False


def ids_to_word(list_of_ids):
    word = ""
    for id in list_of_ids:
        word += id_to_character(id)
    return word


def id_to_character(id):
    m = {
        0: 't',
        1: 'd',
        2: 'o',
        3: 'g',
        4: 'a',
        5: 't',
        6: 'i',
        7: 'c',
        8: 'b',
        9: 't',
        10: 'e',
        11: 'h',
        12: 'v',
        13: 'h',
        14: 'r',
        15: 'f',
    }
    return m[id]


def main():
    words_to_find = [
        "attic",
        "bat",
        "date",
        "dog",
        "hate",
        "her",
        "their",
        "tie",
        "baddy",
        "noone",
        "bitcoin",
        "amc",
        "gme"
    ]

    # Boggle board by character:
    # t d o g
    # a t i c
    # b t e h
    # v h r f
    graph = {
        0: [1, 4],
        1: [0, 2, 5],
        2: [1, 3, 6],
        3: [2, 7],
        4: [1, 5, 8],
        5: [1, 4, 6, 9],
        6: [2, 5, 7, 10],
        7: [3, 6, 11],
        8: [4, 9, 12],
        9: [5, 8, 10, 13],
        10: [6, 9, 11, 14],
        11: [7, 10, 15],
        12: [8, 13],
        13: [9, 12, 14],
        14: [10, 13, 15],
        15: [11, 14],
    }

    words = find_words(words_to_find, graph)
    print(words)


main()