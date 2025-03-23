# test response
import requests
response = requests.get("https://catfact.ninja/fact")
print(response.status_code)
print(response.json())

# test user API 
response_user_api = requests.get("https://reqres.in/api/users?page=2")
print(response_user_api.status_code)
print(response_user_api.json())

#Requests Library (for API Calls)
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

# simple test run
import requests
def test_api():
    response_github_api = requests.get("https://api.github.com")
    assert response_github_api.status_code == 200
    print("GitHub API is running!!!!!!!!!!!!!!!")

if __name__ == "__main__":
    test_api()
