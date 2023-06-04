def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

show_instructions = yes_no("Have you watched this before? (yes/no): ")
if not show_instructions:
    print("Instructions")


      