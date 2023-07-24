#import sqlite3
import recipes
import ingredients
import __init__
import argparse
import logging
import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config["General"] = {
        "title": "Tasty Pallet",
        "version": "1.0",
        "debug": "True"
    }

    parser = argparse.ArgumentParser(description='Document recipes')
    parser.add_argument('-t', '--title', type=str, metavar='', required=True, help='title of recipe')
    parser.add_argument('-I', '--ingredients', type=list, metavar='', required=True, help='list of ingredients for recipe')
    parser.add_argument('-i', '--ingredient', type=list, metavar='', required=True, help='one ingredient among the list of ingredients')
    args = parser.parse_args()

    #conn = sqlite3.connect("recipes.db")

    logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H: %M: %S", filename="basic.log")         #DEBUG, INFO
    logging.debug("This is a debug message.")           #diagnosis and troubleshooting
    logging.info("This is an info message.")            #confirmation program is working as expected
    logging.warning("This is a warning message.")       #something unexpected happened that may cause issue in the future, but still working as expected
    logging.error("This is an error message.")          #more serious problem, software is not able to execute code
    logging.critical("This is a critical message.")     #serious error, program may be unanle to continue running

    test = recipes.Recipes()
    test_ing = ingredients.Ingredients()
    print(test_ing)
    test.add_recipe(args.title, args.ingredients)
    test.delete_recipe(args.title)
    test.edit_recipe(args.title, args.ingredients)
    print(test.search_recipe(args.title))
    print(test_ing.search_ingedient(args.ingredient))
    test.add_recipe(args.title, args.ingredients)
    print(test)
    print(test.search_recipe(args.title))
    test.delete_recipe(args.title)
    test.edit_recipe(
        args.title, args.ingredients)
    print(test.search_recipe(args.title))
    test.add_recipe(args.title, args.ingredients)
    print(test.search_recipe(args.title))
    test_ing.add_ingredients(args.title, args.ingredients)
    print(test.search_recipe(args.title))
    test.edit_recipe(
        args.title, args.ingredients)
    test_ing.delete_ingredient(
        args.title, args.ingredient)
    test_ing.edit_ingredients(
        args.title, args.ingredients)
    logging.warning(test)
