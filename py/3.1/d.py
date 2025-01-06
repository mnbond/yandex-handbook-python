while (s := input()) != "":
    if s.endswith("@@@"):
        continue
    if s.startswith("##"):
        s = s[2:]
    print(s)
