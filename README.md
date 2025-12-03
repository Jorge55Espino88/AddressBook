# Address Book - Phase 1: Procedural Implementation

A simple command-line address book application built with Python, focusing on procedural programming.

## Description

This is the first phase of a multi-phase address book project. In this phase, we implement a basic contact management system using procedural programming in Python. Users can add, view, update, and delete contacts through a console-based menu. Each contact includes an ID (generated with date and sequence), name, last name, telephone, cell phone, and email.

The goal is to demonstrate fundamental Python concepts like functions, loops, dictionaries, input validation, and date handling, while building a foundation for future object-oriented and GUI phases.

**Key Features:**
- Unique ID generation using current date and incremental counter (e.g., "20231015-1").
- Input validation for required fields and data types (e.g., numeric phones, valid emails).
- Menu-driven interface for easy navigation.
- Error handling for invalid inputs and missing contacts.

**Technologies Used:**
- Python 3.x
- Standard libraries: `datetime` for ID generation.

**Programming Paradigm:** Procedural (functions and global data structures).

## Installation

1. Clone the repository: git clone https://github.com/Jorge55Espino88/AddressBook.git

2. Ensure Python 3.x is installed.

3. Run the application: python main.py

## Usage

1. Start the program and enter your name.
2. Choose an option from the menu:
- 1: View all contacts.
- 2: View a specific contact by ID.
- 3: Add a new contact (with validations).
- 4: Update an existing contact.
- 5: Delete a contact.
- 6: Exit.
3. Follow the prompts to interact with the address book.

Example:
- Add a contact: Enter name, last name, phone numbers, and email.
- Update: Enter the ID and modify fields (leave blank to keep current).

## Future Phases

- **Phase 2:** File-based persistence (save/load contacts to/from TXT/JSON).
- **Phase 3:** Database integration (SQLite).
- **Phase 4:** GUI with Tkinter.

## Contributing

Feel free to fork and contribute! Suggestions for improvements are welcome.

## License

This project is open-source under the MIT License.