def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

show_instructions = yes_no("Have you been here before? (yes/no): ")
if not show_instructions:
    print("**************************")
    print("        INSTRUCTIONS      ")
    print("**************************")
    print("1. Enter your name.")
    print("2. Enter your age.")
    print("3. Make the payment (cash or credit).")
    print("4. You will be entered into the draw to win a prize.")
    print("5. If your name is called out, please come to collect your prize.")
    print("**************************")



      