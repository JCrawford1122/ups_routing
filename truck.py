# truck.py
# Author: Justin Crawford
# Student ID: 000918681
# Date: 5/17/2020
from datetime import timedelta
from distanceGraph import DistanceGraph, Vertex
from hashTable import HashTable


class Truck:
    def __init__(self, distance_graph, hash_table, clock):
        self.clock = clock
        self.packages = []
        self.delivery_route = []
        self.distance_graph = distance_graph
        self.sub_graph = DistanceGraph()
        self.hash_table = hash_table
        self.distance = 0

    # loads an individual package into a truck
    # O(N)
    def load_package(self, package_id):
        package = self.hash_table.search(package_id)
        self.packages.append(package)
        package.delivery_status = "on truck"

    # loads multiple packages into a truck
    # O(n)
    def load_packages(self, *args):
        for arg in args:
            self.load_package(arg)

    # A sub graph for packages specific to a truck
    # O(N^2)
    def create_sub_graph(self):
        # the hub
        vertex_hub = self.distance_graph.get_vertex("4001 South 700 East")
        # add the hub to the sub graph
        self.sub_graph.add_location(vertex_hub)
        # Add the needed vertices from the main graph to the sub graph
        for package in self.packages:
            for vertex in self.distance_graph.adjacency_list:
                if vertex.label == package.address:
                    # Only add the vertex once. Don't need duplicates
                    if vertex not in self.sub_graph.adjacency_list:
                        self.sub_graph.add_location(vertex)
        # Add edges to the each vertex
        for vertex in self.sub_graph.adjacency_list:
            for vertex2 in self.sub_graph.adjacency_list:
                self.sub_graph.add_directed_edge(vertex, vertex2, self.distance_graph.edge_weights[(vertex, vertex2)])

    # Route planning algorithm. Based off of nearest neighbor algorithm.
    # Starts from the a vertex and then adds the next closest vertex to the list
    # The next vertex becomes the starting vertex and then looks for the next closest
    # vertex, until the unvisited list only has 1 item left. The last item is added to
    # the end of the list. After the algorithm finishes, the truck has a sorted
    # delivery route list.
    # O(N^2)
    def shortest_path(self):
        unvisited_locations = []
        # initially add all the locations to the unvisited list
        # O(N)
        for vertex in self.sub_graph.adjacency_list:
            unvisited_locations.append(vertex)
        # set the starting location as the hub
        start_vertex = unvisited_locations[0]
        self.delivery_route.append(start_vertex)
        # The next vertex to visit
        next_vertex = None
        # variable for the shortest distance
        distance = float('inf')
        # Loop through the unvisited list until only 1 address is left
        while len(unvisited_locations) > 1:
            # find the location closest to the start address
            for vertex in unvisited_locations:
                # Don't want to go to the same address
                if vertex != start_vertex:
                    # the distance between start location and unvisited location
                    weight = float(self.sub_graph.edge_weights[(start_vertex, vertex)])
                    # if the distance is less than the current distance
                    # set the location to be the next location and set the distance
                    if weight < distance:
                        next_vertex = vertex
                        distance = weight
            # add the location to the route list
            self.delivery_route.append(next_vertex)
            unvisited_locations.pop(unvisited_locations.index(start_vertex))
            start_vertex = next_vertex
            distance = float('inf')
        # Truck should go back to the hub
        next_vertex = self.sub_graph.get_vertex("4001 South 700 East")

    # Delivers the packages from the sorted list and updates
    # the truck time, miles, and package deliver status
    # O(N^2)
    def deliver_packages(self, stop_time):
        # the first node is the hub
        hub = self.delivery_route[0]
        self.distance = 0.0
        while len(self.delivery_route) > 1:
            # Stop if the time is later than requested from user
            if self.clock < stop_time:
                # index of delivery route
                i = 0
                # get the miles between starting node and next node
                edge = self.sub_graph.edge_weights[(self.delivery_route[i], self.delivery_route[i+1])]
                # Printing the from address
                print(self.delivery_route[i].label)
                # printing the to address
                print(self.delivery_route[i + 1].label)
                # print the miles
                print(edge)
                # Calculate how much time has passed
                self.clock = self.clock + timedelta(minutes=(float(edge)/18*60))
                # Dont update packages if the time has passed requested time
                if self.clock < stop_time:
                    # deliver all packages with the address
                    for package in self.packages:
                        if package.address == self.delivery_route[i+1].label:
                            package.delivery_status = "delivered at " + str(self.clock)
                    # update the distance traveled
                    self.distance = self.distance + float(edge)
                    # remove the current node from the route
                    self.delivery_route.pop(i)
                else:
                    break
            else:
                break
        # Return to the hub after all packages are delivered
        print("returning to hub")
        # add the distance to the hub
        self.distance = self.distance + float(self.sub_graph.edge_weights[(self.delivery_route[0], hub)])




























