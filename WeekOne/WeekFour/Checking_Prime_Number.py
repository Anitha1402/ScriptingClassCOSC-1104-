# Author: Anita Mohan (100884879)
# Date: 10-10-2024
"""Simple Application on Analyzing whether given number is a prime number or not
    and providing some additional information about it"""

#Checking if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#Checking the largest prime number less than n.
def previous_prime(n):
    for num in range(n - 1, 1, -1):
        if is_prime(num):
            return num
    return None

#checking the smallest prime number greater than n.
def next_prime(n):
    num = n + 1
    while True:
        if is_prime(num):
            return num
        num += 1

#Retriving a list of factors of n
def list_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

#Main Method
def main():
    while True:
        user_input = input("Please enter a positive whole number: ")

        # Check if the input is a positive whole number
        if user_input.isdigit():  # Check if the input is all digits
            number = int(user_input)

            if number <= 0:
                print("The given number is not a positive whole number. Please try again.")
                continue

            # Get previous prime, check if number is prime, getting next prime
            prev_prime = previous_prime(number)
            is_number_prime = is_prime(number)
            next_prime_number = next_prime(number)

            # Printing output results
            if prev_prime is not None:
                print(f"The prime number before {number} is {prev_prime}.")
            else:
                print(f"There is no prime number before {number}.")

            if is_number_prime:
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
                factors = list_factors(number)
                print(f"The factors of {number} are: {factors}.")

            print(f"The next prime number after {number} is {next_prime_number}.")
            break  # Exit the loop after successful processing
        else:
            print("Invalid input. Please enter a positive whole number.")

if __name__ == "__main__":
    main()
