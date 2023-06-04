def sell_tickets():
    max_tickets = 150
    tickets_sold = 0
    exit_code = "xxx"
    loop_counter = 0

    while True:
        loop_counter += 1
        if loop_counter > 5:
            print("Loop limit reached. Exiting the program.")
            break

        if tickets_sold >= max_tickets:
            print("Sorry, all tickets have been sold.")
            break

        ticket_count_left = max_tickets - tickets_sold
        print(f"You have {ticket_count_left} seats left.")

        name = input("Enter your name (or 'xxx' to exit): ")
        if name.lower() == exit_code:
            print("Exiting the program.")
            break

        tickets_sold += 1
        print(f"Ticket {tickets_sold} sold for {name}!")

    print("Ticket sales completed.")

# Call the function to sell tickets
sell_tickets()

