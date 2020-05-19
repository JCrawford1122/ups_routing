# hashTable.py
# Author: Justin Crawford
# Student ID: 000918681
# Date: 5/17/2020


# HashTable class using chaining.
import csv
from package import Package


class HashTable:
    # constructor sets initial capacity of the hash table
    # O(1)
    def __init__(self, initial_capacity=40):
        # initialize the hash table
        self.table = []
        # Add empty lists to the buckets
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hashtable.
    # O(N)
    def insert(self, package):
        # get the bucket list where this item will go.
        bucket = int(package.package_id) % 40
        bucket_list = self.table[bucket]
        # insert the item to the end of the bucket list.
        bucket_list.append(package)

    # Searches the package by package_id
    # Returns a package object or None
    # key is the package id
    # O(N)
    def search(self, package_id):
        # get the bucket list where this key would be.
        bucket = int(package_id) % 40
        bucket_list = self.table[bucket]
        # search for the package id in the bucket list
        for package in bucket_list:
            # return the package or None
            if package.package_id == package_id:
                return package
            else:
                return None

    # overwriting the str method to print the table
    # O(N * M)
    def __str__(self):
        index = 0
        s = "   --------\n"
        s += "Id      Address                              State    Zip     Deadline  weight   notes   \n"
        s += "  --------\n"
        # looks through each bucket in the hash table
        # O(N)
        for bucket in self.table:
            # looks through each package in a bucket
            # O(M)
            for package in bucket:

                s += "%2s:| %-40s %-5s %-10s %-10s %-5s %-25s %s\n" % (int(package.package_id), package.address, package.state,
                                                    package.zip_code, package.deadline, package.weight, package.delivery_status, package.notes)
                index += 1
        s += "   --------"
        return s

    # Loads package data from CSV into the hash table
    # O(N)
    @staticmethod
    def load_table(graph):
        with open('package_data.csv') as package_file:
            csv_reader = csv.reader(package_file, delimiter=',')
            for row in csv_reader:
                # Create package
                package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                # Add the package to the hash table
                graph.insert(package)






