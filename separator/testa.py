from deep_translator import MyMemoryTranslator
import json
import time
result={}
counter=0
with open("data.json", "r") as json_file:
    data=json.load(json_file)
    for key in data:
        recipe={}
        to_trans = []

        try:
            to_trans.append(data[key]["instructions"])
        except KeyError:
            to_trans.append('none')

        try:
            to_trans+=data[key]['ingredients']
        except KeyError:
            to_trans.append("none")

        try:
            to_trans.append(data[key]["title"])
        except KeyError:
            to_trans.append('none')

        recipe['instructions']=MyMemoryTranslator(source="en", target="ru").translate(to_trans[0])
        time.sleep(0.3)
        recipe['ingredients']=MyMemoryTranslator(source="en", target="ru").translate_batch(to_trans[1:-1])
        time.sleep(0.3)
        recipe["title"]=MyMemoryTranslator(source="en", target="ru").translate(to_trans[-1])
        time.sleep(0.3)

        result[key]=recipe


        counter+=1
        if not counter%500:
            print(counter)
        # for key_in in data[key]:
        #     inst, ing, tit=
        #     translated_value=None
        #     if type(data[key][key_in])==str:
        #         translated_value=MyMemoryTranslator(source="en", target="ru").translate(text=data[key][key_in])
        #     elif type(data[key][key_in])==list:
        #         translated_value = [MyMemoryTranslator(source="en", target="ru").translate(text=i) for i in data[key][key_in]]
        #
        #     recipe[key_in]=translated_value
        # result[key]=recipe

with open("translated.json", "w") as dump_file:
    json.dump(obj=result,fp=dump_file)

# with open("sep_clean/1.txt", "r") as file:
#     en_text=file.read()
#     translated = MyMemoryTranslator(source="en", target="ru").translate(text=en_text)
#     print(translated)
