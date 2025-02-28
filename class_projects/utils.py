import random


from faker import Faker

fake = Faker()

gender = ["Male", "Female"]

def generate_fake_clients(t=300):
    from main import Client
    passenger_list = [ ]
    for _ in range(t):
        passenger_name = fake.name()
        passenger_age = random.randint(0, 100)
        passenger_gender = random.choice(gender)
        new_human = Client(passenger_name, passenger_age, passenger_gender)
        passenger_list.append(new_human)
    return passenger_list