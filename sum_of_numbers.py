#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Apr. 28, 2025
# This program asks the user to enter a positive
# integer. It then calculates the sum of numbers from 0
# up to that integer.


# Define the main function.
def main():
    # Initialize the loop counter to zero.
    loop_counter = 0
    # Initialize the sum to zero.
    sum = 0
    # Get the positive integer from the user as a string.
    user_number_str = input("\nEnter a positive integer: ")

    # Try to check the validity of the user input.
    try:
        # Attempt to convert the entered string into an integer.
        user_number_int = int(user_number_str)

        # Check if the entered integer was really a positive one.
        if user_number_int > 0:
            # Proceed to the while loop to determine the sum of numbers.
            while loop_counter <= user_number_int:
                # Add the loop counter to the sum.
                sum = sum + loop_counter
                # Increment the loop counter by one.
                loop_counter = loop_counter + 1

            # Display the sum of numbers from 0 up to the desired number
            # to the user.
            print(f"\nThe sum of numbers from 0 to {user_number_int} is {sum}.")

        # Otherwise, the user entered a negative integer or zero.
        else:
            # Display to the user that they did not
            # enter a positive integer.
            print(f"\n{user_number_int} is not a positive integer.")

    # Runs if int() could not convert the user's string
    # input into an integer.
    except ValueError:
        # Display to the user that they did not
        # enter a positive integer.
        print(f"\n{user_number_str} is not a positive integer.")

    # Finally, run the exit message.
    finally:
        # Thank the user for using this program.
        print("\nThanks for using this program!")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
