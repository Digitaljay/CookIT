import pandas as pd
from fridge_util import Fridge
class Generator():
    def __init__(self):
        self.correlation_matrix=pd.read_csv("correlations.csv", delimiter=',').to_numpy()
    def top5recipes(self, ingredients:list):
        ingredients_indexes = Fridge().ings2indexes(ingredients)
        recipes_scores=[]
        for kit in range(1, 2**len(ingredients)):
            kit_mask=str(bin(kit))[2:]
            kit_mask="0"*(len(ingredients)-len(kit_mask))+kit_mask
            totake=[]
            for i in range(len(ingredients)):
                if kit_mask[i]=="1":
                    totake.append(ingredients_indexes[i])
            score=self.count_correlation(totake)
            recipes_scores.append((score, totake))
        recipes_scores.sort(reverse=True)
        return recipes_scores[:5]

    def count_correlation(self, indexes):
        ressa=0
        for inda in range(len(indexes)-1):
            for indb in range(inda, len(indexes)):
                ressa+=2*(self.correlation_matrix[inda][indb+1])
        return ressa/(len(indexes)**2)

gen=Generator()
ingredients_i_have = ["garlic", "milk", "chicken", "pepper", "cabbage", "sugar", "cheese"]
print(gen.top5recipes(ingredients_i_have))
