from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Restaurant, Customer, Review

# Create a database connection
engine = create_engine('sqlite:///restaurant_reviews.db')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Display all restaurants
restaurants = session.query(Restaurant).all()
print("Restaurants:")
for restaurant in restaurants:
    print(f"ID: {restaurant.id}, Name: {restaurant.name}, Price: {restaurant.price}")

# Display all customers
customers = session.query(Customer).all()
print("\nCustomers:")
for customer in customers:
    print(f"ID: {customer.id}, First Name: {customer.first_name}, Last Name: {customer.last_name}")

# Display all reviews
reviews = session.query(Review).all()
print("\nReviews:")
for review in reviews:
    print(f"ID: {review.id}, Content: {review.content}, Rating: {review.star_rating}")
