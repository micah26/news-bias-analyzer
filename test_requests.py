# test_requests.py - Testing if requests library works

# Import the requests library
import requests

print("Testing requests library...")
print("Making a simple internet request...\n")

# Let's test with a simple API that returns our IP address
# API = Application Programming Interface (a way to get data from internet)
response = requests.get("https://api.ipify.org?format=json")

# Check if it worked
if response.status_code == 200:  # 200 means "success"
    print("✅ Success! Requests library is working!")
    print(f"Response data: {response.json()}")
else:
    print("❌ Something went wrong")
    print(f"Error code: {response.status_code}")