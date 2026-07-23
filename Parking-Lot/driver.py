from classes import Vehicle, ParkingLot, Ticket


def main():
    parking_lot = None

    while True:
        command = input().split()

        if command[0] == "exit":
            break

        parking_lot = commands(parking_lot, command)


def commands(parking_lot, command):
    if command[0] == "create_parking_lot": 
        #create_parking_lot PR1234 2 6
        #Created parking lot with 2 floors and 6 slots per floor
        parking_lot = ParkingLot(command[1], int(command[2]), int(command[3]))
        print(f"Created parking lot with {command[2]} floors and {command[3]} slots per floor")

    elif command[0] == "park_vehicle" and parking_lot:
        #park_vehicle CAR KA-01-DB-1234 black
        #Parked vehicle. Ticket ID: PR1234_1_4
        new_vehicle = Vehicle(command[1], command[2], command[3])
        ticket = parking_lot.park(new_vehicle)
        print("Parked vehicle. Ticket ID:", ticket) if ticket else print("Parking Lot Full")

    elif command[0] == "unpark_vehicle" and parking_lot:
        #unpark_vehicle PR1234_2_5
        #Unparked vehicle with Registration Number: WB-45-HO-9032 and Color: white
        #Invalid Ticket

        parking_lot_id, floor_no, slot_no = command[1].split("_")
        vehicle = parking_lot.unPark(Ticket(parking_lot_id, int(floor_no), int(slot_no)))

        if vehicle:
            print(f"Unparked vehicle with Registration Number: {vehicle.registration_number} and Color: {vehicle.color}")
        else:
            print("Invalid Ticket")

    elif command[0] == "display" and command[1] == "free_count" and parking_lot:
        #display free_count CAR
        #No. of free slots for CAR on Floor 1: 0 
        avail = parking_lot.getStatus(command[2], True)
        for i, floor in enumerate(avail):
            print(f"No. of free slots for {command[2]} on Floor {i + 1}: {len(floor)}")


    elif command[0] == "display" and command[1] == "free_slots" and parking_lot: 
        #display free_slots CAR
        #Free slots for CAR on Floor 2: 5
        avail = parking_lot.getStatus(command[2], True)
        for i, floor in enumerate(avail):
            print(f"Free slots for {command[2]} on Floor {i + 1}: {','.join(map(str, floor))}")

    elif command[0] == "display" and command[1] == "occupied_slots" and parking_lot:
        #display occupied_slots BIKE
        #Occupied slots for CAR on Floor 1: 4,5,6
        occupied = parking_lot.getStatus(command[2], False)
        for i, floor in enumerate(occupied):
            print(f"Occupied slots for {command[2]} on Floor {i + 1}: {','.join(map(str, floor))}")
    return parking_lot
    
if __name__ == "__main__":
    main()