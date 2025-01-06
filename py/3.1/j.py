text = ""
while (s := input()) != "ФИНИШ":
    text += s.lower()
top_char = ""    
max_count = 0
for char in text:
    if char == " ":
        continue
    count = text.count(char)
    if count > max_count or (count == max_count and char < top_char):
        top_char = char
        max_count = count
print(top_char)
