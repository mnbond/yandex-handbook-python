count = int(input())
first_player = input()
for _ in range(count - 1):
    first_player = min(first_player, input())
print(first_player)
