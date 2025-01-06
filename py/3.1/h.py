for _ in range(int(input())):
    pos = input().find("зайка")
    if pos != -1:
        print(pos + 1)
    else:
        print("Заек нет =(")
