# Jourdan Farmer, ID: 011503932

import csv

class Package:

    # constructor
    # time complexity: O(1)
    # space complexity: O(1)
    def __init__(self, id, address_name, delivery_address, deadline, delivery_city, delivery_zip, weight, status):
        self.id = id
        self.address_name = address_name
        self.delivery_address = delivery_address
        self.deadline = deadline
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.weight = weight
        self.status = status

    # retains status of package
    # time complexity: O(1)
    # space complexity: O(1)
    def __str__(self):
        return f"{self.id}, {self.status}, {self.address_name}, {self.delivery_address}, {self.deadline}, {self.delivery_city}, {self.delivery_zip}, {self.weight}"

    # setter
    # time complexity: O(1)
    # space complexity: O(1)
    def set_status(self, status):
        self.status = status

    # get package status
    # time complexity: O(1)
    # space complexity: O(1)
    def get_status(self):
        return self.status

    # Returns the id of a package
    # time complexity: O(1)
    # space complexity: O(1)
    def get_id(self):
        return self.id

    # update function
    # time complexity: O(1)
    # space complexity: O(1)
    def update(self, new_delivery_address, new_address_name, new_city, new_zip, new_status):
        self.delivery_address = new_delivery_address
        self.address_name = new_address_name
        self.delivery_city = new_city
        self.delivery_zip = new_zip
        self.status = new_status
