import os
import json
import re
import phonenumbers
from validate_email import validate_email
from docx import Document
from docx.shared import Inches

# ------------------ Utility Functions ------------------

def validate_email_address(email):
    """Validate email using the validate_email library."""
    return validate_email(email)

def validate_phone_number(phone):
    """Validate phone number using the phonenumbers library."""
    try:
        phone_number = phonenumbers.parse(phone, "KE")  # KE for Kenya or replace with your country
        return phonenumbers.is_valid_number(phone_number)
    except phonenumbers.NumberParseException:
        return False

def get_input_with_validation(prompt, validation_fn, error_message):
    """Reusable input function with validation."""
    while True:
        value = input(prompt).strip()
        if validation_fn(value):
            return value
        print(error_message)

def load_data_from_json():
    """Load data from a JSON file."""
    file_name = input("Enter the JSON file path (or press Enter to skip): ").strip()
    if file_name and os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                print("Data loaded successfully!")
                return data
        except json.JSONDecodeError:
            print("Invalid JSON format. Please try again.")
    return None

# ------------------ CV Sections ------------------

def add_profile_picture(document, image_path):
    """Add a profile picture to the document."""
    if os.path.exists(image_path):
        document.add_picture(image_path, width=Inches(2.0))
    else:
        print(f"Warning: Profile picture '{image_path}' not found. Skipping.")

def get_contact_details(data=None):
    """Get validated contact details."""
    print("\n--- Contact Information ---")
    if data:
        name = data.get("name", "")
        phone_number = data.get("phone_number", "")
        email = data.get("email", "")
    else:
        name = input("What is your name? ").strip()
        phone_number = get_input_with_validation(
            "Enter your phone number: ", validate_phone_number, "Invalid phone number format. Try again."
        )
        email = get_input_with_validation(
            "Enter your email: ", validate_email_address, "Invalid email format. Try again."
        )
    return name, phone_number, email

def add_about_me(document, data=None):
    """Add the 'About Me' section."""
    print("\n--- About Me Section ---")
    document.add_heading("About Me", level=1)
    about_me = data.get("about_me", "") if data else input("Tell me about yourself: ").strip()
    if about_me:
        document.add_paragraph(about_me)

def add_work_experience(document, data=None):
    """Add work experiences."""
    print("\n--- Work Experience ---")
    experiences = data.get("work_experience", []) if data else []
    while True:
        if not data:
            company = input("Enter company name (or 'done' to skip): ").strip()
            if company.lower() == "done":
                break
            from_date = input("From Date: ").strip()
            to_date = input("To Date: ").strip()
            description = input(f"Describe your experience at {company}: ").strip()
            experiences.append({"company": company, "from_date": from_date, "to_date": to_date, "description": description})
        else:
            break  # JSON data already has work experience

    for exp in experiences:
        p = document.add_paragraph()
        p.add_run(exp['company'] + " ").bold = True
        p.add_run(f"{exp['from_date']} - {exp['to_date']}\n").italic = True
        p.add_run(exp['description'])

def add_skills(document, data=None):
    """Add skills."""
    print("\n--- Skills Section ---")
    document.add_heading("Skills", level=1)
    skills = data.get("skills", []) if data else []
    while not data:
        skill = input("Enter a skill (or 'done' to finish): ").strip()
        if skill.lower() == "done":
            break
        skills.append(skill)

    for skill in skills:
        document.add_paragraph(skill, style="List Bullet")

def save_document(document):
    """Save the document with a custom name."""
    filename = input("\nEnter the output file name (e.g., my_cv.docx): ").strip()
    if not filename.endswith(".docx"):
        filename += ".docx"
    document.save(filename)
    print(f"CV successfully saved as '{filename}'!")

# ------------------ Main Function ------------------

def main():
    print("Welcome to the Enhanced CV Generator!")
    document = Document()

    # Option to load data from JSON
    data = load_data_from_json()

    # Add profile picture
    image_path = "pexels-rachel-claire-5490276.jpg"
    add_profile_picture(document, image_path)

    # Add Contact Details
    name, phone_number, email = get_contact_details(data)
    document.add_paragraph(f"{name} | {phone_number} | {email}")

    # Add About Me
    add_about_me(document, data)

    # Add Work Experience
    add_work_experience(document, data)

    # Add Skills
    add_skills(document, data)

    # Save the document
    save_document(document)

if __name__ == "__main__":
    main()
