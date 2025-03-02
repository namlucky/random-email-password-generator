# Random Email and Password Generator (Local Version)

This Python-based program generates random emails and passwords using a customizable word list (`words.txt`). The program is designed to run locally on your computer. It provides functionality to:
1. Generate emails with a custom prefix and meaningful random words.
2. Generate secure passwords with numbers, special characters, and meaningful words.
3. Export the results to an Excel file.

---

## Features
- **Word List Customization**:
  Supply a `words.txt` file containing meaningful words (one word per line) to personalize email and password generation.
- **Random Email Generator**:
  Automatically generates random email addresses, such as:
my_custom+Golden123@gmail.com
my_custom+Sunny789@gmail.com
- **Password Generator**:
Creates secure passwords using:
- A capitalized word.
- A lowercase word.
- A random number.
- A special character.
Example:
Brightmagic47!
Silverforest28@
- **Excel Export**:
Save the generated emails and passwords as an Excel file on your desktop.

---

## Prerequisites
To run this program locally, you need:
1. **Python 3.8 or higher** installed on your computer.
2. The following Python libraries:
openpyxl

---

## Installation and Setup

### Step 1: Set Up the Environment
1. Clone this repository or download the script files into a folder on your computer.


2. Open a terminal (Command Prompt, PowerShell, or any terminal emulator).

3. Navigate to the project folder:

### Step 2: Install the Required Library
Use `pip` to install the necessary library (`openpyxl`):

### Step 3: Create the `words.txt` File
1. Open a text editor (e.g., Notepad, VS Code).
2. Create a file named `words.txt` in the EXACTLY project folder that same directory.
3. Add meaningful words, one word per line. For example:
Sunny
Golden
Silver
Magic
Bright
Bright
4. Save the file.

---

## Usage Instructions

1. **Run the Program**
- Open a terminal or Command Prompt.
- Navigate to the project folder where `app.py` is located:
  ```
  cd path\to\project-folder
  ```
- Run the program:
  ```
  python app.py
  ```

2. **Follow the Prompts**
- The program will prompt you for input:
  1. **Custom Email Prefix**:
     Enter a prefix for your emails (e.g., `my_custom`).
  2. **Number of Entries**:
     Specify how many emails and passwords to generate.
  3. **Export Filename**:
     Enter the filename to save the results as an Excel file (e.g., `output.xlsx`).


