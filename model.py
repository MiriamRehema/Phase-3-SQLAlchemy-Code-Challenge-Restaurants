from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a database connection
engine = create_engine('sqlite:///restaurant_reviews.db')
#The base
Base = declarative_base()

# Define the Restaurant, Customer, and Review models
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

     #To have a relationship with review we should
    reviews = relationship('Review', back_populates='restaurant')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # To have a relationship with review we should
    reviews = relationship('Review', back_populates='customer')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    star_rating = Column(Integer)

  # for review we should establish relationships with both customer and restaurant id's
    # To Establish a foreign key relationships
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    #and the other classes as well
    #To Establish relationships with Restaurant and Customer
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()