import json

def __init__(self):
        with open("recipes.json", "r") as json_file:
            self.data = json.load(json_file)