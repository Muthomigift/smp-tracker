#in vs code requires pip install requests
import requests

url = "https://jsonplaceholder.typicode.com/users?"

response = requests.get(url)

print("status code:", response.status_code)
data = response.json()
print("User Data", data)