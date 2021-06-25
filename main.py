parking_space = []
no_of_parking_spaces = 0


def init():  # creating the parking lot with the required parking space
    for i in range(no_of_parking_spaces):
        parking_space.append(["empty", "empty"])
    print("Created parking of " + str(no_of_parking_spaces) + " slots")


def populate_parking(registration_num, age):  # populating the parking lot as cars enter it
    assigned_parking_space = False
    for i in range(no_of_parking_spaces):
        if parking_space[i][0] == "empty":   # populating the empty slots first if any car has left
            parking_space[i][0] = registration_num
            parking_space[i][1] = age
            print("Car with vehicle registration number \"" + parking_space[i][
                0] + "\" has been parked at slot number " + str(i + 1))
            assigned_parking_space = True  # if parking is not assigned then parking lot if full
            break
    if not assigned_parking_space:
        print("Parking space not assigned as the parking limit has been reached. Please wait till someone leaves.")


def empty_slot(slot_no):
    if slot_no > no_of_parking_spaces:  # if you have entered invalid slot number
        print("The limit of number of slots is " + str(no_of_parking_spaces))
    print("Slot number " + str(slot_no + 1) + "vacated, the car with vehicle registration number \"" +
          parking_space[slot_no][0] + "\" left the space, the driver of the car was of age " + str(
        parking_space[slot_no][1]))
    parking_space[slot_no] = ["empty", "empty"]


def get_reg_no_by_age(age):
    found = False
    vehicle_reg = ""
    for i in range(no_of_parking_spaces):
        if parking_space[i][1] == age:
            vehicle_reg += parking_space[i][0] + ","
            found = True
    if found:
        print(vehicle_reg[:len(vehicle_reg) - 1])  # removing the last comma
    else:
        print("No car with the driver as age " + str(age) + " is parked currently in the lot")


def get_slot_no_from_age(age):
    found = False
    slot = ""
    for i in range(no_of_parking_spaces):
        if parking_space[i][1] == age:
            slot += str(i + 1) + ","
            found = True
    if found:
        print(slot[:len(slot) - 1])
    else:
        print("No car with the driver as age " + str(age) + " is parked currently in the lot")


def get_slot_from_registrationnum(reg):
    found = False
    slot = ""
    for i in range(no_of_parking_spaces):
        if parking_space[i][0] == reg:
            slot += str(i + 1) + ","
            found = True
    if found:
        print(slot[:len(slot) - 1])
    else:
        print("No car with the registration number \"" + reg + "\" is currently parked in the lot")


def take_input():  # processing the input
    with open("testing.txt") as f:
        lines = f.readlines()  # reading the input line by line
    global no_of_parking_spaces
    if lines == "":
        print("Input is empty")
    if lines[0] != "Create_parking_lot":
        print("Cannot assign parking space without creating a lot")
    no_of_parking_spaces = int(lines[0].split()[1]) - 1  # assigning the number of parking space
    if no_of_parking_spaces <= 0:
        print("Invalid input of number of parking spaces, please enter positive value")
    init()  # assigning slots
    for line in lines: # line by line traversal
        current_condition = line.split()
        if current_condition[0].lower() == "park":  # can be in lower case
            populate_parking(current_condition[1], current_condition[3])
        elif current_condition[0] == "Slot_numbers_for_driver_of_age":
            get_slot_no_from_age(current_condition[1])
        elif current_condition[0] == "Slot_number_for_car_with_number":
            get_slot_from_registrationnum(current_condition[1])
        elif current_condition[0].lower() == "leave":  # can be in lower case
            empty_slot(int(current_condition[1]) - 1)
        elif current_condition[0] == "Vehicle_registration_number_for_driver_of_age":
            get_reg_no_by_age(int(current_condition[1]))


if __name__ == "__main__":
    take_input()
    