import json

class Recipes:
    """
    A class of CRUD and search functions for recipes in database recipes.json

    Methods: 
        add_recipe(recipe, ingredients): add recipe as a dictionary in which a list of ingredients follows the title
        delete_recipe(recipe): delete recipe along with its ingredients
        edit_recipe(recipe, ingredients): change the ingredients of a recipe
        search_recipe(recipe): retrieve a specfic recipe
        import_recipe(file_path): add recipe to recipes.json from another json file
    """

    def __init__(self):
        with open("recipes.json", "r") as json_file:
            self.data = json.load(json_file)

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        # FIXME: no idea what is going on here
        # return f"Recipes(data = self.data)"
        return f"{repr(self.data)}"

    def add_recipe(self, recipe, ingredients):
        """
        Function that adds a list of ingredient(s) to a specific recipe

        Parameters:
            recipe (str): Title of the recipe 
            ingredients (list): A list of ingredient(s)
        """
        if any(entry["title"] == recipe for entry in self.data):
            print("Recipe already archived")
            return
        updated_recipe = {
            "title": recipe,
            "ingredients": ingredients
        }
        self.data.append(updated_recipe)
        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)

    def delete_recipe(self, recipe):
        """
        Function that adds a list of ingredient(s) to a specific recipe

        Parameters:
            recipe (str): Title of the recipe
            ingredients (list): A list of ingredient(s)
        """
        for recipes in self.data:
            if recipes["title"] == recipe:
                self.data.remove(recipes)
                break
        else:
            print("Recipe not archived")
            return
        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)

    def edit_recipe(self, recipe, ingredients):
        """
        Function that adds a list of ingredient(s) to a specific recipe

        Parameters:
            recipe (str): Title of the recipe
            ingredients (list): A list of ingredient(s)
        """
        for recipes in self.data:
            # current = recipes["title"]
            if recipes["title"] == recipe:
                recipes["ingredients"] = ingredients
                break
        else:
            print("Recipe not archived")
            return
        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)

    def search_recipe(self, recipe):
        """
        Function that adds a list of ingredient(s) to a specific recipe

        Parameters:
            recipe (str): Title of the recipe
            ingredients (list): A list of ingredient(s)

        Return:
            dict: Recipe title and list of ingredients
        """
        for recipes in self.data:
            if recipes["title"] == recipe:
                return recipes
        return "Recipe not archived"

    def import_recipe(self, file_path):
        """
        Function that adds a list of ingredient(s) to a specific recipe

        Parameters:
            file_path (str): Location of file
        """
        with open(file_path, "r") as file2:
            add_recipes = json.load(file2)
        self.data += add_recipes
        with open("recipes.json", "w") as file1:
            json.dump(self.data, file1)