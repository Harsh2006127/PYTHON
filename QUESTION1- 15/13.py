contacts = {}

while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add / Store Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update / Modify Contact")
    print("5. Remove Contact")
    print("6. Discard All Contacts")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print("Contact added successfully.")

        case 2:
            if not contacts:
                print("No contacts available.")
            else:
                print("\nStored Contacts:")
                for name, phone in contacts.items():
                    print(name, ":", phone)

        case 3:
            name = input("Enter name to search: ")
            if name in contacts:
                print("Contact found:", name, "->", contacts[name])
            else:
                print("Contact not found.")

        case 4:
            name = input("Enter name to update: ")
            if name in contacts:
                new_phone = input("Enter new phone number: ")
                contacts[name] = new_phone
                print("Contact updated successfully.")
            else:
                print("Contact not found.")

        case 5:
            name = input("Enter name to remove: ")
            if name in contacts:
                del contacts[name]
                print("Contact removed.")
            else:
                print("Contact not found.")

        case 6:
            contacts.clear()
            print("All contacts discarded.")

        case 7:
            print("Exiting Contact Book.")
            break

        case _:
            print("Invalid choice. Please try again.")