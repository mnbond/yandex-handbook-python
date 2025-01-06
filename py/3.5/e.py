from sys import stdin

result = set()
for word in stdin.read().split():
    n = len(word)
    if word[:n // 2].lower() == word[:(n - 1) // 2:-1].lower():
        result.add(word)
print("\n".join(sorted(result)))
