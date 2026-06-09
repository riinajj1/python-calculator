# Import math module

import math

# Function to validate integer input

def get_integer(prompt):

    while True:

        try:
            return int(input(prompt))

        except ValueError:
            print("Invalid input!")

# Ask user for numbers

def main():

    number_1 = get_integer("Enter first number: ")
    number_2 = get_integer("Enter second number: ")

# Main program loop

    while True:


# Display menu and selected numbers

        print("""
        (1) +
        (2) -
        (3) *
        (4) /
        (5) sin(number1/number2)
        (6) cos(number1/number2)
        (7) Change numbers
        (8) Exit
        """)

        print("Selected numbers:", number_1, number_2)

        choice = get_integer("Make a choice (1-8): ")

# Calculate result

        if choice == 1:
            print("Result:", number_1 + number_2)

        elif choice == 2:
            print("Result:", number_1 - number_2)

        elif choice == 3:
            print("Result:", number_1 * number_2)

        elif choice == 4:
            if number_2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", number_1 / number_2)

        elif choice == 5:
            if number_2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", math.sin(number_1 / number_2))

        elif choice == 6:
            if number_2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", math.cos(number_1 / number_2))

        elif choice == 7:
            number_1 = get_integer("Enter first number: ")
            number_2 = get_integer("Enter second number: ")

        elif choice == 8:
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
        main()
