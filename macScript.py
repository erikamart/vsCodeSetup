import math
import sys
from os import rename

import requests

# #############################
# Code before min 47:50
# #####################
# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Corey'))
r = requests.get("https://coreyms.com")
print(r.status_code)
# print(r.ok)
# #############################

# #############################
# Code after min 47:55
# ####################
# name = input("Your Name? ")
# print("Hello,", name)

# #############################
