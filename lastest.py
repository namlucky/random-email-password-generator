import os
import random
import openpyxl

print("Current working directory:", os.getcwd()) # Print the current working directory
# Function to load words from a .txt file
def load_words_from_txt(filename):
    try:
        with open(filename, "r") as file:
            # Read all lines, strip whitespace, and create a list
            words = [line.strip() for line in file.readlines()]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to generate random emails
def generate_random_email(prefix, n, words):
    emails = []
    for _ in range(n):
        word = random.choice(words)
        number = random.randint(10, 999)  # Random number for uniqueness
        email = f"{prefix}+{word}{number}@gmail.com"
        emails.append(email)
    return emails

# Function to generate random passwords
def generate_random_password(n, words):
    passwords = []
    special_chars = "!@#$%^&*"
    
    for _ in range(n):
        word1 = random.choice(words)
        word2 = random.choice(words).lower()
        number = random.randint(10, 99)
        special = random.choice(special_chars)
        password = f"{word1}{word2}{number}{special}"
        passwords.append(password)
    return passwords

# Function to ensure the output directory exists
def get_safe_filename(filename):
    # Specify the directory where the Excel file will be saved
    output_folder = "C:\\Users\\nambl\\Desktop"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Creates the folder if it doesn't exist
    
    # Combine the folder path and filename
    return os.path.join(output_folder, filename)

# Function to export emails and passwords to Excel file
def export_to_excel(emails, passwords, filename="output.xlsx"):
    # Use the safe filename utility
    safe_filename = get_safe_filename(filename)
    
    # Create a new Excel workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Emails and Passwords"
    
    # Add headers to the sheet
    sheet["A1"] = "Email"
    sheet["B1"] = "Password"
    
    # Write the data (emails and passwords) to the spreadsheet
    for i, (email, password) in enumerate(zip(emails, passwords), start=2):
        sheet[f"A{i}"] = email
        sheet[f"B{i}"] = password

    # Save the workbook
    workbook.save(safe_filename)
    print(f"\nData successfully exported to {safe_filename}")

# Main program
def main():
    print("Loading words from 'words.txt'...")
    # Load words from the external words.txt file
    words = load_words_from_txt("words.txt")
    
    if not words:
        print("No words were loaded. Please ensure 'words.txt' exists and contains valid data.")
        return
    
    while True:
        # Display the menu
        print("\nSelect a feature:")
        print("1. Generate random emails and passwords")
        print("0. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1/0): ")
        
        if choice == "1":
            # Generate emails and passwords
            prefix = input("Enter your custom email prefix (e.g., my_custom): ")
            n = int(input("Enter the number of random emails and passwords to generate: "))
            
            # Generate random emails
            random_emails = generate_random_email(prefix, n, words)
            
            # Generate random passwords
            random_passwords = generate_random_password(n, words)
            
            # Display the emails and passwords
            print("\nGenerated Emails and Passwords:")
            for email, password in zip(random_emails, random_passwords):
                print(f"Email: {email} | Password: {password}")
            
            # Export to Excel
            filename = input("\nEnter the Excel filename to save (e.g., output.xlsx): ")
            export_to_excel(random_emails, random_passwords, filename)
        
        elif choice == "0":
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select 1 or 0.")

# Run the main program
if __name__ == "__main__":
    main()
