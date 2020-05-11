# hashTable.py
# author: Justin Crawford
# date: 05/06/2020


# HashTable class using chaining.
class HashTable:
    # constructor sets initial capacity of the hash table
    def __init__(self, initial_capacity=40):
        # initialize the hash table
        self.table = []

        # Add empty lists to the buckets
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hashtable.
    def insert(self, package):

        # get the bucket list where this item will go.
        bucket = int(package.package_id) % 40
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(package)

    # Searches the package by package_id
    # Returns a package object or None
    # key is the package id
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

    def __str__(self):
        index = 0
        s = "   --------\n"
        s += "Id      Address                              State    Zip     Deadline  weight   notes   \n"
        s += "  --------\n"
        for bucket in self.table:
            for package in bucket:

                s += "%2s:| %-40s %-5s %-10s %-10s %-5s %s\n" % (int(package.package_id), package.address, package.state,
                                                    package.zip_code, package.deadline, package.weight, package.notes)
                index += 1
        s += "   --------"
        return s







