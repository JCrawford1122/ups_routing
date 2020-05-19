# distanceGraph.py
# Author: Justin Crawford
# Student ID: 000918681
# Date: 5/17/2020
import csv


class DistanceGraph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    # add a vertex to the adjacency list
    # O(N)
    def add_location(self, new_address):
        self.adjacency_list[new_address] = []

    # Add a directed edge between two vertexes
    # O(N)
    def add_directed_edge(self, from_address, to_address, weight=1):
        self.edge_weights[(from_address, to_address)] = weight
        self.adjacency_list[from_address].append(to_address)

    # Adds undirected edge between two vertexes
    # O(N)
    def add_undirected_edge(self, from_address, to_address, weight=1):
        self.add_directed_edge(from_address, to_address, weight)
        self.add_directed_edge(to_address, from_address, weight)

    # Method gets a vertex object from the adjacency list
    # O(N)
    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None


class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

