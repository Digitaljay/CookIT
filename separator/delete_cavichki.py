import re
for file_num in range(1, 202):
    file_name="sep_kitanai/"+str(file_num)+".json"
    raw = open(file_name, "r").read()
    result = re.sub("[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0 123456789,.:[{}\]]", '', raw)
    write_in = open("sep_clean/"+str(file_num)+'.txt', "w")
    write_in.write(result)



