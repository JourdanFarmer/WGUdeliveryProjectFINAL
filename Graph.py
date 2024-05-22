# Jourdan Farmer, ID: 011503932

import csv
from HashTable import HashTable


class Graph:
    # constructor
    # time complexity: O(1)
    # space complexity: O(1)
    def __init__(self):
        self.location_names = [None] * 27
        self.raw_distance_data = []
        self.adjacency_matrix = HashTable()

    # interprets location data
    # time complexity: O(n)
    # space complexity: O(n)
    def initialize_location_name(self):
        with open("./data/distance_names.csv") as file:
            names_reader = csv.reader(file)
            raw_distance_names = list(names_reader)
            i = 0
        for entry in raw_distance_names:
            self.location_names[i] = entry
            i += 1

    # interprets distance
    # time complexity: O(n)
    # space complexity: O(n)
    def initialize_location_distance(self):
        with open("./data/distance_data.csv") as file:
            reader = csv.reader(file)
            self.raw_distance_data = list(reader)

    # interprets raw_distance_data from distance_data.csv
    # time complexity: O(n^2)
    # space complexity: O(n^2)
    def initialize_nodes_hashtable(self):
        for i in range(len(self.raw_distance_data)):
            for j in range(len(self.raw_distance_data)):
                if j < i:
                    self.add_node(
                        from_node=self.location_names[i][1], to_node=self.location_names[j][1], weight=self.raw_distance_data[i][j])
                elif j > i:
                    self.add_node(
                        from_node=self.location_names[i][1], to_node=self.location_names[j][1], weight=self.raw_distance_data[j][i])

    # adds node to matrix
    # time complexity: O(1)
    # space complexity: O(1)
    def add_node(self, from_node, to_node, weight):
        node = self.adjacency_matrix.get(from_node)
        if node != None:
            node.edges.append(
                Edges(from_node, to_node, weight))
            self.adjacency_matrix.add(from_node, node)
        else:
            self.adjacency_matrix.add(
                from_node, Node(from_node, [Edges(from_node, to_node, weight)]))

    # print node function
    # time complexity: O(n^2)
    # space complexity: O(n^2)
    def print_nodes(self):
        for from_vertex in self.location_names:
            connected_verticies = []
            for edge in self.adjacency_matrix.get(from_vertex[1]).get_edge():
                connected_verticies.append(
                    f"{edge.from_node}-({edge.weight})->{edge.to_node}")
            print(f"{edge.from_node} is connected to {connected_verticies}")


# Graph edges
class Edges():

    # init
    # time complexity: O(1)
    # space complexity: O(1)
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    # string
    # time complexity: O(1)
    # space complexity: O(1)
    def __str__(self):
        #  -> {self.weight}
        return f"{self.from_node} -> {self.to_node}"


# Graph nodes
class Node():

    # init
    # time complexity: O(1)
    # space complexity: O(1)
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges

    # string
    # time complexity: O(1)
    # space complexity: O(1)
    def __str__(self):
        return f"{self.name}"

    # add function
    # time complexity: O(1)
    # space complexity: O(1)
    def add_edge(self, target_node, weight):
        self.edges.add(target_node, Edges(from_node=self.name,
                       to_node=target_node, weight=weight))

    # getter
    # time complexity: O(1)
    # space complexity: O(1)
    def get_edge(self):
        return self.edges
