# distanceGraph.py
# author: Justin Crawford
# date: 05/06/2020


class DistanceGraph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_location(self, new_address):
        self.adjacency_list[new_address] = []

    def add_directed_edge(self, from_address, to_address, weight=1):
        self.edge_weights[(from_address, to_address)] = weight
        self.adjacency_list[from_address].append(to_address)

    def add_undirected_edge(self, from_address, to_address, weight=1):
        self.add_directed_edge(from_address, to_address, weight)
        self.add_directed_edge(to_address, from_address, weight)

    def print_graph(self):
        print(self.edge_weights.values())

    def find_distance(self, start, end):
        pass


class Vertex:
    def __init__(self, label):
        self.label = label
