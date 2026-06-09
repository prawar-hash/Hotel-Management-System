import mysql.connector
from datetime import date


class HotelManagement:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="prawar1234",
            database="hotel_db"
        )
        self.cursor = self.conn.cursor()

    # Add Guest
    def add_guest(self):

        name = input("Enter Guest Name: ")

        try:
            age = int(input("Enter Age: "))
            room_no = int(input("Enter Room Number: "))
        except ValueError:
            print("Invalid Input")
            return

        # Check if room is occupied
        self.cursor.execute(
            "SELECT * FROM guests WHERE room_no=%s",
            (room_no,)
        )

        if self.cursor.fetchone():
            print("Room Already Occupied")
            return

        query = """
        INSERT INTO guests(name, age, room_no, check_in_date)
        VALUES(%s,%s,%s,%s)
        """

        values = (name, age, room_no, date.today())

        self.cursor.execute(query, values)
        self.conn.commit()

        print("Guest Added Successfully")

    # View All Guests
    def view_guests(self):

        self.cursor.execute("SELECT * FROM guests")

        records = self.cursor.fetchall()

        if not records:
            print("No Records Found")
            return

        print("\n----- Guest Records -----")

        for row in records:
            print("---------------------------")
            print("Guest ID :", row[0])
            print("Name     :", row[1])
            print("Age      :", row[2])
            print("Room No  :", row[3])
            print("Check In :", row[4])

    # Search Guest
    def search_guest(self):

        try:
            guest_id = int(input("Enter Guest ID: "))
        except ValueError:
            print("Invalid Input")
            return

        self.cursor.execute(
            "SELECT * FROM guests WHERE guest_id=%s",
            (guest_id,)
        )

        record = self.cursor.fetchone()

        if record:
            print("\nGuest Found")
            print("---------------------------")
            print("Guest ID :", record[0])
            print("Name     :", record[1])
            print("Age      :", record[2])
            print("Room No  :", record[3])
            print("Check In :", record[4])
        else:
            print("Guest Not Found")

    # Update Room
    def update_guest(self):

        try:
            guest_id = int(input("Enter Guest ID: "))
            new_room = int(input("Enter New Room Number: "))
        except ValueError:
            print("Invalid Input")
            return

        # Check if new room is occupied
        self.cursor.execute(
            "SELECT * FROM guests WHERE room_no=%s",
            (new_room,)
        )

        if self.cursor.fetchone():
            print("Room Already Occupied")
            return

        self.cursor.execute(
            "UPDATE guests SET room_no=%s WHERE guest_id=%s",
            (new_room, guest_id)
        )

        self.conn.commit()

        if self.cursor.rowcount > 0:
            print("Room Updated Successfully")
        else:
            print("Guest Not Found")

    # Check Out Guest
    def delete_guest(self):

        try:
            guest_id = int(input("Enter Guest ID: "))
        except ValueError:
            print("Invalid Input")
            return

        self.cursor.execute(
            "DELETE FROM guests WHERE guest_id=%s",
            (guest_id,)
        )

        self.conn.commit()

        if self.cursor.rowcount > 0:
            print("Guest Checked Out Successfully")
        else:
            print("Guest Not Found")

    # View Available Rooms
    def view_available_rooms(self):

        all_rooms = [101, 102, 103, 104, 105,
                     106, 107, 108, 109, 110]

        self.cursor.execute("SELECT room_no FROM guests")

        occupied_rooms = []

        for room in self.cursor.fetchall():
            occupied_rooms.append(room[0])

        print("\nAvailable Rooms")

        found = False

        for room in all_rooms:
            if room not in occupied_rooms:
                print(room)
                found = True

        if not found:
            print("No Rooms Available")

    # View Occupied Rooms
    def view_occupied_rooms(self):

        self.cursor.execute(
            "SELECT room_no, name FROM guests"
        )

        records = self.cursor.fetchall()

        if not records:
            print("No Rooms Occupied")
            return

        print("\nOccupied Rooms")

        for row in records:
            print("Room:", row[0], "| Guest:", row[1])

    def close_connection(self):

        self.cursor.close()
        self.conn.close()


def menu():

    hotel = HotelManagement()

    while True:

        print("\n===== HOTEL MANAGEMENT SYSTEM =====")
        print("1. Add Guest")
        print("2. View Guests")
        print("3. Search Guest")
        print("4. Update Guest Room")
        print("5. Check Out Guest")
        print("6. View Available Rooms")
        print("7. View Occupied Rooms")
        print("8. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            hotel.add_guest()

        elif choice == "2":
            hotel.view_guests()

        elif choice == "3":
            hotel.search_guest()

        elif choice == "4":
            hotel.update_guest()

        elif choice == "5":
            hotel.delete_guest()

        elif choice == "6":
            hotel.view_available_rooms()

        elif choice == "7":
            hotel.view_occupied_rooms()

        elif choice == "8":
            hotel.close_connection()
            print("Thank You")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()
