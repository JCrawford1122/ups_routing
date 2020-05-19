# main.py
# Author: Justin Crawford
# Student ID: 000918681
# Date: 5/17/2020
import csv
import operator
import printMenu
from datetime import timedelta
from location import Location
from distanceGraph import DistanceGraph, Vertex
from package import Package
from hashTable import HashTable
from truck import Truck
from distance_data import DistanceData
import utility

printMenu.print_menu()
menu = True
while menu:
    # truck1 start time
    delta_1 = timedelta(hours=8)
    # truck2 start time
    delta_2 = timedelta(hours=9, minutes=5)
    # truck3 start time
    delta_3 = timedelta(hours=10, minutes=20)
    # Create the hash table object
    hash_table = HashTable()
    # load the hash table
    HashTable.load_table(hash_table)
    # create and load the distance graph
    distance_graph = DistanceData.load_graph()
    # instantiate truck1
    truck1 = Truck(distance_graph, hash_table, delta_1)
    # instantiate truck2
    truck2 = Truck(distance_graph, hash_table, delta_2)
    # instantiate truck3
    truck3 = Truck(distance_graph, hash_table, delta_3)
    # load packages on truck1
    truck1.load_packages("4", "7", "13", "14", "15", "16", "19", "20", "27", "29", "34", "40", "23", "11", "17")
    # make a sub-graph of the package locations
    truck1.create_sub_graph()
    # sort the packages on the truck
    truck1.shortest_path()
    # load the packages on truck 2.
    # Includes required packages (3, 18, 36, 38)
    truck2.load_packages("1", "3", "6", "18", "25", "26", "31", "32", "36", "37", "38", "30")
    # Create sub graph for truck 2
    truck2.create_sub_graph()
    # sort the packages on truck 2
    truck2.shortest_path()
    # load remaining packages on truck 3
    truck3.load_packages("2", "5", "8", "9", "10", "12", "21", "22",  "24", "28", "33", "35", "39")
    # create sub graph for truck 3
    truck3.create_sub_graph()
    # sort the packages on truck 3
    truck3.shortest_path()
    # get the users menu selection
    user_input = input()
    # user wants to view a package at a certain time
    if user_input == "1":
        # get the package id from the user
        package_id = input("Enter a package ID: ")
        # get the time from the user
        package_time = input("Enter a time (HH:MM:SS)  ")
        # convert the time to a timedelta
        delta = utility.get_time_stamp(package_time)
        # run the trucks until the specified time
        truck1.deliver_packages(delta)
        truck2.deliver_packages(delta)
        truck3.deliver_packages(delta)
        # Print the package fields
        Package.print_package(hash_table.search(package_id))
        # display the menu
        printMenu.print_menu()
    # the user wants all of the packages at a specified time
    elif user_input == "2":
        # get the time from the user
        timestamp = input("Enter a time (HH:MM:SS) ")
        # convert the time to a timedelta
        delta = utility.get_time_stamp(timestamp)
        # run the trucks until the specified time
        truck1.deliver_packages(delta)
        # Truck leaves at 9:05
        truck2.deliver_packages(delta)
        # Driver1 takes truck3 after return time
        # Truck leaves at 10:20
        truck3.deliver_packages(delta)
        # Display the hash table at the input time
        print(hash_table)
        # print individual truck distances
        print("Truck1 traveled " + str(truck1.distance))
        print("Truck2 traveled " + str(truck2.distance))
        print("truck3 traveled " + str(truck3.distance))
        # print the total distance of all trucks
        print("total distance traveled " + str(truck1.distance + truck2.distance + truck3.distance))
        # display the menu
        printMenu.print_menu()
    elif user_input == "3":
        delta = timedelta(hours=17, minutes=0, seconds=0)
        # run the trucks until the specified time
        truck1.deliver_packages(delta)
        # Truck leaves at 9:05
        truck2.deliver_packages(delta)
        # Driver1 takes truck3 after return time
        # Truck leaves at 10:20
        truck3.deliver_packages(delta)
        # Display the hash table at the input time
        print(hash_table)
        # print individual truck distances
        print("Truck1 traveled " + str(truck1.distance))
        print("Truck2 traveled " + str(truck2.distance))
        print("truck3 traveled " + str(truck3.distance))
        # print the total distance of all trucks
        print("total distance traveled " + str(truck1.distance + truck2.distance + truck3.distance))
        # display the menu
        printMenu.print_menu()
    elif user_input == "0":
        menu = False
    # display the menu after invalid selections
    else:
        printMenu.print_menu()
























