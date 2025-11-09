from model import Model


class AddRoom(Model):
    def __init__(self):
        self.rooms = self.load_a_file(name_of_file="rooms.json")

    def run(self):
        room_number = input("Enter room number: ")
        room_type = input("Enter room type (Single/Double/Suite/Executive): ")
        price = float(input("Enter price per night: "))

        room = {
            "room_number": room_number,
            "room_type": room_type,
            "price": price,
            "status": "Available"
        }

        self.rooms.append(room)
        self.save_a_file(name_of_file="rooms.json", content=self.rooms)

        print(f"{'==' * 24}\nRoom {room_number} added successfully.\n{'==' * 24}")
