from model import Model


class BookRoom(Model):
    def run(self):
        guests = self.load_a_file(name_of_file="guests.json")
        rooms = self.load_a_file(name_of_file="rooms.json")

        guest_id = input("Enter guest ID: ")
        room_number = input("Enter room number to book: ")

        guest = None
        room = None

        for g in guests:
            if g["customer_id"] == int(guest_id):
                guest = g
                break

        if not guest:
            print(f"{'==' * 24}\nGuest not found.\n{'==' * 24}")
            return

        for r in rooms:
            if r["room_number"] == room_number and r["status"] == "Available":
                room = r
                break

        if not room:
            print(f"{'==' * 24}\nRoom not found or already booked.\n{'==' * 24}")
            return

        days = int(input("Enter number of nights: "))
        total_bill = room["price"] * days

        if "bookings" not in guest:
            guest["bookings"] = []

        booking = {
            "room_number": room["room_number"],
            "days": days,
            "bill": total_bill
        }

        guest["bookings"].append(booking)
        room["status"] = "Booked"

        self.save_a_file("guests.json", guests)
        self.save_a_file("rooms.json", rooms)

        print(
            f"{'==' * 24}\nRoom {room['room_number']} booked for {guest['name']}.\nTotal bill: ₦{total_bill}\n{'==' * 24}")
