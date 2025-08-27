class Customer:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

    def input_details(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")

    def show_details(self):
        print("\nCustomer Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Booking:
    def __init__(self):
        self.destination = ""
        self.flight_choice = 0
        self.charge = 0.0

    def show_destinations(self):
        print("\nAvailable Destinations:")
        print("1. Dubai - Rs. 14000")
        print("2. Canada - Rs. 34000")
        print("3. UK - Rs. 44000")
        print("4. USA - Rs. 37000")
        print("5. Australia - Rs. 39000")
        print("6. Europe - Rs. 31000")

    def book_flight(self):
        self.show_destinations()
        self.flight_choice = int(input("Enter destination number to book: "))

        if self.flight_choice == 1:
            self.destination = "Dubai"
            self.charge = 14000
        elif self.flight_choice == 2:
            self.destination = "Canada"
            self.charge = 34000
        elif self.flight_choice == 3:
            self.destination = "UK"
            self.charge = 44000
        elif self.flight_choice == 4:
            self.destination = "USA"
            self.charge = 37000
        elif self.flight_choice == 5:
            self.destination = "Australia"
            self.charge = 39000
        elif self.flight_choice == 6:
            self.destination = "Europe"
            self.charge = 31000
        else:
            print("Invalid selection. Booking cancelled.")
            self.destination = "None"
            self.charge = 0

    def show_ticket(self, customer):
        if self.charge > 0:
            print("\n----- Ticket -----")
            print(f"Name: {customer.name}")
            print(f"Destination: {self.destination}")
            print(f"Charge: Rs. {self.charge}")
        else:
            print("No ticket booked.")


c = Customer()
c.input_details()

b = Booking()
b.book_flight()

c.show_details()
b.show_ticket(c)