import requests

def check_api(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print("API is healthy")
        else:
            print("API is unhealthy:", response.status_code)

    except requests.exceptions.Timeout:
        print("API request timed out")

    except requests.exceptions.ConnectionError:
        print("Unable to connect to API")

    except requests.exceptions.RequestException as e:
        print("API request failed:", e)


check_api("https://example.com")
