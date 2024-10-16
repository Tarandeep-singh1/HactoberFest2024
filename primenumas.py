import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to find all prime numbers in a given range
def find_primes(start, end):
    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Example usage
start = 10
end = 50
primes_in_range = find_primes(start, end)
print(f"Prime numbers between {start} and {end}: {primes_in_range}")
