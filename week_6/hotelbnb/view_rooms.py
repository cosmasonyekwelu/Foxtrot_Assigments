from model import Model


class ViewRooms(Model):
    def run(self):
        rooms = self.load_a_file(name_of_file="rooms.json")
        print(f"{'==' * 24}\n--- Room List ---\n{'==' * 24}")
        for r in rooms:
            print(
                f"Room {r['room_number']} | {r['room_type']} | ₦{r['price']} | {r['status']}")
        print(f"{'==' * 24}")
