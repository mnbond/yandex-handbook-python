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
result = ""
for char in input():
    new_char = RULES.get(char.upper(), char)
    if char.islower():
        new_char = new_char.lower()
    result += new_char
print(result)
