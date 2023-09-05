from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Restaurant, Customer, Review  

# Create a database connection
engine = create_engine('sqlite:///restaurant_reviews.db')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Data seeding (creating sample data)
restaurant1 = Restaurant(name="CJ's", price=490)
restaurant2 = Restaurant(name="Kilimanjaro", price=650)
restaurant3 = Restaurant(name="Roswan", price=430)
restaurant4 = Restaurant(name="Two in Ones", price=890)
restaurant5 = Restaurant(name="Pronto", price=786)
restaurant6 = Restaurant(name="Big knife", price=435)
restaurant7 = Restaurant(name="Grill", price=250)
restaurant8 = Restaurant(name="Tj's", price=1000)
restaurant9 = Restaurant(name="Westies", price=500)
restaurant10 = Restaurant(name="Pork in", price=990)


customer1 = Customer(first_name="Miriam", last_name="Rehema")
customer2 = Customer(first_name="Luke", last_name="John")
customer3 = Customer(first_name="Hellen", last_name="Wamaitha")
customer4 = Customer(first_name="Jane", last_name="Wangeci")
customer5 = Customer(first_name="Hadassah", last_name="Neema")
customer6 = Customer(first_name="Ruth", last_name="Gituku")
customer7 = Customer(first_name="Wilson", last_name="Wakibatha")
customer8= Customer(first_name="Jemimah", last_name="Wamaitha")
customer9 = Customer(first_name="Keziah", last_name="Wangeci")
customer10 = Customer(first_name="Neema", last_name="Wangeci")



review1 = Review(content="Nice food!", star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(content="Average .", star_rating=3, restaurant=restaurant2, customer=customer2)
review3 = Review(content="Awsome!", star_rating=7, restaurant=restaurant3, customer=customer3)
review4 = Review(content="Good.", star_rating=6, restaurant=restaurant4, customer=customer4)
review5 = Review(content="Delicious!", star_rating=8, restaurant=restaurant5, customer=customer5)
review6 = Review(content="Tasty .", star_rating=9, restaurant=restaurant6, customer=customer6)
review7 = Review(content="Not bad!", star_rating=5, restaurant=restaurant7, customer=customer7)
review8 = Review(content="Excellent .", star_rating=9, restaurant=restaurant8, customer=customer8)
review9 = Review(content="Great!", star_rating=7, restaurant=restaurant9, customer=customer9)
review10 = Review(content="Enjoyable.", star_rating=8, restaurant=restaurant10, customer=customer10)


# Add data to the session and commit it to the database
session.add_all([restaurant1, restaurant2,restaurant1, restaurant2,restaurant1, restaurant2,restaurant1, restaurant2,restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()

