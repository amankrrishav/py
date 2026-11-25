# 2 types of modules:
# built-in (math, os) and external (requests)
# unused imports appear dimmed in the editor

import math
import mymod
import requests

print(math.sqrt(100))  # 10.0

mymod.smtg()

resp = requests.get("https://www.google.com", timeout=10)
print(resp.status_code)  # 200 = OK
print(resp.text[:200])   # first 200 chars of the HTML
# resp.json() if the endpoint returns JSON