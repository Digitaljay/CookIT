import json
new_one={}
keys_counter={}

# with open("recipes_raw_nosource_fn.json", "r") as json_file:
#     data=json.load(json_file)
#     for key in data:
#         for key_in in data[key]:
#             if key_in not in keys_counter:
#                 keys_counter[key_in]=0
#             keys_counter[key_in]+=1
#
# print(keys_counter)
with open("recipes_raw_nosource_fn.json", "r") as json_file:
    data=json.load(json_file)
    for key in data:
        try:
            ings=data[key]["ingredients"]
            inst=data[key]["instructions"]
            title=data[key]["title"]

            if len(ings)==0 or len(inst)==0 or len(title)==0:
                print(data[key])
                print()
            else:
                new_one[key]=data[key]
        except:
            print(data[key])
            print()

with open ("cleaned_recipes.json", "w") as dump_file:
    json.dump(new_one, dump_file)

print(len(new_one))
