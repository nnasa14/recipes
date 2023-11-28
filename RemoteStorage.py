import recipes
import ingredients
from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

Base = declarative_base()

class Recipes(Base):
    __tablename__ = "recipes"
    title = Column(String, primary_key=True, nullable=False)
    ingredients = Column(String, nullable=False)

    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def __repr__(self):
        return f"{self.title}: {self.ingredients}"

# Create a database engine
engine = create_engine("sqlite:///recipes.db")

# Create all defined tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def clear_table(session):
    session.query(Recipes).delete()
    session.commit()
    session.close()

def insert_data(data):
    # Add data and commit to table
    session.add_all(data)
    session.commit()
    session.close()

def display_table():
    # Retrieve data from table
    data = session.query(Recipes).all()

    # Display the data
    for row in data:
        print(row.task, row.status)

    session.close()

def search_recipe(title):
    return title

def search_ingredient(ingredient):
    return ingredient

if __name__ == "__main__":
   clear_table(session)
   """data = [
        Recipes(title="banana bread", ingredients="banana, eggs, flour"),
        Recipes(title="chicken parm", ingredients="chicken, parmesan, tomato sauce"),
        Recipes(title="cheeseburger", ingredients="buns, beef, cheese")
    ]
   insert_data(data)"""

    #recipes = session.query(Recipes).filter(Recipes.title = "banana bread").all()      # search recipe