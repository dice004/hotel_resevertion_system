from datetime import date

class Hotel:


	def __init__(self, hotel_name, location):
		self.hotel_name = hotel_name 
		self.location = location 
		


class Five_Star_Hotel(Hotel):
	def __init__(self, hotel_name, location, rooms_availability):
		super().__init__(hotel_name, location)
		self.rooms_availability = rooms_availability
		


class Four_Star_Hotel(Hotel):
	def __init__(self, hotel_name, location, rooms_availability):
		super().__init__(hotel_name, location)
		self.rooms_availability = rooms_availability
		
		

class Three_Star_Hotel(Hotel):
	def __init__(self, hotel_name, location, rooms_availability):
		super().__init__(hotel_name, location)
		self.rooms_availability = rooms_availability
		
		


class Kempinski_Hotel(Five_Star_Hotel):

	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Presidential Suite" : 6000,
						 	"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
											 }
						
		self.room_type = {'Presidential Suite' :[4501, 4507, 4519],
							"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]

						}

class Accra_Marriott_Hotel(Five_Star_Hotel):

	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Presidential Suite" : 6000,
						 	"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
											 }
						
		self.room_type = {'Presidential Suite' :[4501, 4507, 4519],
							"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]
										}

class Movenpick_Ambassador(Five_Star_Hotel):

	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Presidential Suite" : 6000,
							"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
											 }
						
		self.room_type = {'Presidential Suite' :[4501, 4507, 4519],
							"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]

											}			

class Labadi_Beach_Hotel(Five_Star_Hotel):

	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Presidential Suite" : 6000,
							"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
											 }
						
		self.room_type = {'Presidential Suite' :[4501, 4507, 4519],
							"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]
						}

class Tang_Hotel(Five_Star_Hotel):

	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Presidential Suite" : 6000,
							"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
						
		self.room_type = {'Presidential Suite' :[4501, 4507, 4519],
							"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]
						}
						 

class Lancaster_Kumasi_City(Four_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]
						}
							

class Lancaster_Accra(Four_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]
						}
							

class La_Palm_RoyalBeach(Four_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]
						}
							

class Kwarleyz_Residence(Four_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136] 
							}
		
class Villa_Monticello_Boutique_Hotel(Four_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Execuetive Suite" : 5000 ,
							"Junior Suite" : 4000 ,
							"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Execuetive Suite" : [3923, 3955, 3984],
							"Junior Suite": [2564, 2533, 2521],
							"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]
						}

class Zaina_Lodge(Three_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]

		}
							

class Orchid_Hotel_EastLegon(Three_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]

		}
							


class Orchid_Hotel_EastLegon(Three_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]

		}

class OakPlaza_Suites_Kumasi(Three_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]

		}

class ThePalms_PramPram(Three_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]

		}

class TheAfricanRegent(Three_Star_Hotel):
	def __init__(self,hotel_name, location, rooms_availability,  room_status):
		super().__init__(hotel_name, location, rooms_availability)
		self.room_status = room_status 
		self.room_price = {"Deluxe Room" : 3000 ,
							"Luxury Room" : 2000,
							"Standard Room" : 1000,
						 }
							
						
		self.room_type = {"Deluxe Room": [1541, 2535, 2501],
							"Luxury Room": [801, 865, 845],
							"Standard Room": [101, 108, 136]

		}


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



