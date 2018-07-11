class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant'name is " + self.restaurant_name.title() +
              " and its type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " in operation.")

    def set_number_served(self):
        print("How many people have dinner in the restaurant?" + " " +
              str(self.number_served))


restaurant = Restaurant("lei", "sh_an_dong cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served()

