import requests
from pprint import pprint


url = "https://fakestoreapi.com/carts"

response = requests.get(url).json()

pprint(response)


