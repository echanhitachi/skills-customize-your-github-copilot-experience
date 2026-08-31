# Task 1
def welcome_message():
    # Ask the user for their name, age, and favorite color
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")
    # Return a formatted welcome message
    return f"Hello, {name}! You are {age} years old and your favorite color is {color}."

# Task 2


def add_two_numbers():
    # Ask the user to enter two numbers
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    # Add them together, print and return the result
    result = first_number + second_number
    print(result)
    return result

# Task 3


def is_even(number):
    # Return True if number is even, False if odd
    return number % 2 == 0


if __name__ == "__main__":
    print(welcome_message())
    add_two_numbers()
    print(is_even(4))  # True
    print(is_even(5))  # False
