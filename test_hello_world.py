# PR-1
from json import JSONDecodeError

import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parse_response_text = response.json()
    print(parse_response_text)
except JSONDecodeError:
    print("Response is not JSON format")
