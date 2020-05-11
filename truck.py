# truck.py
# author: Justin Crawford
# date : 05/07/2020
from distanceGraph import DistanceGraph


class Truck:
    def __init__(self, distance_graph):
        self.packages = []
        self.distance_graph = distance_graph
        self.delivery_route = []

    def load_package(self, package):
        self.packages.append(package)

    def calculate_route(self, current_location, destination):
        pass

    def get_distance(self):
        pass
