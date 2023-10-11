from datetime import date

class Hotel:


	def __init__(self, hotel_name, location,rooms_availability, total_rooms):
		self.hotel_name = hotel_name 
		self.location = location 
		self.rooms_availability = rooms_availability
		self.total_rooms = total_rooms


class Five_Star_Hotel(Hotel):
	def __init__(self, hotel_name, location, rooms_availability, rating):
		super().__init__(hotel_name, location, rooms_availability)
		self.rating = "Five Star"



class Four_Star_Hotel(Hotel):
	def __init__(self, hotel_name, location, rooms_availability, rating):
		super().__init__(hotel_name, location, rooms_availability)
		self.rating = "Four Star"

class Three_Star_Hotel(Hotel):
	def __init__(self, hotel_name, location, rooms_availability, rating):
		super().__init__(hotel_name, location, rooms_availability)
		self.rating = "Three Star"


class Room:

	 def __init_(self, room_number, room_type, room_price, room_status):
						self.room_number = room_number 
						self.room_type = room_type 
						self.room_price = room_price 
						self.room_status = room_status 

class Presidential_Suite(Room):
	    pass

class Execuetive_Suite(Room):
        pass

class Junior_Suite(Room):
        pass

class Deluxe_Room(Room):
		pass

class Luxury_Room(Room):
		pass

class Standard_Room(Room):
		pass


class HotelMgmtSystem:

		def __init__(self, hotel_list):
				self.hotel_list = []

		def check_hotel_availability(self, hotel_name):
				return hotel_name in self.hotel_list

		def check_room_availability (self, hotel_name, room_type):
				room_type = Room
				for hotel in self.hotel_list:
					if hotel.hotel_name == hotel_name:
						for room in hotel.room_availability:
							if room.room_type == room.room_status == "Available"
											return True

		def get_room_rice (self, hotel_name, room_type):
			for hotel in self.hotel_list:
				if hotel.hotel_name == hotel.name:
					for room_type in room.room_availability:
						return



def sort_by_location(self):
	pass

def sort_by_rating(self):
	pass


						

class User:
	def __init__(self, user_name, phone_number, email):
		self.user_name = user_name  
		self.phone_number = phone_number
		self.email = email



