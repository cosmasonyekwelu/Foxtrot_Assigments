from model import Model


class BookRoom(Model):
    def __init__(self):
        self.guests = self.load_a_file(name_of_file="guests.json")
        self.rooms = self.load_a_file(name_of_file="rooms.json")

    def run(self):
        guest_id = input("Enter guest ID: ")
        room_number = input("Enter room number to book: ")

        guest = None
        room = None

        for g in self.guests:
            if g["customer_id"] == int(guest_id):
                guest = g
                break


        for r in self.rooms:
            if r["room_number"] == room_number and r["status"] == "Available":
                room = r
                break

        if not guest:
            print(f"{'==' * 24}\nGuest not found.\n{'==' * 24}")
            return

        if not room:
            print(f"{'==' * 24}\nRoom not found or already booked.\n{'==' * 24}")
            return

        days = int(input("Enter number of nights: "))
        total_bill = room["price"] * days

        guest["room_number"] = room["room_number"]
        guest["days"] = days
        guest["bill"] = total_bill
        room["status"] = "Booked"

        self.save_a_file("guests.json", self.guests)
        self.save_a_file("rooms.json", self.rooms)

        print(
            f"{'==' * 24}\nRoom {room['room_number']} booked for {guest['name']}.\nTotal bill: ₦{total_bill}\n{'==' * 24}")
