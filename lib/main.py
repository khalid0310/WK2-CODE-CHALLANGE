# main.py
from customer import Customer
from restaurant import Restaurant
from review import Review

# Create instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Awesome Restaurant")
restaurant2 = Restaurant("Fantastic Cafe")

# Create reviews
review1 = Review(customer1, restaurant1, 5)
review2 = Review(customer2, restaurant1, 4)
review3 = Review(customer1, restaurant2, 3)

# Test functionality
print(customer1.full_name())
print(restaurant2.average_star_rating())
print(customer1.num_reviews())
