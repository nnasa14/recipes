import recipes
import ingredients
import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

Base = declarative_base()

class Recipes(Base):
    __tablename__ = "recipes"
    title = Column(String, unique=True, nullable=False)
    ingredients = Column(String, nullable=False)

    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

# Create a database engine
engine = create_engine("sqlite:///recipes.db")

# Create all defined tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def clear_table(session):
    session.query(recipes).delete()
    session.commit()
    session.close()

def insert_data(data):
    # Add data and commit to table
    session.add_all(data)
    session.commit
    session.close

def display_table():
    # Retrieve data from table
    data = session.query(recipes).all()

    # Display the data
    for row in data:
        print(row.task, row.status)

    session.close()

if __name__ == "__main__":
    new_recipe = Recipes(title = "banana bread", ingredients = "banana")
    session.add(new_recipe)
    session.commit()

    #recipes = session.query(Recipes).filter(Recipes.title = "banana bread").all()      # search recipe

    # refer to the namespace