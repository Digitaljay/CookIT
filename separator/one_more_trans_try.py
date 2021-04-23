from google_trans_new import google_translator
translator = google_translator()
for file_num in range(1, 202):
    file_name="sep_kitanai/"+str(file_num)+".json"
    raw = open(file_name, "r").read()
    translated_value=translator.translate(raw, lang_tgt="ru")
    print(translated_value)
    break
