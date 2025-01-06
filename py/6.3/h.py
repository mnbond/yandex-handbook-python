from requests import post
from json import dumps

address = "http://" + input() + "/users"
new_user = {x: input() for x in ["username", "last_name", "first_name", "email"]}
post(address, data=dumps(new_user))
