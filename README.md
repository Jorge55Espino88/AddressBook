# Address Book - Phase 1: Object-Oriented Implementation

A simple command-line address book application built with Python, focusing on object-oriented programming (OOP) principles. This phase implements a contact management system using classes for encapsulation, validation, and modularity.

## Description

This is the first phase of a multi-phase address book project. In this phase, we implement a basic contact management system using OOP in Python. Users can add, view, update, and delete contacts through a console-based menu. Each contact includes an ID (generated with date and sequence), name, last name, telephone, cell phone, and email.

Key features include:
- **Unique ID generation:** Using current date and incremental counter (e.g., "20231015-1").
- **Input validation:** Required fields and data types (e.g., numeric phones, valid emails) enforced via properties and setters.
- **OOP design:** Classes `Contact` (for individual contacts) and `AddressBook` (for managing the collection), with encapsulation and error handling.
- **Menu-driven interface:** Easy navigation with error handling for invalid inputs.

**Technologies Used:**
- Python 3.x
- Standard libraries: `datetime` for ID generation.

**Programming Paradigm:** Object-Oriented Programming (OOP) with classes, properties, and inheritance-ready structure.

## Installation

1. Clone the repository:
git clone https://github.com/Jorge55Espino88/AddressBook.git cd AddressBook


Copy code

2. Ensure Python 3.x is installed.

3. Run the application:
python main.py


Copy code

## Usage

1. Start the program and enter your name.
2. Choose an option from the menu:
- 1: View all contacts.
- 2: View a specific contact by ID.
- 3: Add a new contact (with validations).
- 4: Update an existing contact (selective updates).
- 5: Delete a contact.
- 6: Exit.
3. Follow the prompts to interact with the address book.

Example:
- Add a contact: Enter name, last name, phone numbers, and email.
- Update: Enter the ID, and modify fields (leave blank to keep current).

## Project Structure

- `contact.py`: Defines the `Contact` class with properties, setters, and validation.
- `addressbook.py`: Defines the `AddressBook` class for managing contacts (add, view, edit, delete).
- `main.py`: Main script with the interactive menu.
- `README.md`: This file.

## Future Phases

- **Phase 2:** File-based persistence (save/load contacts to/from JSON files).
- **Phase 3:** Database integration (SQLite).
- **Phase 4:** GUI with Tkinter.

## Contributing

Feel free to fork and contribute! Suggestions for improvements are welcome. Open an issue for bugs or features.

## License

This project is open-source under the MIT L