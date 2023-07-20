import json
import sqlite3
import recipes
import ingredients
import __init__
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Document recipes')
    parser.add_argument('-t', '--title', type=str, metavar='', required=True, help='title of recipe')
    parser.add_argument('-I', '--ingredients', type=list, metavar='', required=True, help='list of ingredients for recipe')
    parser.add_argument('-i', '--ingredient', type=list, metavar='', required=True, help='one ingredient among the list of ingredients')
    args = parser.parse_args()
    conn = sqlite3.connect("recipes.db")
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
    print(test)
