RULES = {
    "А": "A", "Б": "B", "В": "V", "Г": "G",
    "Д": "D", "Е": "E", "Ё": "E", "Ж": "Zh",
    "З": "Z", "И": "I", "Й": "I", "К": "K",
    "Л": "L", "М": "M", "Н": "N", "О": "O",
    "П": "P", "Р": "R", "С": "S", "Т": "T",
    "У": "U", "Ф": "F", "Х": "Kh", "Ц": "Tc",
    "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ъ": "",
    "Ы": "Y", "Ь": "", "Э": "E", "Ю": "Iu", 
    "Я": "Ia"
}

with open("cyrillic.txt", "r", encoding="UTF-8") as file_in:
    text = file_in.read()

translit = ""
for char in text:
    new_char = RULES.get(char.upper(), char)
    if char.islower():
        new_char = new_char.lower()
    translit += new_char

with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(translit)
