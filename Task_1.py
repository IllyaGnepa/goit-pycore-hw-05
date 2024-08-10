def caching_fibonacci():
    # Create an empty dictionary to cache the results
    cache = {}

    # Inner function to calculate the Fibonacci number
    def fibonacci(n):
        try:
            # Check if n is an integer
            if not isinstance(n, int):
                raise TypeError("The argument must be an integer.")
            # Check if n is a non-negative number
            if n < 0:
                raise ValueError("The argument must be a non-negative integer.")
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            # If the value is already in the cache, return it
            if n in cache:
                return cache[n]
            # Otherwise, calculate the value recursively, store it in the cache, and return the result
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

        except TypeError as te:
            print(f"Type Error: {te}")
        except ValueError as ve:
            print(f"Value Error: {ve}")
        except Exception as e:
            print(f"Unknown Error: {e}")

    # Return the inner function fibonacci
    return fibonacci

# Example usage
fibonacci = caching_fibonacci()

# Output several Fibonacci numbers
print(fibonacci(10))  # Outputs 55
print(fibonacci(20))  # Outputs 6765
print(fibonacci(-5))  # Outputs an error message
print(fibonacci("text"))  # Outputs an error message
