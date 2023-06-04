def sell_tickets():
    max_tickets = 5
    tickets_sold = 0
    exit_code = "xxx"

    while max_tickets > 0:
        if max_tickets == 1:
            print("*** There is one ticket left ***")
        else:
            print(f"There are {max_tickets} tickets left.")

        name = input("Enter your name: ")
        if name.lower() == exit_code:
            print(f"Ticket sales completed. {tickets_sold} tickets were sold.")
            break

        tickets_sold += 1
        max_tickets -= 1

    if tickets_sold == 0:
        print("No tickets were sold.")
    elif max_tickets == 0:
        print("There are no more tickets available.")

# Call the function to sell tickets
sell_tickets()





