from google_trans_new import google_translator
from typing import Dict


def translate_recipe(recipe: Dict[str, str]):
    translator = google_translator()
    translated_recipe = {}
    for key in recipe:
        translated_value = None
        if type(recipe[key]) == str:
            translated_value = translator.translate(recipe[key], lang_tgt="ru")
        elif type(recipe[key]) == list:
            translated_value = [translator.translate(i, lang_tgt="ru") for i in recipe[key]]
        translated_recipe[key] = translated_value

    return translated_recipe


# usage example
print(translate_recipe({"Arctic Monkeys": "505",
                        "Poets of the Fall": "Carnival of Rust",
                        "Mushmellow": "Without you"
                        }))
