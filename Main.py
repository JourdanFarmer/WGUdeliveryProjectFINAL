# Jourdan Farmer, ID: 011503932

from PackageIngest import PackageIngest
from Graph import *
from Truck import Truck
from datetime import timedelta
from operator import itemgetter
from queue import Queue
import datetime
import time
import collections

# retains package status
package_status = dict(dict())

# initialize graph
g = Graph()

# initialize packages
package_ingest = PackageIngest()


# load truck 1 and calculate route
# complexity: O(n)
def initialize_truck1():
    truck1.delivery_nodes.clear()
    truck1.add_package(package_ingest.get_package_by_id('1'))
    truck1.add_package(package_ingest.get_package_by_id('29'))
    truck1.add_package(package_ingest.get_package_by_id('7'))
    truck1.add_package(package_ingest.get_package_by_id('30'))
    truck1.add_package(package_ingest.get_package_by_id('8'))
    truck1.add_package(package_ingest.get_package_by_id('34'))
    truck1.add_package(package_ingest.get_package_by_id('40'))
    truck1.add_package(package_ingest.get_package_by_id('13'))
    truck1.add_package(package_ingest.get_package_by_id('39'))
    truck1.add_package(package_ingest.get_package_by_id('14'))
    truck1.add_package(package_ingest.get_package_by_id('15'))
    truck1.add_package(package_ingest.get_package_by_id('16'))
    truck1.add_package(package_ingest.get_package_by_id('19'))
    truck1.add_package(package_ingest.get_package_by_id('20'))
    truck1.add_package(package_ingest.get_package_by_id('37'))
    truck1.make_route(g.adjacency_matrix)


