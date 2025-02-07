import threading
from math import factorial
from time import time


# Function to calculate the factorial of a large number
def calculate_factorial(n):
    return factorial(n)


# Run the factorial calculation in multiple threads
def run_threads():
    threads = []
    results = []
    numbers = [
        100000,
        100000,
        100000,
        100000,
    ]  # List of numbers to calculate factorial for

    for number in numbers:
        thread = threading.Thread(
            target=lambda n=number: results.append(calculate_factorial(n))
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


# Benchmarking code
if __name__ == "__main__":
    start_time = time()
    run_threads()
    end_time = time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
