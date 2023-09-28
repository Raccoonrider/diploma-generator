from datetime import time

class Mock:
    def __init__(self):
        self.id = 1
        self.place = 29
        self.category = "M40+"
        self.last_name = "Константинов"
        self.first_name = "Константин"
        self.club = "Цепная Реакция"
        self.race_number = 55
        self.distance = 57
        self.time = time(hour=3, minute=24)

    @classmethod
    def get(cls, *args, **kwargs):
        return cls()