def sell_tickets():
    max_tickets = 5
    tickets_sold = 0
    exit_code = "xxx"
    loop_counter = 5

    while True:
        loop_counter -= 1
        if loop_counter < 5:
            print("There is no more tickets avalible sorry.")
            break
        if loop_counter == 1
            print("*** There is one ticket left ***")
      

        ticket_count_left = max_tickets - tickets_sold
        print(f"There is {ticket_count_left} seats left.")

        name = input("Enter your name: ")
        if name.lower() == exit_code:
            break

        tickets_sold += 1

# Call the function to sell tickets
sell_tickets()

