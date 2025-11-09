import random
from model import Model


class Register(Model):
    def __init__(self):
        self.guests = self.load_a_file(name_of_file="guests.json")

    def run(self):
        name = input("Enter guest full name: ")
        email = input("Enter guest email: ")

        customer_id = random.randint(1000, 9999)

        guest = {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "room_number": None,
            "days": 0,
            "bill": 0.0
        }

        self.guests.append(guest)
        self.save_a_file(name_of_file="guests.json", content=self.guests)

        print(
            f"{'==' * 24}\nGuest registered successfully!\nGuest ID: {customer_id}\n{'==' * 24}")
