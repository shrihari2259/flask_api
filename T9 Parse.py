import requests

# Example API endpoint that returns JSON
url = 'http://127.0.0.1:5000/items'

# Send a GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)
