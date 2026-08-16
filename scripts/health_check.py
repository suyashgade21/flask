import sys
import requests


URL = "http://localhost:5000/health"


print(f"Checking application health: {URL}")

try:
    response = requests.get(URL, timeout=5)

    if response.status_code == 200:
        data = response.json()

        if data.get("status") == "healthy":
            print("Application is healthy!")
            sys.exit(0)

    print(f"Health check failed. HTTP status: {response.status_code}")
    sys.exit(1)

except requests.exceptions.RequestException as error:
    print(f"Unable to connect to application: {error}")
    sys.exit(1)
