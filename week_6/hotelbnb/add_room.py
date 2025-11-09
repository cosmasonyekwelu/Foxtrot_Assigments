from model import Model


class AddRoom(Model):
    def run(self):
        rooms = self.load_a_file(name_of_file="rooms.json")

        room_number = input("Enter room number: ")

        for r in rooms:
            if r["room_number"] == room_number:
                print(
                    f"{'==' * 24}\nRoom {room_number} already exists.\n{'==' * 24}")
                return

        room_type = input("Enter room type (Single/Double/Suite/Executive): ")
        price = float(input("Enter price per night: "))

        room = {
            "room_number": room_number,
            "room_type": room_type,
            "price": price,
            "status": "Available"
        }

        rooms.append(room)
        self.save_a_file(name_of_file="rooms.json", content=rooms)

        print(f"{'==' * 24}\nRoom {room_number} added successfully.\n{'==' * 24}")
