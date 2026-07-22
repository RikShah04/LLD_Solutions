class Vehicle:
    def __init__(self, type, registration_number, color):
        self.type = type
        self.registration_number = registration_number
        self.color = color

class ParkingFloor:
    def __init__(self, no_of_slots_per_floor):
        self.truck = None
        self.bikes = [None, None]
        self.cars = [None] * (no_of_slots_per_floor - 3)

    def park(self, vehicle):

        avail = self.checkStatus(vehicle.type, True)

        if not avail:
            return -1

        if vehicle.type == "TRUCK":
            self.truck = vehicle
            return 1
        
        elif vehicle.type == "BIKE":
            if not self.bikes[0]:
                self.bikes[0] = vehicle
                return 2
            else:
                 self.bikes[1] = vehicle
                 return 3
            
        elif vehicle.type == "CAR":
            for i in range(len(self.cars)):
                if not self.cars[i]:
                    self.cars[i] = vehicle
                    return i + 4
                
    def checkStatus(self, type, status):
        avail = []
        if type == "TRUCK":
            avail.append(1) if (self.truck is None) == status else 0
        
        elif type == "BIKE":
            if (self.bikes[0] is None) == status:
                avail.append(2) 
            if (self.bikes[1] is None) == status:
                avail.append(3) 
            
        elif type == "CAR":
            for i, car in enumerate(self.cars):
                if (car is None) == status:
                    avail.append(i + 4)

        return avail

    def unPark(self, slot):
        if slot == 1:
            unParked = self.truck
            self.truck = None

        elif slot == 2:
            unParked = self.bikes[0]
            self.bikes[0] = None

        elif slot == 3:
            unParked = self.bikes[1]
            self.bikes[1] = None

        else:
            unParked = self.cars[slot - 4]
            self.cars[slot - 4] = None

        return unParked

        
            
class ParkingLot:
    def __init__(self, parking_lot_id, no_of_floors, no_of_slots_per_floor):
        self.id = parking_lot_id
        self.no_of_slots_per_floor = no_of_slots_per_floor
        self.floors = [ParkingFloor(no_of_slots_per_floor) for _ in range(no_of_floors)] 

    def park(self, vehicle):
        for i, floor in enumerate(self.floors):
            slot = floor.park(vehicle)

            if slot == -1:
                continue

            return Ticket(self.id, i + 1, slot)
        
        return None

    def unPark(self, ticket):
        return self.floors[ticket.floor_no - 1].unPark(ticket.slot_no)

    def getStatus(self, type, status):
        vehicles = []

        for floor in self.floors:
            vehicles.append(floor.checkStatus(type, status))

        return vehicles

class Ticket:
    def __init__(self, parking_lot_id, floor_no, slot_no):
        self.lot_id = parking_lot_id
        self.floor_no = floor_no
        self.slot_no = slot_no
    def __str__(self):
        return f"{self.lot_id}_{self.floor_no}_{self.slot_no}"