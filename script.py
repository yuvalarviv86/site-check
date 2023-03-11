import requests
import time

# Get user input
url = input("Enter website URL to check: ")
print(f"Now monitoring {url}...")

while True:
    # Ping website to check if it's up or down
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\033[1m\033[92mWebsite is UP\033[0m")
        else:
            print("\033[1m\033[91mWebsite is Down\n\n" + "Website is Down\n" * 5 + "\033[0m")

    except requests.exceptions.RequestException as e:
        print("\033[1m\033[91mWebsite is Down\n\n" + "Website is Down\n" * 5 + "\033[0m")

    # Wait for 1 minute before checking the website status again
    time.sleep(60)
