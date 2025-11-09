import random
from model import Model


class Register(Model):
    def run(self):
        guests = self.load_a_file("guests.json")

        name = input("Enter guest full name: ")
        email = input("Enter guest email: ")
        customer_id = random.randint(1000, 9999)

        guest = {
            "customer_id": customer_id,
            "name": name,
            "email": email
        }

        guests.append(guest)
        self.save_a_file("guests.json", guests)

        print(
            f"{'==' * 24}\nGuest registered successfully!\nGuest ID: {customer_id}\n{'==' * 24}")
