import random

from ticketype import ticket_data
from utils import generate_fake_clients


class Client:
    def __init__(self, fullname: str, age: int, gender: str):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.balance = random.randint(300, 500)

    def __str__(self):
        return f"{self.fullname} {self.age} {self.gender}"

    def __repr__(self):
        return self.__str__()
    
class Plane:
    def __init__(self, name: str, speed: str, max_capacity: int, passengers: list):
        self.name = name
        self.speed = speed
        self.max_capacity = max_capacity
        self.passengers = passengers
    
    def add_client(self, info: Client):
        self.passengers.append(info)


aze_plane = Plane("AZAL", 100, 300, [])
fake_passengers = generate_fake_clients(aze_plane.max_capacity)
for passenger in fake_passengers:
    aze_plane.add_client(passenger)