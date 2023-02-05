import re

receipt_without_tip_unformatted = input("Please enter the sum ");
receipt_without_tip = float(re.sub("[a-z$£]", "", receipt_without_tip_unformatted)); #"[^\d.]"

print(f"Your receipt today is {receipt_without_tip}");

print(f"Would you like to leave a tip?");


answer = input("Please enter 'yes' or 'no': ")

if answer == "yes":
    print("Please choose one of the following tip options:")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    tip_choice = input("Enter the number of your choice: ")

    if tip_choice == "1":
        tip = receipt_without_tip * 0.1
    elif tip_choice == "2":
        tip = receipt_without_tip * 0.15
    elif tip_choice == "3":
        tip = receipt_without_tip * 0.2
    else:
        print("Invalid choice. Please try again.")
        tip = 0

else:
    tip = 0

total = receipt_without_tip + tip
print(f"Your total receipt with tip is {total}")



