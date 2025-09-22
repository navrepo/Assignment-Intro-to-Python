print("\n Movie Tickets Pricing \n")


name = input("\n Enter your name: ")
age = float(input("Enter your age: "))
print("Child Ticket (under 13): $8")
print("Adult Ticket (13−64): $12")
print("Senior Ticket (65+): $9")
tickets = int(input("How many tickets would you like? "))
print("\n")

if age < 13:
    result = 8 * tickets
    print("=== MOVIE TICKET RECEIPT ===")
    print(f"Customer: {name}")
    print(f"Ticket Type: Child ($8.00 each)")
    print(f"Quantity: {tickets}")
    print(f"Total: ${result:.2f}")
    print("\n Thank you for your purchase!")

elif age >= 13 and age < 65:
    result = 12 * tickets
    print("=== MOVIE TICKET RECEIPT ===")
    print(f"Customer: {name}")
    print(f"Ticket Type: Adult ($12.00 each)")
    print(f"Quantity: {tickets}")
    print(f"Total: ${result:.2f}")
    print("\n Thank you for your purchase!")
    
elif age >= 65: 
    result = 9 * tickets
    print("=== MOVIE TICKET RECEIPT ===")
    print(f"Customer: {name}")
    print(f"Ticket Type: Senior ($9.00 each)")
    print(f"Quantity: {tickets}")
    print(f"Total: ${result:.2f}")
    print("\n Thank you for your purchase!")

