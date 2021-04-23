import pandas as pd
from fridge_util import Fridge

ingredients_i_have = ["mint", "milk", "banana", "strawberr", "milk", "honey", "cheese"]

correlation_matrix=pd.read_csv("correlations.csv", delimiter=',').to_numpy()
fridge=Fridge()

ingredients_indexes = fridge.ings2indexes(ingredients_i_have)
for inga in ingredients_indexes:
    for ingb in ingredients_indexes:
        print(fridge.indexes2ings([inga, ingb]), correlation_matrix[inga][ingb+1])
