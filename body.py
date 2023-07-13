import json

class Recipes:
    def __init__ (self):
        with open("recipes.json", "r") as json_file:    
            self.data = json.load(json_file)     


    def __str__(self):
        return f"{self.data}"

    
    def add_recipe(self, recipe, ingredients):
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
        for recipes in self.data:
            if recipes["title"] == recipe:
                self.data.remove(recipes)             #del recipes
                break
        
        else:
            print("Recipe not archived")
            return

        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)

    
    def edit_recipe(self, recipe, ingredients):
        for recipes in self.data:
            #current = recipes["title"]
            if recipes["title"] == recipe:
                recipes["ingredients"] = ingredients
                break

        else:
            print("Recipe not archived")
            return

        with open("recipes.json", "w") as json_file:
            json.dump(self.data, json_file)


    def search_recipe(self, recipe):
        for recipes in self.data:
                if recipes["title"] == recipe:
                    return recipes
                
        return "Recipe not archived"
    

    def import_recipe(self, file_path):
        with open(file_path, "r") as file2:
            add_recipes = json.load(file2)

        self.data += add_recipes

        with open("recipes.json", "w") as file1:
            json.dump(self.data, file1)

class Ingredients:
    def __init__ (self):
        with open("recipes.json", "r") as json_file:    
            self.data = json.load(json_file) 


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
            #current = recipes["title"]
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

    
if __name__ == "__main__":
    test = Recipes()
    #test_ing = Ingredients()

    #print(test)

    #test.add_recipe("banana bread", ["bananas", "flour", "eggs"])

    #test.delete_recipe("dgsdgsdg")

    #test.edit_recipe("ghjjrtyg", ["i", "y", "t"])

    #print(test.search_recipe("popcorn"))

    #print(test_ing.search_ingedient("oranges"))


    test.add_recipe("banana bread", ["bananas", "eggs", "flour"])
    test.add_recipe("pizza", ["tomatoes", "flour", "cheese"])
    test.add_recipe("salad", ["lettuce", "tomatoes", "onions"])
    test.add_recipe("chicken and broccoli", ["chicken", "broccoli", "soy sauce"])

    print(test)

    #print(test.search_recipe("salad"))
    #test.delete_recipe("salad")
    #test.edit_recipe("pizza", ["tomatoes", "flour", "cheese", "pepperoni"])
    #print(test.search_recipe("pizza"))

    #test.add_recipe("pizza", ["tomatoes", "flour", "cheese"])

    #print(test.search_recipe("pizza"))

    #test_ing.add_ingredients("pizza", ["yeast", "water"])
    #print(test.search_recipe("popcorn"))
    #test.edit_recipe("salad", ["lettuce", "tomato", "eggs"])

    #test_ing.delete_ingredient("chicken and broccoli", "soy sauce")
    #test_ing.edit_ingredients("chicken and broccoli", ["chicken", "broccoli", "soy sauce"])