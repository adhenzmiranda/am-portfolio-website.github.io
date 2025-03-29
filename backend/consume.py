import requests

try:
    response = requests.get("http://127.0.0.1:8000/projects")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")