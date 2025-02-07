import threading
import requests
from time import time


# Function to make a web request
def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} with status code: {response.status_code}")


# Run multiple web requests in threads
def run_threads():
    threads = []
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/get",
        "https://httpbin.org/get",
        "https://httpbin.org/get",
    ]

    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# Benchmarking code
if __name__ == "__main__":
    start_time = time()
    run_threads()
    end_time = time()
    print(f"Time taken to fetch URLs: {end_time - start_time:.4f} seconds")
