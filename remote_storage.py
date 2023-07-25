import recipes
import ingredients
import __init__
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker
Base = declarative_base()
engine = create_engine('db_url')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Recipes(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    ingredients = Column(String)

if __name__ == "__main__":
    new_recipe = Recipes(title = "banana bread", ingredients = "banana")
    session.add(new_recipe)
    session.commit()