class Hotel:
    def __init__(self, hotel_name, location, rooms_available):
        self.hotel_name = hotel_name
        self.location = location  
        self.rooms_available = rooms_available

class FiveStarHotel(Hotel):
         def __init__(self, hotel_name, location, rooms_available, price, presidential_suite, executive_suite, deluxe_suite, luxury_suite, standard_suite):
            super().__init__(hotel_name, location, rooms_available)

            self.price = price
            self.presidential_suite = presidential_suite
            self.executive_suite = executive_suite
            self.deluxe_suite = deluxe_suite
            self.luxury_suite = luxury_suite            
            self.standard_suite = standard_suite
 
class FourStarHotel(Hotel):
         def __init__(self, hotel_name, location, rooms_available, price, executive_suite, deluxe_suite, luxury_suite, standard_suite):
            super().__init__(hotel_name, location, rooms_available)

            self.price = price
            self.executive_suite = executive_suite
            self.deluxe_suite = deluxe_suite
            self.luxury_suite = luxury_suite            
            self.standard_suite = standard_suite

class ThreeStarHotel(Hotel):
            def __init__(self, hotel_name, location, rooms_available, price, deluxe_suite, luxury_suite, standard_suite):
                super().__init__(hotel_name, location, rooms_available)
    
                self.price = price
                self.deluxe_suite = deluxe_suite
                self.luxury_suite = luxury_suite            
                self.standard_suite = standard_suite   

class StarRating:
    def __init__(self, star_rating):
        self.star_rating = star_rating

class User:
    def __init__(self, user_name, email, phone_number):
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number

class Booking:
    def __init__(self, hotel_name, location, rooms_available, price, presidential_suite, executive_suite, deluxe_suite, luxury_suite, standard_suite):
        self.hotel_name = hotel_name
        self.location = location
        self.rooms_available = rooms_available
        self.price = price
        self.presidential_suite = presidential_suite
        self.executive_suite = executive_suite
        self.deluxe_suite = deluxe_suite
        self.luxury_suite = luxury_suite            
        self.standard_suite = standard_suite

# Create objects for the five-star hotels

# Objects

# Five-star hotels
kempinski = FiveStarHotel("Accra", True, "Kempinski Hotel Gold Coast City", 500, True, True, True, True, True)
marriott = FiveStarHotel("Accra", True, "Marriott Hotel Accra", 450, True, True, True, True, True)
movenpick = FiveStarHotel("Accra", True, "Mövenpick Ambassador Hotel Accra", 400, True, True, True, True, True)
labadi_beach_hotel = FiveStarHotel("Accra", True, "Labadi Beach Hotel", 350, True, True, True, True, True)
tang_hotel = FiveStarHotel("Accra", True, "Tang Palace Hotel", 300, True, True, True, True, True)

# Four-star hotels
lancaster_kumasi = FourStarHotel("Kumasi", True, "Lancaster Kumasi City Hotel", 250, True, True, True, True)
lancaster_accra = FourStarHotel("Accra", True, "Lancaster Accra City Hotel", 200, True, True, True, True)
villa_monticello = FourStarHotel("Accra", True, "Villa Monticello Hotel", 150, True, True, True, True)
kwarleyz = FourStarHotel("Accra", True, "Kwarleyz Residence", 100, True, True, True, True)
la_palm_royal = FourStarHotel("Accra", True, "La Palm Royal Beach Hotel", 50, True, True, True, True)

# Three-star hotels
zaina = ThreeStarHotel("Accra", True, "Zaina Lodge", 30, True, True, True)
oak_plaza_kumasi = ThreeStarHotel("Kumasi", True, "Oak Plaza Hotel Kumasi", 25, True, True, True)
orchid_hotel = ThreeStarHotel("Accra", True, "Orchid Hotel", 20, True, True, True)
african_regen = ThreeStarHotel("Accra", True, "African Regent Hotel", 15, True, True, True)
the_palms_pram_pram = ThreeStarHotel("Pram Pram", True, "The Palms Resort", 10, True, True, True)

# Create objects for the star ratings

# Create objects for the users

# Create objects for the bookings

# Create a list of all the hotels

