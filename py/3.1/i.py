while (s := input()) != "":
    pos = s.find("#")
    if pos == -1:
        print(s)
    elif pos > 0:
        print(s[:pos])
