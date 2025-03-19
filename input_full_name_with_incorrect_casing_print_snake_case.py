# Ask the user to input their full name
fullname = input("Please input your full name with incorect casing: ")
# Print the result using snake case
print(fullname.lower().replace(" ", "_"))