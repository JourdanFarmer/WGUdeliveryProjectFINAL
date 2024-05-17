# Jourdan Farmer, ID: 011503932

from queue import Queue
from datetime import timedelta
from HashTable import HashTable
from Package import Package
import sys
import datetime
import copy

class Truck:

    # constructor
    # complexity: O(1)
    def __init__(self, id):
        self.speed = 18
        self.id = id
        self.packages = HashTable()
        self.delivery_nodes = set()
        self.route = Queue()
        self.package_count = 0

    # truck and package count string
    # complexity: O(1)
    def __str__(self):
        return f"truck{self.id} has {self.package_count} packages remaining."

    # package getter
    # complexity: O(1)
    def get_packages(self):
        return self.packages

    # add package function
    # complexity: O(1)
    def add_package(self, package):
        self.packages.add(package.id, package)
        self.package_count += 1
        self.delivery_nodes.add(package.address_name)

    # remove package function
    # complexity: O(1)
    def remove_package(self, package):
        self.packages.remove(package)
        self.package_count -= 1
        self.delivery_nodes.discard(package.address_name)

    # nearest neighbor algorithm used to build an optimal delivery route
    # starts from home base (WGU) and then delivers to the next closest location. After final delivery, returns home.
    # time complexity: O(N^2)
    # space complexity: O(N)
    def make_route(self, node_list):
        current_node = "Western Governors University"
        self.route = Queue()
        next_node = None
        total_distance = 0
        remaining_nodes = set()
        remaining_nodes = self.delivery_nodes.copy()
        while (len(remaining_nodes) > 0):
            edges = node_list.get(current_node).edges
            shortest_distance = sys.maxsize
            for edge in edges:
                if edge.to_node in remaining_nodes:
                    if float(edge.weight) < shortest_distance:
                        shortest_distance = float(edge.weight)
                        current_node = edge.to_node
                        next_node = [
                            edge.to_node, edge.weight]
            remaining_nodes.discard(current_node)
            total_distance += shortest_distance
            self.route.put(next_node)

        # return home
        edges = node_list.get(current_node).edges
        for edge in edges:
            if edge.to_node == "Western Governors University":
                total_distance += float(edge.weight)
                next_node = [edge.to_node, edge.weight]
                break
        self.route.put(next_node)
        return(total_distance)

    # returns packages currently being delivered to target location
    # complexity: O(N)
    def get_packages_being_delivered(self, delivery_location_name):
        packages_current = list()
        # 40 total packages to check
        for i in range(1, 41):
            candidate_package = self.packages.get(str(i))
            if candidate_package != None:
                if candidate_package.address_name == delivery_location_name:
                    packages_current.append(candidate_package.id)
        return packages_current

    # returns packages headed got target location.
    # complexity: O(N)
    def get_packages_on_board(self):
        all_packages = list()
        for i in range(1, 41):
            candidate_package = self.packages.get(str(i))
            if candidate_package != None:
                all_packages.append(candidate_package.id)
        return all_packages

    # delivery function
    # complexity: O(N)
    def deliver_packages(self, truck_departure_time, package_ingest, package_status, package_9_status):
        return_time = None
        travel_distance = 0
        request_to_update_9 = False

        if ("delivered" not in package_status):
            package_status["delivered"] = set()

        if ("delivered times" not in package_status):
            package_status["delivered times"] = dict()

        if ("start_transit" not in package_status):
            package_status["start_transit"] = dict()

        if ("hub departure" not in package_status):
            package_status["hub departure"] = dict()

        for i in range(1, 41):
            temporary_package = self.packages.get(str(i))
            if (temporary_package != None):
                package_status["hub departure"][int(
                    temporary_package.get_id())] = truck_departure_time.strftime("%H:%M:%S")
        start_transit = truck_departure_time.strftime("%H:%M:%S")
        while (self.route.qsize() > 0):

            delivery_next = self.route.get()

            packages_current = self.get_packages_being_delivered(
                delivery_next[0])

            travel_distance += float(delivery_next[1])

            # drive time
            drive_time = travel_distance / self.speed

            # current time
            current_time = truck_departure_time + \
                timedelta(hours=drive_time)

            # makes time object to update package #9
            ten_twenty_am = datetime.datetime(2021, 7, 1, 10, 20, 0, 0)

            # print progress
            if (delivery_next[0] == 'Western Governors University'):
                print("\t" + current_time.strftime("%H:%M:%S") + ": TRUCK" +
                      self.id + " returning to: '" + delivery_next[0] + "'\n")
            else:
                print("\t" + current_time.strftime("%H:%M:%S") + ": TRUCK" + self.id +
                      " delivering package to: '" + delivery_next[0] + "'")

            if (current_time >= ten_twenty_am and not package_9_status and self.id == "1 trip2" and not request_to_update_9):
                print("")
                print(f"\tan update is required for package #9")
                print(f"\twould you like to make the update? input: 'yes' or 'no'")
                print("")

                answer = input(">")

                # corrects package 9
                while answer != "yes" and answer != "no":
                    print(f"\tinvalid input")
                    print(f"\tplease type: 'yes' or 'no'")
                    answer = input(">")

                if answer == "yes":
                    package_ingest.package_hash.add("9", Package(
                        "9", "Third District Juvenile Court", "410 S State St", "EOD", "Salt Lake City", "84111", "2", "in transit"))
                    print(f"\tpackage #9 has been updated to: 410 S State St., Salt Lake City, UT 84111")
                    print("")
                    package_9_status = True
                elif answer == "no":
                    package_ingest.package_hash.add("9", Package(
                        "9", "Council Hall", "300 State St", "EOD", "Salt Lake City", "84103", "2", "Wrong address listed"))
                    request_to_update_9 = True
                    print("")

            onboard_packages = self.get_packages_on_board()
            # records  data for playback
            if package_status == None:
                package_status = dict()
            for pack in packages_current:
                time_translated = current_time.strftime("%H:%M:%S")
                if not time_translated in package_status:
                    package_status[time_translated] = dict()
                temporary_package = self.packages.get(pack)

                # records delivered times
                temporary_package.set_status("delivered")
                package_status["delivered times"][int(
                    temporary_package.get_id())] = time_translated

                # records in transit times
                package_status["start_transit"][int(
                    temporary_package.get_id())] = start_transit

                # updates when delivered
                self.packages.add(pack, temporary_package)

                # adds packages to package_status
                package_hash_key = str(temporary_package.get_id())
                package_status[time_translated][package_hash_key] = copy.deepcopy(
                    temporary_package)

                if str(i) not in packages_current and temporary_package != None and temporary_package.get_status() != "delivered":

                    # maintains status
                    temporary_package.set_status("in transit")
                    package_status[time_translated][temporary_package.get_id()] = copy.deepcopy(
                        temporary_package)
                    package_status["delivered times"][int(temporary_package.get_id(
                    ))] = time_translated

                # updates delivered status
                elif temporary_package != None and (temporary_package.get_status() == "delivered" or str(temporary_package.get_id()) in package_status["delivered"]):

                    package_status[time_translated][temporary_package.get_id()] = copy.deepcopy(
                        temporary_package)

                    # records ID of delivered packages
                    package_status["delivered"].add(
                        temporary_package.get_id())

                # finds unloaded packages
                elif temporary_package != None and temporary_package.get_status() != "delivered" and temporary_package.get_status() != "in transit":
                    print("At Amazon Facility: " + temporary_package.get_id)

            # updates status
            for i in range(1, 41):
                temporary_package = package_ingest.package_hash.get(str(i))

                # added measure to make sure all delivered packages are marked as such.
                if (i in package_status["delivered"]):
                    package_status[time_translated][temporary_package.get_id()] = copy.deepcopy(
                        temporary_package)
            start_transit = time_translated

        return_time = truck_departure_time + timedelta(hours=drive_time)

        return[return_time, drive_time, travel_distance, package_9_status]
