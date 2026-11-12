# Suppose your Python script calls an API.
# - First attempt fails.
# - Retry after 1 second.
# - Second attempt fails.
# - Retry after 2 seconds.
# - Third attempt fails.
# - Retry after 4 seconds.
# - Stop after the maximum number of attempts.
# This is called exponential backoff.

import time
import requests

def call_api(url, max_retries=3):

    for attempt in range(max_retries + 1):
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                print("API is healthy")
                return response

            if response.status_code < 500:
                print("Non-retryable error:", response.status_code)
                return None

            print("Server error:", response.status_code)

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)

        if attempt < max_retries:
            delay = 2 ** attempt
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)

    print("Maximum retries exceeded")
    return None
