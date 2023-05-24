from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage = (mileage / self.MAX_MILEAGE) * 100
        cargo_percentage = percentage * 0.95
        self.battery_level -= round(cargo_percentage)
