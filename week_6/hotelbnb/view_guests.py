from model import Model


class ViewGuests(Model):
    def run(self):
        guests = self.load_a_file(name_of_file="guests.json")
        print(f"{'==' * 24}\n--- Guest List ---\n{'==' * 24}")

        if not guests:
            print("No registered guests.")
            print(f"{'==' * 24}")
            return

        for g in guests:
            bookings = g.get("bookings", [])
            room_count = len(bookings)
            total_due = sum(b["bill"] for b in bookings)
            status = "Checked-in" if bookings else "No active booking"
            print(
                f"Name: {g['name']} | Email: {g['email']} | Rooms: {room_count} | Total Due: ₦{total_due} | Status: {status}")

        print(f"{'==' * 24}")
