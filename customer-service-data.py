# Task 1: Customer Service Ticket Tracket
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Implement functions for opening a new service ticket, updating the status of an existing ticket, and displaying all tickets or filtering by status
def open_ticket(tickets, tid, name, issue, status):
    if tid not in tickets:
        if status == "open" or status == "closed":
            tickets[tid] = {"Customer": name, "Issue": issue, "Status": status}
            print(f"'{tid}' with customer '{name}' opened.")
        else:
            print("Invalid status. Please enter either 'open' or 'closed'.")
    else:
        print(f"'{tid}' already exists. Please try again.")

def update_status(tickets, tid, status):
    if tid in tickets:
        if status == "open" or status == "closed":
            tickets[tid].update({"Status": status})
            print(f"'{tid}' updated to '{status}' status.")
        else:
            print("Invalid status. Please enter either 'open' or 'closed'.")
    else:
        print(f"'{tid}' not found. Please try again.")

def display_all_tickets(tickets):
    for ticket, info in tickets.items():
        print(f"{ticket}:")
        print(f"  Customer: {info["Customer"]}\n  Issue: {info["Issue"]}\n  Status: {info["Status"].capitalize()}")

def display_filtered_tickets(tickets, filter):
    if filter_input == "open":
        for ticket, info in tickets.items():
            if "open" in info["Status"]:
                print(f"{ticket}:")
                print(f"  Customer: {info["Customer"]}\n  Issue: {info["Issue"]}\n  Status: {info["Status"].capitalize()}")
            else:
                continue
    elif filter_input == "closed":
        for ticket, info in tickets.items():
            if "closed" in info["Status"]:
                print(f"{ticket}:")
                print(f"  Customer: {info["Customer"]}\n  Issue: {info["Issue"]}\n  Status: {info["Status"].capitalize()}")
            else:
                continue
    else:
        print("Invalid status. Please enter either 'open' or 'closed'.")

# Display a menu for the customer service data program and collect user input to utilize functions
print("Customer Service Data Program")
while True:
    print("\n1. Open a new service ticket\n2. Update the status of an existing ticket\n3. Display all tickets or filter by status\n4. Quit the program")
    choice_input = input("Enter your choice: ")
    
    if choice_input == "1":
        tid_input = input("Enter the new ticket ID: ").capitalize()
        name_input = input("Enter the customer name: ").title()
        issue_input = input("Enter the issue description: ").capitalize()
        status_input = input("Enter the status (open/closed): ").lower()
        open_ticket(service_tickets, tid_input, name_input, issue_input, status_input)
        
    elif choice_input == "2":
        tid_input = input("Enter the ticket ID: ").capitalize()
        status_input = input(f"Enter the updated status of '{tid_input}': ").lower()
        update_status(service_tickets, tid_input, status_input)
    
    elif choice_input == "3":
        print("The program can display all tickets or filter them by status.")
        display_input = input("Enter what the program should display (all/filtered): ")
        if display_input == "all":
            display_all_tickets(service_tickets)
        elif display_input == "filtered":
            filter_input = input("Enter what ticket status the program should filter (open/closed): ")
            display_filtered_tickets(service_tickets, filter_input)
        else:
            print("Invalid input. Please enter either 'all' or 'filtered'.")
    
    elif choice_input == "4":
        print("Quitting the program...")
        break
    
    else:
        print("Invalid choice. Please try again.")