# load truck 1, trip 2 and calculate route
# complexity: O(n)
def initialize_truck1_trip2():
    truck1_trip2.delivery_nodes.clear()
    truck1_trip2.add_package(package_ingest.get_package_by_id('6'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('5'))

    truck1_trip2.add_package(package_ingest.get_package_by_id('21'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('4'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('24'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('23'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('26'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('22'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('10'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('11'))
    truck1_trip2.add_package(package_ingest.get_package_by_id('31'))
    truck1_trip2.make_route(g.adjacency_matrix)


# load truck 2 and calculate route
# complexity: O(n)
def initialize_truck2():
    truck2.delivery_nodes.clear()
    truck2.add_package(package_ingest.get_package_by_id('17'))
    truck2.add_package(package_ingest.get_package_by_id('12'))
    truck2.add_package(package_ingest.get_package_by_id('25'))
    truck2.add_package(package_ingest.get_package_by_id('28'))
    truck2.add_package(package_ingest.get_package_by_id('32'))
    truck2.add_package(package_ingest.get_package_by_id('3'))
    truck2.add_package(package_ingest.get_package_by_id('18'))
    truck2.add_package(package_ingest.get_package_by_id('36'))
    truck2.add_package(package_ingest.get_package_by_id('38'))
    truck2.add_package(package_ingest.get_package_by_id('27'))
    truck2.add_package(package_ingest.get_package_by_id('35'))
    truck2.add_package(package_ingest.get_package_by_id('2'))
    truck2.add_package(package_ingest.get_package_by_id('33'))
    truck2.add_package(package_ingest.get_package_by_id('9'))
    truck2.make_route(g.adjacency_matrix)


# initialize_graph
# complexity: O(n^2)
def initialize_graph():
    g.initialize_location_name()
    g.initialize_location_distance()
    g.initialize_nodes_hashtable()


# initialize trucks and ids
initialize_graph()
truck1 = Truck(" 1")
truck1_trip2 = Truck(" 1, TRIP 2")
truck2 = Truck(" 2")
initialize_truck1()
initialize_truck1_trip2()
initialize_truck2()

# track package 9 - the problematic one
package_9_has_been_updated = False


# delivery program init
# complexity: O(n)
def delivery_program(package_status):
    eight_am = datetime.datetime(2021, 7, 1, 8, 0, 0, 0)
    nine_oh_five = datetime.datetime(2021, 7, 1, 9, 5, 0, 0)
    ten_twenty = datetime.datetime(2021, 7, 1, 10, 20, 0, 0)

    # deliver truck 1
    initialize_truck1()
    truck1_return_data = truck1.deliver_packages(
        eight_am, package_ingest, package_status, package_9_has_been_updated)

    initialize_truck1_trip2()
    truck1_trip2_return_data = truck1_trip2.deliver_packages(
        truck1_return_data[0], package_ingest, package_status, truck1_return_data[3])

    # deliver truck 2
    initialize_truck2()
    truck2_return_data = truck2.deliver_packages(
        ten_twenty, package_ingest, package_status, truck1_trip2_return_data[3])

    start = eight_am
    finish = truck2_return_data[0]
    finish = finish - start
    hours = finish.seconds // 3600
    minutes = (finish.seconds % 3600) // 60
    total_trip_time = str(hours) + ":" + str(minutes)

    total_time_all_packages = round(
        float(truck2_return_data[1] + truck1_trip2_return_data[1]), 2)
    total_time_all_packages = datetime.datetime(
        2021, 7, 1, 0, 0, 0, 0) + timedelta(hours=total_time_all_packages)

    total_mileage = truck1_return_data[2] + \
        truck1_trip2_return_data[2] + truck2_return_data[2]
    print("\tDELIVERIES COMPLETED!")
    print("")
    print("\tTRUCK 1 DATA: ----")
    print(f"\tDEPARTURE TIME: {eight_am}")
    print(f"\tCOMPLETION TIME: {truck1_return_data[0]}")
    print(
        f"\tTRAVEL TIME: {round(float(truck1_return_data[1]),2)} hours")
    print(
        f"\tTRAVEL DISTANCE: {round(float(truck1_return_data[2]),2)} miles")
    print("")
    print("\tTRUCK 1- TRIP 2 - DATA: ----")
    print(f"\tDEPARTURE TIME: {truck1_return_data[0]}")
    print(f"\tCOMPLETION TIME: {truck1_trip2_return_data[0]}")
    print(
        f"\tTRAVEL TIME: {round(float(truck1_trip2_return_data[1]),2)} hours")
    print(
        f"\tTRAVEL DISTANCE: {round(float(truck1_trip2_return_data[2]),2)} miles")
    print(f"")
    print("\tTRUCK 2 DATA: ----")
    print(f"\tDEPARTURE TIME: {ten_twenty}")
    print(f"\tCOMPLETION TIME: {truck2_return_data[0]}")
    print(
        f"\tTRAVEL TIME: {round(float(truck2_return_data[1]),2)} HOURS")
    print(
        f"\tTRAVEL DISTANCE: {round(float(truck2_return_data[2]),2)} MILES")
    print(f"")
    print(f"\tDISTANCE BY ALL TRUCKS: {round(float(total_mileage),2)} miles")
    print(f"\tDELIVERY TIME: {hours} HOURS, AND {minutes} MINUTES")
    initialize_graph()
    initialize_truck1()
    initialize_truck1_trip2()
    initialize_truck2()

    package_status = list()

# complexity: O(n)
user_input = ""
while (user_input != "begin"):
    print("")

    print("\tWelcome to Amazon package delivery! Please select an option below:")
    print("")
    print("\tbegin - BEGIN DELIVERY AND SEARCH ITEM FUNCTION")
    print("\tquit - QUIT")
    print("")
    package_status.clear()
    user_input = input(">").lower()

    if (user_input == "begin"):
        print("")
        print("\tSTARTING DELIVERY!")
        print("")
        delivery_program(package_status)
        print("")
        while (user_input != "package" and user_input != "back"):
            print("\tWhat would you like to do next?")
            print("")
            print("\tpackage - PACKAGE INFORMATION LOOKUP")
            print("\tback - BACK TO MAIN MENU")
            print("")
            user_input = input(">").lower()

            selected_time = None
            if (user_input == "package"):
                while (selected_time == None):

                    print("")
                    while True:
                        print("\tInput a package time. i.e.:" + " 12:00")
                        print("")
                        selected_time = input(">").lower()
                        try:
                            if (time.strptime(selected_time, "%H:%M")):

                                selected_time = time.strptime(
                                    selected_time, "%H:%M")

                                break
                        except ValueError:
                            print("\tINVALID INPUT!")
                            continue

                    print("")
                    print("\tWhat are you interested in searching by?")
                    print("")
                    print(
                        f'\tall <- present all info {time.strftime("%H:%M", selected_time)}')
                    print("\tid <- query package id")
                    print("\taddress <- query package address")
                    print("\tdeadline <- query package deadline")
                    print("\tcity <- query package city")
                    print("\tzip <- query package zip")
                    print("\tweight <- query package weight")
                    print("\tstatus <- query package status")
                    print("")
                    input_choice = input(">")

                    while (input_choice != "all" and input_choice != "id" and input_choice != "address" and input_choice != "deadline" and input_choice != "city" and input_choice != "zip" and input_choice != "weight" and input_choice != "status"):
                        print("\tINVALID INPUT!")
                        print("")
                        print("\tHow would you like to query packages?")
                        print("")
                        print(
                            f"\tall <- present all info {package_status[int(user_input)][0]}")
                        print("\tid <- query package id")
                        print("\taddress <- query package address")
                        print("\tdeadline <- query package deadline")
                        print("\tcity <- query package city")
                        print("\tzip <- query package zip")
                        print("\tweight <- query package weight")
                        print("\tstatus <- query package status")
                        print("")
                        input_choice = input(">")

                    # query all
                    if (input_choice == "all"):

                        # retains packages sorted through
                        sorted_packages = dict()

                        for package_id in sorted(package_status["delivered times"]):
                            if (time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status["delivered times"][package_id]
                                package_ingest.get_package_by_id(str(package_id)).set_status(
                                    'delivered (' + delivered_time + ')')
                                sorted_packages[int(package_id)] = package_ingest.get_package_by_id(
                                    str(package_id))

                            elif ((time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") <= selected_time)):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('in progress')
                                sorted_packages[int(package_id)] = package_ingest.get_package_by_id(
                                    str(package_id))

                            elif (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") > selected_time):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('package facility')
                                sorted_packages[int(package_id)] = package_ingest.get_package_by_id(
                                    str(package_id))

                        print("")
                        print(
                            f'\tAll statuses at: {time.strftime("%H:%M:%S", selected_time)}')

                        # Output all items status
                        for key in sorted_packages:
                            if ("delivered" in str(sorted_packages[key])):
                                print("\t"+str(sorted_packages[key]))
                            elif ("in progress" in str(sorted_packages[key])):
                                print("\t"+str(sorted_packages[key]))
                            elif ("packing facility" in str(sorted_packages[key])):
                                print("\t"+str(sorted_packages[key]))

                        user_input = "back"

                    # query package id
                    elif (input_choice == "id"):

                        print("")
                        print("\tEnter package id. i.e.:" + " 9")
                        print("")
                        target_id = input(">")
                        print("")
                        sorted_packages = dict()

                        for package_id in sorted(package_status["delivered times"]):
                            if (time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status["delivered times"][package_id]
                                package_ingest.get_package_by_id(str(package_id)).set_status(
                                    'delivered (' + delivered_time + ')')

                            elif ((time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") <= selected_time)):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('in progress')

                            elif (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") > selected_time):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('packing facility')

                            if (str(package_id) == target_id):
                                sorted_packages[int(package_id)] = package_ingest.get_package_by_id(
                                    str(package_id))

                        print("")
                        print(
                            f'\titem ({target_id}) at (' + time.strftime("%H:%M:%S", selected_time) + ')')
                        if ("delivered" in str(sorted_packages[int(target_id)])):
                            print("\t"+str(sorted_packages[int(target_id)]))
                        elif ("in progress" in str(sorted_packages[int(target_id)])):
                            print("\t"+str(sorted_packages[int(target_id)]))
                        elif ("packing facility" in str(sorted_packages[int(target_id)])):
                            print("\t"+str(sorted_packages[int(target_id)]))

                        user_input = "back"

                    # query address
                    elif (input_choice == "address"):
                        print("")
                        print("\tInput target address - i.e.: 4300 S 1300 E")
                        print("")
                        target_address = input(">")
                        print("")

                        sorted_packages = dict()

                        for package_id in sorted(package_status["delivered times"]):
                            if (time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status["delivered times"][package_id]
                                package_ingest.get_package_by_id(str(package_id)).set_status(
                                    'delivered (' + delivered_time + ')')

                            elif ((time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") <= selected_time)):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('in progress')

                            elif (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") > selected_time):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('packing facility')

                            if (str(package_id) == target_address):
                                sorted_packages[int(package_id)] = package_ingest.get_package_by_id(
                                    str(package_id))

                        print("")
                        print(
                            f'\tItem with address ({target_address}) at (' + time.strftime("%H:%M:%S", selected_time) + ')')
                        print("")

                        sorted_packages = package_ingest.get_package_by_address(
                            target_address)
                        for package in sorted_packages:
                            if ("delivered" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("in progress" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("packing facility" in str(package)):
                                print("\t" +
                                      str(package))

                        user_input = "back"

                    # query deadline
                    elif (input_choice == "deadline"):
                        print("")
                        print("\tInput item deadline. i.e.: 10:30 AM")
                        print("")
                        target_deadline = input(">")
                        print("")

                        sorted_packages = dict()

                        for package_id in sorted(package_status["delivered times"]):
                            if (time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status["delivered times"][package_id]
                                package_ingest.get_package_by_id(str(package_id)).set_status(
                                    'delivered (' + delivered_time + ')')

                            elif ((time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") <= selected_time)):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('in progress')

                            elif (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") > selected_time):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('packing facility')

                        print("")
                        print(
                            f'\titems of deadline ({target_deadline}) at (' + time.strftime("%H:%M:%S", selected_time) + ')')
                        print("")

                        # print packages based on address
                        sorted_packages = package_ingest.get_package_by_deadline(
                            target_deadline)
                        for package in sorted_packages:
                            if ("delivered" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("in progress" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("packing facility" in str(package)):
                                print("\t" +
                                      str(package))

                        user_input = "back"

                    # query city
                    elif (input_choice == "city"):
                        print("")
                        print("\tInput delivery city. i.e.: Salt Lake City")
                        print("")
                        target_city = input(">")
                        print("")

                        # retains delivered items
                        sorted_packages = dict()

                        for package_id in sorted(package_status["delivered times"]):
                            if (time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status["delivered times"][package_id]
                                package_ingest.get_package_by_id(str(package_id)).set_status(
                                    'delivered (' + delivered_time + ')')

                            elif ((time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") <= selected_time)):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('in progress')

                            elif (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") > selected_time):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('packing facility')

                        print("")
                        print(
                            f'\titems being delivered to ({target_city}) at (' + time.strftime("%H:%M:%S", selected_time) + ')')
                        print("")

                        # prints items and status at address
                        sorted_packages = package_ingest.get_package_by_city(
                            target_city)
                        for package in sorted_packages:
                            if ("delivered" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("in progress" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("packing facility" in str(package)):
                                print("\t" +
                                      str(package))

                        user_input = "back"

                    # query zip
                    elif (input_choice == "zip"):
                        print("")
                        print("\tInput delivery zip code. i.e.: 84117")
                        print("")
                        target_zip = input(">")
                        print("")

                        # retains delivered items
                        sorted_packages = dict()

                        for package_id in sorted(package_status["delivered times"]):
                            if (time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status["delivered times"][package_id]
                                package_ingest.get_package_by_id(str(package_id)).set_status(
                                    'delivered (' + delivered_time + ')')

                            elif ((time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") <= selected_time)):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('in progress')

                            elif (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") > selected_time):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('packing facility')

                        print("")
                        print(
                            f'\tbeing delivered to ({target_zip}) at (' + time.strftime("%H:%M:%S", selected_time) + ')')
                        print("")

                        # print status
                        sorted_packages = package_ingest.get_package_by_zip(
                            target_zip)
                        for package in sorted_packages:
                            if ("delivered" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("in progress" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("packing facility" in str(package)):
                                print("\t" +
                                      str(package))

                        user_input = "back"

                    elif (input_choice == "weight"):
                        print("")
                        print("\tInput weight. i.e.: 4")
                        print("")
                        target_weight = input(">")
                        print("")

                        # retains items delivered
                        sorted_packages = dict()

                        for package_id in sorted(package_status["delivered times"]):
                            if (time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status["delivered times"][package_id]
                                package_ingest.get_package_by_id(str(package_id)).set_status(
                                    'delivered (' + delivered_time + ')')

                            elif ((time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") <= selected_time)):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('in progress')

                            elif (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") > selected_time):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('packing facility')

                        print("")
                        print(
                            f'\titems that weigh ({target_weight}) at (' + time.strftime("%H:%M:%S", selected_time) + ')')
                        print("")

                        # output status
                        sorted_packages = package_ingest.get_package_by_weight(
                            target_weight)
                        for package in sorted_packages:
                            if ("delivered" in str(package)):
                                print(str(package))
                            elif ("in progress" in str(package)):
                                print(str(package))
                            elif ("packing facility" in str(package)):
                                print(str(package))

                        user_input = "back"

                    # query status
                    elif (input_choice == "status"):
                        print("")
                        print("\tInput desired status. i.e.: delivered, in progress, or packing facility")
                        print("")
                        target_status = input(">")
                        print("")

                        # retains delivered status
                        sorted_packages = dict()

                        for package_id in sorted(package_status["delivered times"]):
                            if (time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status["delivered times"][package_id]
                                package_ingest.get_package_by_id(str(package_id)).set_status(
                                    'delivered')

                            elif ((time.strptime(package_status["delivered times"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") <= selected_time)):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('in progress')

                            elif (time.strptime(package_status["hub departure"][package_id], "%H:%M:%S") > selected_time):
                                package_ingest.get_package_by_id(
                                    str(package_id)).set_status('packing facility')

                        print("")
                        print(
                            f'\titems of status ({target_status}) at (' + time.strftime("%H:%M:%S", selected_time) + ')')
                        print("")

                        # output by status
                        sorted_packages = package_ingest.get_package_by_status(
                            target_status)
                        for package in sorted_packages:
                            if ("delivered" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("in progress" in str(package)):
                                print("\t" +
                                      str(package))
                            elif ("packing facility" in str(package)):
                                print("\t" +
                                      str(package))

                        user_input = "back"
