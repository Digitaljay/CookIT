import json
from googletrans import Translator
from fridge_util import Fridge


class Searcher():
    def __init__(self, products_available: list):
        self.fridge = Fridge()
        self.products_available = self.fridge.ings2mask(products_available)
        with open("adapted_recipes.json", "r") as json_file:
            self.recipes = json.load(json_file)
        self.suitable_codes = self.search_suitable()
        self.suitable_recipes = self.decode2recipe()

    def search_suitable(self):
        suitable = []
        max_similarity = 0
        for recipe in self.recipes:
            recipe_len = str(bin(self.recipes[recipe])).count("1")
            try:
                similarity = str(bin(self.recipes[recipe] & self.products_available)).count("1") / recipe_len
                if similarity > max_similarity:
                    suitable = [recipe]
                    max_similarity = similarity
                elif similarity == max_similarity:
                    suitable.append(recipe)
            except ZeroDivisionError:
                pass
        return suitable

    def decode2recipe(self):
        recipes_text = []
        with open("recipes_raw_nosource_fn.json", "r") as json_file:
            decoder = json.load(json_file)
            for recipe_code in self.suitable_codes:
                recipes_text.append(decoder[recipe_code])
        return recipes_text

    def get_suitable_recipes(self, language = "en"):
        if language=="en":
            return self.suitable_recipes
        else:
            translator = Translator()
            translated_recipes = []
            for recipe in self.suitable_recipes:
                translated_recipe = {}
                for key in recipe:
                    translated_value=None
                    print(type(recipe[key]), recipe[key])
                    if type(recipe[key])==str:
                        translated_value=translator.translate(recipe[key], dest=language).text
                    else:
                        translated_value = [translator.translate(i, dest=language).text for i in recipe[key]]
                    recipe[key]=translated_value
                translated_recipes.append(translated_recipe)
            return translated_recipes

