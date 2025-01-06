from sys import stdin
from requests import put
from json import dumps

address = "http://" + input() + "/users/" + input()
updates = {x[0]: x[1] for x in [line.strip().split("=") for line in stdin.readlines()]}
put(address, data=dumps(updates))
