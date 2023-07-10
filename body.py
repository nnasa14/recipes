import json

class Recipes:
    def __init__ (self):
        self.recipes_list = {}            

    def add_recipe(self, recipe, ingredients):                
        with open("recipes.json", "r") as json_file:    
            data = json.load(json_file)                 #data becomes a list

        if recipe in data:                              #do not append existing recipe
            print("Recipe already archived")
            return

        updated_recipe = {
            "title": recipe,
            "ingredients": ingredients
        }

        #existing_data.append({
        #    "title": banana_bread_title["title"],
        #    "ingredients": banana_bread_ing["ingredients"]
        #   })

        data.append(updated_recipe)

        with open("recipes.json", "w") as json_file:
            json.dump(data, json_file)                       

        #recipes_list = data["recipes_list"]             #volatile variable, define in init
        #recipes_list[recipe] = ingredients
        

    def delete_recipe(self, recipe):
        with open("recipes.json", "r") as json_file:
            data = json.load(json_file)

        #recipes_list = data["recipes_list"]

        #if recipe not in data:
        #    return ("Recipe not archived")

        for recipes in data:
            if recipes["title"] == recipe:
                data.remove(recipes)             #del recipes
                break
        
        else:
            print("Recipe not archived")
            return

        #if recipe in recipes_list:
        #    del recipes_list[recipe]

        with open("recipes.json", "w") as json_file:
            json.dump(data, json_file)

    
    def edit_recipe(self, recipe, ingredients):
        with open("recipes.json", "r") as json_file:
            data = json.load(json_file)

        #if recipe not in data:
        #    return ("Recipe not archived")

        for recipes in data:
            #current = recipes["title"]
            if recipes["title"] == recipe:
                recipes["ingredients"] = ingredients
                break

        else:
            print("Recipe not archived")
            return

        #recipes_list = data["recipes_list"]

        #if recipe in recipes_list:
        #    recipes_list[recipe] = ingredients

        with open("recipes.json", "w") as json_file:
            json.dump(data, json_file)


    def search_recipe(self, recipe):
        with open("recipes.json", "r") as json_file:
            data = json.load(json_file)

        #recipes_list = data["recipes_list"]

        #if recipe in recipes_list:
        #    return recipes_list[recipe]

        for recipes in data:
                if recipes["title"] == recipe:
                    return recipes
                
        return "Recipe not archived"


    def search_ingedient(self, ingredient):         
        valid_recipes = []

        with open("recipes.json", "r") as json_file:
            data = json.load(json_file)

        #recipes_list = data["recipes_list"]

        #for recipe, ingredients in recipes_list.items():
        #    if ingredient in ingredients:
        #        valid_recipes.append(recipes_list[recipe])

        for recipes in data:
            for items in recipes["ingredients"]:
                if items == ingredient:
                    valid_recipes.append(recipes)

        if len(valid_recipes) <= 0:
            return "No recipes contain this ingredient"

        return valid_recipes

    
if __name__ == "__main__":
    #banana_bread_title = {"title": "banana bread"}
    #banana_bread_ing = {"ingredients": ["bananas", "flour", "eggs"]}
    
    test = Recipes()

    #test.add_recipe("banana bread", ["bananas", "flour", "eggs"])

    #test.delete_recipe("dgsdgsdg")

    #test.edit_recipe("ghjjrtyg", ["i", "y", "t"])

    #print(test.search_recipe("popcorn"))

    #print(test.search_ingedient("oranges"))

    test.add_recipe("banana bread", ["bananas", "eggs", "flour"])
    test.add_recipe("pizza", ["tomatoes", "flour", "cheese"])
    test.add_recipe("salad", ["lettuce", "tomatoes", "onions"])
    test.add_recipe("chicken and broccoli", ["chicken", "broccoli", "soy sauce"])

    test.delete_recipe("salad")
    print(test.search_recipe("salad"))
    test.add_recipe("pizza", ["tomatoes", "flour", "cheese"])

    test.edit_recipe("pizza", ["tomatoes", "flour", "cheese", "pepperoni"])
    print(test.search_recipe("pizza"))

    #print(test.search_recipe("popcorn"))
    #test.edit_recipe("salad", ["lettuce", "tomato", "eggs"])

