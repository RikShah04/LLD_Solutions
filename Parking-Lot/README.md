# Parking Lot — Low Level Design

## Problem
Design a parking lot system that supports multiple floors,
multiple vehicle types, and basic parking operations.

## Features
- Multiple floors and configurable slots per floor
- Supports CAR, BIKE, and TRUCK vehicle types
- Park and unpark vehicles with ticket generation
- Display free and occupied slots per floor per vehicle type

## Classes
- `Vehicle` — represents a vehicle with type, registration, and color
- `ParkingFloor` — manages slots for one floor
- `ParkingLot` — manages all floors, entry point for all operations
- `Ticket` — represents a parking ticket with lot, floor, and slot info

## CLI Commands
- `create_parking_lot <id> <floors> <slots_per_floor>`
- `park_vehicle <type> <reg_no> <color>`
- `unpark_vehicle <ticket_id>`
- `display free_count <vehicle_type>`
- `display free_slots <vehicle_type>`
- `display occupied_slots <vehicle_type>`

## How to Run
```bash
cd Parking-Lot
python driver.py
```