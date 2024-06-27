import json

# File to store contacts
contacts_file = 'contacts.json'


def load_contacts():
    try:
        with open(contacts_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    if name in contacts:
        print("Contact already exists.")
        return

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")


def search_contact(contacts):
    query = input("Enter name or phone number to search: ").lower()
    found = False

    for name, details in contacts.items():
        if query in name.lower() or query in details['phone']:
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print('-' * 20)
            found = True

    if not found:
        print("No matching contacts found.")


def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")
    address = input("Enter new address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
