import requests

# url = "https://icanhazdadjoke.com/search?term=cat"
# response = requests.get(url, headers = {"Accept": "application/json"},  params={"term": "cat", "limit": 1})
# data = response.json()
# print(data["results"])

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(url, headers = {"Accept": "application/json"},  params={"term": user_input, "limit": 1}).json()
print(response['results'][0]['joke'])