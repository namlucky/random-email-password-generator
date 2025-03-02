# Random Email and Password Generator

A Python-based **Streamlit** web application that generates random emails and passwords based on a user-defined word list. The app allows customization of email prefixes and passwords and supports data export as an Excel file.

---

## Features
- **Custom Words**: Use your own `words.txt` file to define the word list.
- **Email Generation**: Generate random emails with a customizable prefix.
- **Password Generation**: Create secure passwords with meaningful words, numbers, and special characters.
- **Excel Export**: Download the generated data as an Excel spreadsheet.

---

## Installation and Setup

### Prerequisites
- **Python 3.8 or higher**
- Libraries listed in `requirements.txt`

### Steps
1. **Clone the Repository**:
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>

2. **Install Dependencies**:
Install required libraries using pip:
pip install -r requirements.txt

3. **Run the Application**:
Start the Streamlit app locally:
streamlit run app.py
Open the link in your browser (e.g., `http://localhost:8501`).

---

## Usage

1. **Upload a `words.txt` File**:
- Create a text file with one word per line (e.g., `Sunny`, `Golden`).
- Upload it using the app interface.

2. **Customize Inputs**:
- Enter your desired email prefix (e.g., `my_custom`).
- Specify how many emails and passwords to generate.

3. **Generate Results**:
- Click the "Generate Emails and Passwords" button.

4. **Export and Download**:
- Download the results as an Excel file.

---

## Example Output

### Sample Table in the App:
| **Email**                      | **Password**       |
|--------------------------------|--------------------|
| my_custom+Golden123@gmail.com  | Brightmagic45@     |
| my_custom+Sunny789@gmail.com   | Silverhidden67!    |

---

## File Structure
project-folder/
├── app.py # Main Streamlit application
├── requirements.txt # List of Python dependencies
├── words.txt # Example word list file
├── LICENSE # License for the project
├── README.md # Documentation and instructions
└── config.json # Configuration file (optional)

---

## License
This project is licensed under the PCT-HIGHSCHOOL License. See the https://www.pct.edu.vn/ for details.

