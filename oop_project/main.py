class Plain:
    def __init__(self, name: str, capacity: int, speed: int, passenger: list, is_flying: bool):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.passenger = passenger
        self.is_flying = is_flying

    def increase_speed(self):
        if self.speed <= 900:
            self.speed += 50
        else:
            self.speed = 900
    
    def add_passenger(self, passenger_name):
        if len(self.passenger <= 299):
            self.passenger.append(passenger_name)
    
    def take_off(self):
        if len(self.passenger) != 0:
            self.is_flying = True

    def land(self):
        if self.is_flying == False:
            self.speed = 0
    
    def removing_passenger(self, removing_passenger):
        self.passenger.remove(removing_passenger)
    
aze_plain = Plain(name="AZAL", capacity=300, speed=0, passenger=["Yusif"], is_flying=False)
