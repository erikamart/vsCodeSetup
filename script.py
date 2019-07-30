# import math
# import sys
# from os import rename

import requests

# # code-runner run button at top right can be used for this type of code
# # However, to run input/output code you can't use that button. Refer to
# # script2.py file for an example.

# print(sys.version)
# print(sys.executable)


# def greet(who_to_greet):
#     greeting = "Hello, {}".format(who_to_greet)
#     return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
