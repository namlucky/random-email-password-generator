import os
import random
import openpyxl
import pandas as pd
import streamlit as st

# Function to load words from a .txt file
def load_words_from_txt(uploaded_file):
    try:
        # Decode bytes to string and split into lines
        words = uploaded_file.getvalue().decode("utf-8").splitlines()
        return [word.strip() for word in words if word.strip()]
    except Exception as e:
        st.error(f"Error loading words: {e}")
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

# Function to export emails and passwords as an Excel file
def export_to_excel(emails, passwords):
    # Create a Pandas DataFrame
    data = {"Email": emails, "Password": passwords}
    df = pd.DataFrame(data)
    
    # Save the data to an Excel file
    excel_file = "generated_emails_passwords.xlsx"
    df.to_excel(excel_file, index=False)
    return excel_file

# Streamlit Web App
def main():
    st.title("Random Email and Password Generator by Namlucky")
    st.write("Checkout my github link for detail and local version!: https://github.com/namlucky/random-email-password-generator")
    st.write("This app generates random emails and passwords based on your input. Upload a `words.txt` file to get started.")

    # Upload words.txt
    uploaded_file = st.file_uploader("Upload your `words.txt` file", type=["txt"])
    if uploaded_file:
        # Load the words from the uploaded file
        words = load_words_from_txt(uploaded_file)
        if not words:
            st.warning("The file is empty or invalid. Please upload a valid `words.txt` file.")
            return
    else:
        st.info("Please upload a `words.txt` file to continue.")
        return

    # Email prefix input
    email_prefix = st.text_input("Enter your custom email prefix (e.g., my_custom):", "my_custom")

    # Number of emails and passwords to generate
    num_entries = st.number_input("Enter the number of emails and passwords to generate:", min_value=1, max_value=1000, value=10)

    # Generate button
    if st.button("Generate Emails and Passwords"):
        # Generate emails and passwords
        random_emails = generate_random_email(email_prefix, num_entries, words)
        random_passwords = generate_random_password(num_entries, words)
        
        # Display the results in the Streamlit app
        st.write("### Generated Results")
        data = {"Email": random_emails, "Password": random_passwords}
        df = pd.DataFrame(data)
        st.dataframe(df)
        
        # Export the results to an Excel file for download
        excel_file = export_to_excel(random_emails, random_passwords)
        with open(excel_file, "rb") as file:
            st.download_button(
                label="Download as Excel",
                data=file,
                file_name="emails_passwords.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

if __name__ == "__main__":
    main()
