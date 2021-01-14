# This file is where we implement the Markov Chain
import random

# Define the graph in terms of verticies
class Vertex:
    def __init__(self, value): # value represents a word
        self.value = value
        self.adjacent = {} # nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight=0):
        # add the edge the the vertex and input the weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # increment the edge of the vertex
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1 # look for vertex in list

    def probability_map(self):
        # Map each word to their probability but put them in seperate lists
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # New word based on weights (randomly)
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

# Now with a graph representation, it can be put into a graph
class Graph:
    def __init__(self):
        self.verticies = {} # empty dictionary

    def get_vertex_values(self):
        # what are the values from all the verticies?
        # simply, return all observed words
        return set(self.verticies.keys())

    def add_vertex(self, value):
        self.verticies[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.verticies:
            self.add_vertex(value)
        return self.verticies[value] # get the Vertex object

    def get_next_word(self, current_vertex):
        return self.verticies[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.verticies.values():
            vertex.probability_map()
