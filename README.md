# New-User-Input-Into-Dictionary

A simple Python program that simulates a programmer registration system with two user roles: Admin and Client. Users can enter their usernames, favorite programming languages, and years of programming experience. The program stores the information in a list of dictionaries and uses the `json` module to display the updated records in a readable format.

## Features

- **Two User Roles:** Supports Admin and Client access.
- **Admin Login:** Requires a password to access the admin section.
- **Password Verification:** Provides up to two additional password attempts after the initial login attempt.
- **Programmer Registration:** Allows users to enter their username, favorite programming languages, and years of experience.
- **Multiple Language Input:** Accepts multiple programming languages separated by commas.
- **Dynamic Data Storage:** Adds new programmer profiles to an existing list of dictionaries.
- **JSON Formatting:** Uses `json.dumps()` with indentation to display updated records in a structured format.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the code in a file named `programmer_registration.py`.
3. Open a terminal or command prompt.
4. Run the program:

   ```bash
   python programmer_registration.py
   ```

5. Select your role:
   - Enter `A` for Admin.
   - Enter `C` for Client.
6. Follow the instructions to register programmer information.

## Example

**Example input:**

```text
What's your current position? [A : Admin, C : Client]: C

Please fill your identity below
Username: Alex
Favorite_Language(s): Python,Java,C++
Years (only enter number): 3
Do you want to continue a new user? [Yes/No]: No
```

**Example output:**

```json
[
    {
        "user_name": "Elshad",
        "favorite_languages": [
            "Python",
            "Java",
            "C#"
        ],
        "experience": 10
    },
    {
        "user_name": "Renad",
        "favorite_languages": [
            "Scratch",
            "Python"
        ],
        "experience": 2
    },
    {
        "user_name": "Alex",
        "favorite_languanges": [
            "Python",
            "java",
            "c++"
        ],
        "experience": 3
    }
]
```

## Concepts Practiced

- **Functions:** Creating a reusable `add_user()` function to register new programmers.
- **Lists and Dictionaries:** Managing multiple programmer profiles and their information.
- **JSON:** Using `json.dumps()` to format and display structured data.
- **Loops:** Using `while` loops to handle repeated registration and password attempts.
- **Conditional Statements:** Implementing role selection and password verification.
- **String Methods:** Applying `.upper()`, `.strip()`, `.capitalize()`, and `.split()` to process user input.
- **User Input:** Collecting and processing information through `input()`.

## Language

Python 3
