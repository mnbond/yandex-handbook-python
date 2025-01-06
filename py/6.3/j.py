from requests import delete

address = "http://" + input() + "/users/" + input()
delete(address)
