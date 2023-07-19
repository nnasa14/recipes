import json

class Ingredients:

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
        valid_recipes = []
        for recipes in self.data:
            for items in recipes["ingredients"]:
                if items == ingredient:
                    valid_recipes.append(recipes)
        if len(valid_recipes) <= 0:
            return "No recipes contain this ingredient"
        return valid_recipes

    def add_ingredients(self, recipe, ingredients):
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
        for recipes in self.data:
            if recipes["title"] == recipe:
                ingredients_value = recipes["ingredients"]
                for item in ingredients_value:
                    if ingredient in ingredients_value:
                        ingredients_value.remove(ingredient)
        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)

    def edit_ingredients(self, recipe, ingredients):
        for recipes in self.data:
            if recipes["title"] == recipe:
                recipes["ingredients"] = ingredients
        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)