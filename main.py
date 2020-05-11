# main.py
# author: Justin Crawford
# date: 05/06/2020
import csv
from location import Location
from distanceGraph import DistanceGraph, Vertex
from package import Package
from hashTable import HashTable
from truck import Truck
# instantiate the package hash table
hash_table = HashTable()
distance_graph = DistanceGraph()
# read the package file
with open('package_data.csv') as package_file:
    csv_reader = csv.reader(package_file, delimiter=',')
    for row in csv_reader:
        # Create package
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        # Add the package to the hash table
        hash_table.insert(package)
# open the distance file
with open('distance_data.csv') as package_file:
    csv_reader = csv.reader(package_file, delimiter=',')
    # add each address to the adjacency list
    for row in csv_reader:
        distance_graph.add_location(row[0])
        # create a list for the edges
        edges = []
        # the first distance index of the row containing a distance
        i = 1
        # add each edge to the list
        while i < len(distance_graph.adjacency_list):
            edges.append(row[i])
            i += 1
        # add each edge to the graph
        for edge in edges:
            print(edge)
            break


'''
for address in distance_graph.adjacency_list:

    print("vertex " + address.label)
    start_vertex = address

    for address2 in distance_graph.adjacency_list:
        next_vertex = address2
        print(distance_graph.edge_weights[(address, address2)])
'''














