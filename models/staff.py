from models.person import Person

class Staff(Person):
    def __init__(self, pid, name, age, stuff_id):
        super().__init__(pid, name, age)
        self.stuff_id = stuff_id
    def __str__(self):
        return f"Name:{self.name},Age:{self.age},StaffID:{self.stuff_id}"