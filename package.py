# package.py
# author: Justin Crawford
# date: 05/06/2020


class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.delivery_status = 'at hub'

    def print_package(self):
        print("%2s:| %-40s %-5s %-10s %-10s %-5s %s\n" % (int(self.package_id), self.address, self.state,
                                                          self.zip_code, self.deadline, self.weight,
                                                          self.delivery_status))



