# Contact Information: Store name, phone number, email, and address for each contact.

    # Add Contact: Allow users to add new contacts with their details.
    # View Contact List: Display a list of all saved contacts with names and phone numbers.
    # Search Contact: Implement a search function to find contacts by name or phone number.
    # Update Contact: Enable users to update contact details.
    # Delete Contact: Provide an option to delete a contact.
    # User Interface: Design a user-friendly interface for easy interaction.


contacts = []  

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']}")
        print()

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if contact['Name'] == search_term or contact['Phone'] == search_term:
            print(contact)
            found = True
    if not found:
        print("No contact found.\n")

def update_contact():
    search_term = input("Enter name or phone number to update: ")
    for contact in contacts:
        if contact['Name'] == search_term or contact['Phone'] == search_term:
            print("Contact found. Enter new details:")
            contact['Name'] = input("Enter new name: ")
            contact['Phone'] = input("Enter new phone number: ")
            contact['Email'] = input("Enter new email: ")
            contact['Address'] = input("Enter new address: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    search_term = input("Enter name or phone number to delete: ")
    for contact in contacts:
        if contact['Name'] == search_term or contact['Phone'] == search_term:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.\n")

menu()
