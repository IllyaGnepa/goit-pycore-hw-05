import re
from typing import Callable

# Function to generate numbers from the text
def generator_numbers(text: str):
    try:
        # Using regex to find all valid numbers in the format X.XX
        numbers = re.findall(r'\b\d+\.\d{2}\b', text)
        # Convert found numbers to float and yield them
        for num in numbers:
            yield float(num)
    except (TypeError, ValueError) as e:
        # Handle unexpected errors during number extraction and conversion
        print(f"Error while processing text: {e}")
        return

# Function to sum up all the numbers
def sum_profit(text: str, func: Callable):
    try:
        # Calculate the sum of all numbers provided by the generator
        total_sum = sum(func(text))
        return total_sum
    except TypeError as e:
        # Handle the case where the generator did not yield numbers properly
        print(f"Error while summing up numbers: {e}")
        return None

# Example
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


