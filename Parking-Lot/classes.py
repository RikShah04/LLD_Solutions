class Vehicle:
    def __init__(self, type, registration_number, color):
        self.type = type
        self.registration_number = registration_number
        self.color = color

class ParkingFloor:
    def __init__(self, no_of_slots_per_floor, slot_config):
        self.slot_config = slot_config
        self.slots = [None] * no_of_slots_per_floor

    def park(self, vehicle):
        avail = self.checkStatus(vehicle.type, True)

        if not avail:
            return -1

        start, end = self.slot_config[vehicle.type]
        
        for i in range(start, end):
            if not self.slots[i]:
                self.slots[i] = vehicle
                return i + 1
                
    def checkStatus(self, type, status):
        if type not in self.slot_config:
            return []
        
        avail = []
        
        start, end = self.slot_config[type]

        for i in range(start, end):
            if (self.slots[i] == None) == status:
                avail.append(i + 1)

        return avail

    def unPark(self, slot):
        if not (1 <= slot <= len(self.slots)):
            return None

        unParked = self.slots[slot - 1]
        self.slots[slot - 1] = None

        return unParked
        
            
class ParkingLot:
    def __init__(self, parking_lot_id, no_of_floors, no_of_slots_per_floor):
        self.id = parking_lot_id
        self.no_of_slots_per_floor = no_of_slots_per_floor
        slot_config = {"TRUCK": (0,1), "BIKE": (1,3), "CAR": (3, no_of_slots_per_floor) }
        self.floors = [ParkingFloor(no_of_slots_per_floor, slot_config) for _ in range(no_of_floors)] 

    def park(self, vehicle):
        for i, floor in enumerate(self.floors):
            slot = floor.park(vehicle)

            if slot == -1:
                continue

            return Ticket(self.id, i + 1, slot)
        
        return None

    def unPark(self, ticket):
        if not(1 <= ticket.floor_no <= len(self.floors)):
            return None
        
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