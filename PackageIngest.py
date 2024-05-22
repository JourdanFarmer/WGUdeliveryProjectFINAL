# Jourdan Farmer, ID: 011503932

import csv
from Package import Package
from HashTable import HashTable

class PackageIngest:

    # constructor
    # complexity: O(1)
    def __init__(self):
        self.total_packages = 40
        self.packages = {}
        self.package_hash = HashTable()
        self.csv_to_package_table()

    # returns package count
    # complexity: O(1)
    def __len__(self):
        return len(self.packages)

    # returns iterator object
    # complexity: O(1)
    def __iter__(self):
        return iter([package for id, package in self.packages.items()])

    # insert function
    # complexity: O(1)
    def insert(self, item):
        self.packages[item.id] = item

    # makes hashtable based on distance_names.csv and packages.csv
    # complexity: O(n)
    def csv_to_package_table(self):
        location_address_to_names = HashTable()

        with open("./data/distance_names.csv") as file:
            names_reader = csv.reader(file)
            raw_distance_names = list(names_reader)
            for entry in raw_distance_names:
                location_address_to_names.add(entry[2], entry[1])

        with open("./data/packages.csv") as file:
            package_reader = csv.reader(file)
            package_csv = list(package_reader)

        for entry in package_csv:
            if len(entry) > 1:
                self.insert(Package(id=entry[0], address_name=location_address_to_names.get(entry[1]), delivery_address=entry[1], deadline=entry[5],
                                    delivery_city=entry[2], delivery_zip=entry[4], weight=entry[6], status="package facility"))
                self.package_hash.add(entry[0], Package(id=entry[0], address_name=location_address_to_names.get(entry[1]), delivery_address=entry[1], deadline=entry[5],
                                                               delivery_city=entry[2], delivery_zip=entry[4], weight=entry[6], status="package facility"))

    # everything under are get functions per each variable

    # complexity: O(1)
    # get package by ID
    def get_package_by_id(self, id):
        return self.package_hash.get(id)

    # complexity: O(n)
    # get package by address
    def get_package_by_address(self, address):
        packages = list()
        for id in range(1, self.total_packages + 1):
            package = self.get_package_by_id(str(id))
            if (package.delivery_address == address):
                packages.append(package)
        return packages

    # complexity: O(n)
    # get package by city
    def get_package_by_city(self, city):
        packages = list()
        for id in range(1, self.total_packages + 1):
            package = self.get_package_by_id(str(id))
            if (package.delivery_city == city):
                packages.append(package)
        return packages

    # complexity: O(n)
    # get package by deadline
    def get_package_by_deadline(self, deadline):
        packages = list()
        for id in range(1, self.total_packages + 1):
            package = self.get_package_by_id(str(id))
            if (package.deadline == deadline):
                packages.append(package)
        return packages

    # complexity: O(n)
    # get package by zip
    def get_package_by_zip(self, zip):
        packages = list()
        for id in range(1, self.total_packages + 1):
            package = self.get_package_by_id(str(id))
            if (package.delivery_zip == zip):
                packages.append(package)
        return packages

    # complexity: O(n)
    # get package by weight
    def get_package_by_weight(self, weight):
        packages = list()
        for id in range(1, self.total_packages + 1):
            package = self.get_package_by_id(str(id))
            if (package.weight == weight):
                packages.append(package)
        return packages

    # complexity: O(n)
    # get package by status
    def get_package_by_status(self, status):
        packages = list()
        for id in range(1, self.total_packages + 1):
            package = self.get_package_by_id(str(id))
            if (package.status == status):
                packages.append(package)
        return packages
