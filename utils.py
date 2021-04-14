class Fridge():
    def __init__(self):
        self.product_list=[]
        with open("fridge.txt") as fridge:
            for food_name in fridge.readlines():
                self.product_list.append(food_name.strip())
        self.volume=len(self.product_list)
    def ings2mask(self, ings:list):
        mask = ["0" for i in range(self.volume)]
        for i in ings:
            try:
                ing_index=self.product_list.index(i)
                mask[ing_index]="1"
            except:
                print("Wrong ingredient, can't find " + i)
        return int(''.join(mask), 2)
    # def mask2ings(self, mask:int):
    #     bin_up=str(bin(mask))[2:]
    #     bin_up = (self.volume-len(bin_up))*"0"+bin_up
    #     ingredients = set()
    #     for bit_index in range(self.volume):
    #         if bin_up[bit_index]=="1":
    #             ingredients.add(self.product_list[i])
