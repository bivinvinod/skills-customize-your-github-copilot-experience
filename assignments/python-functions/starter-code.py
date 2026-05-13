# Starter Code for Python Functions and Modules Assignment

# Task 1: Reusable helper functions

def format_greeting(name, favorite_color):
    # Return a greeting string using the provided values
    return f"Hello, {name}! Your favorite color is {favorite_color}."


def calculate_square_area(side_length):
    # Return the area of a square using the side length
    return side_length * side_length


def is_palindrome(text):
    normalized = ''.join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


# Task 2: Use a separate module for helpers
# You can move the helper functions above into a file named helpers.py
# and then import them here like:
# from helpers import format_greeting, calculate_square_area, is_palindrome


def main():
    name = input("Enter your name: ")
    color = input("Enter your favorite color: ")
    print(format_greeting(name, color))

    side = float(input("Enter the side length of a square: "))
    area = calculate_square_area(side)
    print(f"The area of the square is {area}.")

    word = input("Enter a word or phrase to check for palindrome: ")
    if is_palindrome(word):
        print("That is a palindrome!")
    else:
        print("That is not a palindrome.")


if __name__ == "__main__":
    main()
