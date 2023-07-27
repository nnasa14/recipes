import recipes
import ingredients
import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite://my_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Recipes(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key = True)
    title = Column(String, unique=True, nullable=False)
    ingredients = Column(String, nullable=False)

if __name__ == "__main__":
    new_recipe = Recipes(title = "banana bread", ingredients = "banana")
    session.add(new_recipe)
    session.commit()

    #recipes = session.query(Recipes).filter(Recipes.title = "banana bread").all()      #search recipe

    #refer to the namespace