from HotelMgmtSystem import Hotel
#list of hotels'''

    def start():
        print("Starting app...")
        print("x"*30)


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