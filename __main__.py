import json
import sqlite3
import recipes
import ingredients
import __init__

if __name__ == "__main__":
    conn = sqlite3.connect("recipes.db")
    test = recipes.Recipes()
    test_ing = ingredients.Ingredients()
    print(test_ing)
    test.add_recipe("banana bread", ["bananas", "flour", "eggs"])
    test.delete_recipe("popcorn")
    test.edit_recipe("popcorn", ["pop", "corn"])
    print(test.search_recipe("popcorn"))
    print(test_ing.search_ingedient("oranges"))
    test.add_recipe("banana bread", ["bananas", "eggs", "flour"])
    test.add_recipe("pizza", ["tomatoes", "flour", "cheese"])
    test.add_recipe("salad", ["lettuce", "tomatoes", "onions"])
    test.add_recipe(
        "chicken and broccoli", ["chicken", "broccoli", "soy sauce"])
    print(test)
    print(test.search_recipe("salad"))
    test.delete_recipe("salad")
    test.edit_recipe(
        "pizza", ["tomatoes", "flour", "cheese", "pepperoni"])
    print(test.search_recipe("pizza"))
    test.add_recipe("pizza", ["tomatoes", "flour", "cheese"])
    print(test.search_recipe("pizza"))
    test_ing.add_ingredients("pizza", ["yeast", "water"])
    print(test.search_recipe("popcorn"))
    test.edit_recipe(
        "salad", ["lettuce", "tomato", "eggs"])
    test_ing.delete_ingredient(
        "chicken and broccoli", "soy sauce")
    test_ing.edit_ingredients(
        "chicken and broccoli", ["chicken", "broccoli", "soy sauce"])
    print(test)
