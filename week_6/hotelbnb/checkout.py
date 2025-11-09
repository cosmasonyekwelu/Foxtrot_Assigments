from model import Model


class Checkout(Model):
    def run(self):
        guests = self.load_a_file(name_of_file="guests.json")
        rooms = self.load_a_file(name_of_file="rooms.json")

        guest_id = input("Enter guest ID for checkout: ")

        guest = None
        for g in guests:
            if g["customer_id"] == int(guest_id):
                guest = g
                break

        if not guest or "bookings" not in guest or len(guest["bookings"]) == 0:
            print(f"{'==' * 24}\nGuest not found or no active booking.\n{'==' * 24}")
            return

        total_due = sum(b["bill"] for b in guest["bookings"])
        print(
            f"{'==' * 24}\nGuest: {guest['name']}\nRooms booked: {len(guest['bookings'])}\nTotal Bill: ₦{total_due}\n{'==' * 24}")

        confirm = input("Confirm checkout (yes/no): ").lower()
        if confirm == "yes":
            for booking in guest["bookings"]:
                for r in rooms:
                    if str(r["room_number"]) == str(booking["room_number"]):
                        r["status"] = "Available"

            guest["bookings"] = []

            self.save_a_file("guests.json", guests)
            self.save_a_file("rooms.json", rooms)

            print(f"{'==' * 24}\nCheckout complete. Thank you!\n{'==' * 24}")
        else:
            print(f"{'==' * 24}\nCheckout cancelled.\n{'==' * 24}")
