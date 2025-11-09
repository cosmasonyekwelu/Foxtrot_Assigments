from model import Model


class Checkout(Model):
    def __init__(self):
        self.guests = self.load_a_file(name_of_file="guests.json")
        self.rooms = self.load_a_file(name_of_file="rooms.json")

    def run(self):
        guest_id = input("Enter guest ID for checkout: ")

        guest = None
        for g in self.guests:
            if g["customer_id"] == int(guest_id):  
                guest = g
                break

        if not guest or not guest["room_number"]:
            print(f"{'==' * 24}\nGuest not found or no active booking.\n{'==' * 24}")
            return

        print(
            f"{'==' * 24}\nGuest: {guest['name']}\nRoom: {guest['room_number']}\nTotal Bill: ₦{guest['bill']}\n{'==' * 24}"
        )

        confirm = input("Confirm checkout (yes/no): ").lower()
        if confirm == "yes":

            for r in self.rooms:
                if r["room_number"] == guest["room_number"]:
                    r["status"] = "Available"


            guest["room_number"] = None
            guest["days"] = 0
            guest["bill"] = 0.0

            self.save_a_file("guests.json", self.guests)
            self.save_a_file("rooms.json", self.rooms)

            print(f"{'==' * 24}\nCheckout complete. Thank you!\n{'==' * 24}")
        else:
            print(f"{'==' * 24}\nCheckout cancelled.\n{'==' * 24}")
