# test response
import requests
response = requests.get("https://catfact.ninja/fact")
print(response.status_code)
print(response.json())

# test user API 
response_user_api = requests.get("https://reqres.in/api/users?page=2")
print(response_user_api.status_code)
print(response_user_api.json())