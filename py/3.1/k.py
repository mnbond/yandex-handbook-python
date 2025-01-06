titles = []
for _ in range(int(input())):
    titles.append(input())
query = input().lower()
for title in titles:
    if query in title.lower():
        print(title)
