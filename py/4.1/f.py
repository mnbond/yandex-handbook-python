def modern_print(phrase):
    if phrase not in used_phrases:
        used_phrases.add(phrase)
        print(phrase)


used_phrases = set()