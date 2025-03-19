# Ensure that the user input is a number and within the limits
while True:
    try:
        # Ask the user to input a number from 0 - 1000
        number = int(input("Please input a number from 0 to 1000 only: "))
        if 0 <= number <= 1000:
            break
        else:
            print("Invalid input! Please enter a number between 0 and 1000.")
    except ValueError:
        print("Invalid input. Please only input numbers")

# Print the result with trailing zeros to complete 6 digits
print(f'{number:06}')