from sys import stdin

print("\n".join(x[:x.find("#")] for x in stdin.readlines() if not x.startswith("#")))
