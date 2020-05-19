# distance_data.py
# Author: Justin Crawford
# Student ID: 000918681
# Date: 5/17/2020

import csv
from distanceGraph import DistanceGraph, Vertex


class DistanceData:

    # Reads the distance data csv file into a two dimensional List
    # O(N^2)
    @staticmethod
    def get_distance_data():
        two_d_list = []
        with open('distance_data.csv') as package_file:
            csv_reader = csv.reader(package_file, delimiter=',')
            # Create a list for each row in the file
            # O(N)
            for row in csv_reader:
                distance_list = []
                # add each column of data to the list
                # O(N)
                for index in row:
                    if index == row[0]:
                        distance_list.append(Vertex(index))
                    # not adding the empty columns
                    elif index != '':
                        distance_list.append(index)
                    else:
                        break
                # add the list to the two dimensional list
                two_d_list.append(distance_list)
            return two_d_list

    # Create an undirected graph from the two dimensional list
    @staticmethod
    def load_graph():
        # Get the distance data into a two dimensional list
        two_d_list = DistanceData.get_distance_data()
        # create a graph object
        distance_graph = DistanceGraph()
        # add all the vertices to the adjacency list
        for row in two_d_list:
            distance_graph.add_location(row[0])
        counter = 0
        i = 0
        k = 1
        # add edges between all vertices
        for vertex in distance_graph.adjacency_list:
            while i < len(two_d_list):
                distance_graph.add_undirected_edge(vertex, two_d_list[i][0], two_d_list[i][k])
                i += 1
            counter += 1
            i = counter
            k += 1
        return distance_graph
