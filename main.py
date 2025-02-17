from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time

@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude

def get_coordinates(address: str) -> Coordinates | None:
    geolocator = Nominatim(user_agent='distance_calculator')
    location = geolocator.geocode(address)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)

def calculate_distance_km(home: Coordinates, target: Coordinates) -> float | None:
    if home and target:
        distance: float = geodesic(home.coordinates(), target.coordinates()).km
        return distance

def get_distance_km(home: str, target: str) -> float | None:
    home_coordinates: Coordinates = get_coordinates(home)
    target_coordinates: Coordinates = get_coordinates(target)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'{home} -> {target} -> {distance:.2f} km')
        return distance
    else:
        print('Failed to calculate distance')

def main():
    home_address: str = 'Helsinkigade 10, Copenhagen 2150, Denmark'
    print(f'Home address: {home_address}')

    target_address: str = input('Enter an address: ')
    print('Calculating...')
    time.sleep(1)
    get_distance_km(home_address, target_address)

if __name__ == '__main__':
    main()