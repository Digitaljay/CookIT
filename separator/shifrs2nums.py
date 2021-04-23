import json

with open("data.json", "r") as json_file:
    data = json.load(json_file)

keys_dict = {}
keys_counter = 1

file_num = 1
dict_now = {}

counter = 0
for key in data:
    counter += 1
    counter %= 300
    if counter == 0:
        out_file = open("sep_kitanai/"+str(file_num) + ".json", 'w')
        json.dump(dict_now, out_file)
        file_num += 1
        dict_now = {}
    keys_dict[keys_counter] = key
    dict_now[keys_counter] = data[key]
    keys_counter += 1

out_file = open("sep_kitanai/"+str(file_num) + ".json", 'w')
json.dump(dict_now, out_file)

kd_file = open("keys_dict.json", 'w')
json.dump(keys_dict, kd_file)
