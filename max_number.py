def sell_tickets():
    max_tickets = 1
    tickets_sold = 0
    exit_code = "nvm"

    while max_tickets > 0:
        if max_tickets == 1:
            print("\n *** There is one ticket left *** \n")
        else:
            print(f" \n ***There are {max_tickets} tickets left*** \n")

        name = input("Enter your name: ")
        if name.strip() == "":
            print("Invalid input. Name cannot be blank.")
            continue

        age_str = input("Enter your age: ")
        if not age_str.isdigit():
            print("Invalid input. Age must be a number.")
            continue

        age = int(age_str)
        if age < 12 or age > 120:
            print("Sorry, you are not eligible to watch the movie.")
            continue

        if name.lower() == exit_code:
            print(f"Ticket sales completed. {tickets_sold} tickets were sold.")
            break

        if age >= 12 and age <= 15:
            ticket_price = 7.50
            profit = 2.50
        elif age >= 16 and age <= 64:
            ticket_price = 10.50
            profit = 5.50
        else:
            ticket_price = 6.50
            profit = 1.50

        tickets_sold += 1
        max_tickets -= 1

        print(f"Ticket price: ${ticket_price}")

    if tickets_sold == 0:
        print("No tickets were sold.")
    elif max_tickets == 0:
        print("There are no more tickets available.")
        print(f"Total Profits ${profit}")
    

# Call the function to sell tickets
sell_tickets()








