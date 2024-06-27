# CODSOFT_TASK_05
Sure, here is a theoretical explanation of how the contact management system works:

### Overview

The contact management system is designed to allow users to manage a list of contacts. Each contact includes details like name, phone number, email, and address. The system provides functionality to add new contacts, view existing contacts, search for contacts, update contact information, and delete contacts. The contacts are stored in a JSON file for persistence, meaning the data is saved even when the program is not running.

### Detailed Explanation

1. **Data Storage**:
   - The contacts are stored in a JSON file. JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. Using JSON allows the contact information to be saved in a structured format that can be easily loaded and modified by the program.

2. **Loading Contacts**:
   - When the program starts, it attempts to load the contacts from the JSON file. If the file does not exist, the program initializes an empty list of contacts. This ensures that the program has a list of contacts to work with during its execution.

3. **Saving Contacts**:
   - After any operation that modifies the contact list (adding, updating, or deleting a contact), the program saves the updated list back to the JSON file. This ensures that changes are persistent and will be available the next time the program runs.

4. **Adding a Contact**:
   - The user is prompted to enter the details for a new contact, including name, phone number, email, and address. The program checks if a contact with the same name already exists to prevent duplicates. If the contact is new, it is added to the list and the updated list is saved to the JSON file.

5. **Viewing Contacts**:
   - The program can display a list of all saved contacts. This list includes the names and phone numbers of all contacts, making it easy for the user to see an overview of their contacts.

6. **Searching for a Contact**:
   - The user can search for a contact by name or phone number. The program scans through the contact list and displays any contacts that match the search query. This helps the user quickly find specific contacts without manually browsing through the entire list.

7. **Updating a Contact**:
   - The user can update the details of an existing contact. The program prompts the user to enter the name of the contact they want to update, and then asks for the new details. The contact information is updated and the changes are saved to the JSON file.

8. **Deleting a Contact**:
   - The user can delete a contact by specifying the contact's name. The program removes the contact from the list and saves the updated list to the JSON file.

9. **User Interface**:
   - The user interacts with the program through a simple text-based menu. The menu provides options for adding, viewing, searching, updating, and deleting contacts, as well as exiting the program. The user selects an option by entering the corresponding number, and the program performs the requested operation.

10. **Program Execution**:
    - The main function of the program contains the logic to display the menu and handle user input. It continuously displays the menu and processes user choices until the user decides to exit the program. This loop ensures that the user can perform multiple operations in one session without restarting the program.

### Summary

The contact management system is a console-based application that allows users to manage their contacts efficiently. It uses a JSON file for persistent storage, ensuring that contact data is not lost between sessions. The program provides functionalities to add, view, search, update, and delete contacts, all accessible through a user-friendly text-based interface. The modular design of the functions makes the code easy to read, maintain, and extend with additional features if needed.
