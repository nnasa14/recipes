import json

class Ingredients:
    """
    This is a class for the CRUD and search specifically for the ingredients list in recipes.json

    Methods:
        search_ingredient(ingredient): Retrives recipes that contain a specific ingredient
        add_ingredients(recipe, ingredients): Append a list of ingredients to an already existing one
        delete_ingredient(recipe, ingredient): Delete a specific ingredient from a recipe
        edit_ingredient(recipe, ingredient): Replace an existing list of ingredients in a recipe with another 
    """

    def __init__(self):
        with open("recipes.json", "r") as json_file:
            self.data = json.load(json_file)

    def __str__(self):
        ingredients_list = []
        for item in self.data:
            ingredients_list.append(item["ingredients"])
        return f"{ingredients_list}"

    def __repr__(self):
        # FIXME: again no idea here
        # return f"Recipes(data = self.data)"
        return f"{repr(self.data)}"

    def search_ingedient(self, ingredient):
        """
        Function that returns a list of recipes that contain a specific ingredient

        Parameters:
            ingredient (str): The target ingredient

        Returns:
            list: recipes and their ingrdients which include ingredient
        """
        valid_recipes = []
        for recipes in self.data:
            for items in recipes["ingredients"]:
                if items == ingredient:
                    valid_recipes.append(recipes)
        if len(valid_recipes) <= 0:
            return "No recipes contain this ingredient"
        return valid_recipes

    def add_ingredients(self, recipe, ingredients):
        """
        Function that adds a list of ingredient(s) to a specific recipe

        Parameters:
            recipe (str): Title of the recipe
            ingredients (list): A list of ingredient(s)
        """
        for recipes in self.data:
            # current = recipes["title"]
            if recipes["title"] == recipe:
                ingredients_value = recipes["ingredients"]
                for item in ingredients:
                    if item in ingredients_value:
                        print("Ingredient(s) already exist")
                    else:
                        ingredients_value.append(item)
                break
        else:
            print("Recipe not archived")
            return

    def delete_ingredient(self, recipe, ingredient):
        """
        Function that adds a list of ingredient(s) to a specific recipe

        Parameters:
            recipe (str): Title of the recipe
            ingredient (str): Ingredient function seeks to delete from a recipe
        """
        for recipes in self.data:
            if recipes["title"] == recipe:
                ingredients_value = recipes["ingredients"]
                for item in ingredients_value:
                    if ingredient in ingredients_value:
                        ingredients_value.remove(ingredient)
        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)

    def edit_ingredients(self, recipe, ingredients):
        """
        Function that adds a list of ingredient(s) to a specific recipe

        Parameters:
            recipe (str): Title of the recipe
            ingredients (list): A list of ingredient(s) to replace the list in the database
        """
        for recipes in self.data:
            if recipes["title"] == recipe:
                recipes["ingredients"] = ingredients
        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)