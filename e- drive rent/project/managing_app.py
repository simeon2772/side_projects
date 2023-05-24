from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def find_route(self, route_id):
        for route in self.routes:
            if route.route_id == route_id:
                return route

    def find_vehicle(self, plate):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == plate:
                return vehicle

    def find_user(self, license):
        for user in self.users:
            if user.driving_license_number == license:
                return user

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        valid_types = ("PassengerCar", "CargoVan")
        if vehicle_type not in valid_types:
            return f"Vehicle type {vehicle_type} is inaccessible."
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        if vehicle_type == "PassengerCar":
            v = PassengerCar(brand, model, license_plate_number)
        else:
            v = CargoVan(brand, model, license_plate_number)
        self.vehicles.append(v)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
        r = Route(start_point, end_point, length, route_id=len(self.routes) + 1)
        self.routes.append(r)
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self.find_user(driving_license_number)
        vehicle = self.find_vehicle(license_plate_number)
        route = self.find_route(route_id)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            if vehicle.is_damaged:
                user.decrease_rating()
            else:
                user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                damaged_vehicles.append(vehicle)

        damaged_vehicles.sort(key=lambda v: (v.brand, v.model))

        for v in damaged_vehicles:
            v.is_damaged = False
            v.recharge()

        if len(damaged_vehicles) > count:
            return f"{count} vehicles were successfully repaired!"
        else:
            return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        pass


app = ManagingApp()
print(app.register_user('Tisha', 'Reenie', '7246506'))
print(app.register_user('Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user('Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle('PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
# print(app.users_report())
