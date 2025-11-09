from register import Register
from add_room import AddRoom
from book_room import BookRoom
from view_rooms import ViewRooms
from checkout import Checkout


class Main:
    def __init__(self, name, founded):
        self.name = name
        self.founded = founded

        # Composition 
        self.register = Register()
        self.add_room = AddRoom()
        self.book_room = BookRoom()
        self.view_rooms = ViewRooms()
        self.checkout = Checkout()

    def run(self):
        print(
            f"{'==' * 24}\nWelcome to {self.name}! Your stay begins here.\n{'==' * 24}")
        while True:
            options = input(
                "1. Register guest.\n2. Add room.\n3. Book room.\n4. View all rooms.\n5. Checkout guest.\n6. Exit.\nChoose(1|2|3|4|5|6):"
            )

            match options:
                case "1":
                    self.register.run()
                case "2":
                    self.add_room.run()
                case "3":
                    self.book_room.run()
                case "4":
                    self.view_rooms.run()
                case "5":
                    self.checkout.run()
                case "6":
                    print(
                        f"{'==' * 24}\nThank you for using {self.name}. Goodbye!\n{'==' * 24}")
                    break
                case _:
                    print(
                        f"{'==' * 24}\nWrong option. Choose between 1 to 6.\n{'==' * 24}")


main = Main(name="Hotelbnb", founded=2025)
main.run()
