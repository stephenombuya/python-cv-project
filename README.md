# **Python CV Project**

## **Project Overview**
This Python project generates a CV/Resume document in Word format (.docx) based on user input. The project uses the **`python-docx`** library to create and format the document with structured sections such as Profile Picture, Personal Details, About Me, Work Experience, and Skills.

---

## **Features**
1. **Profile Picture Upload**
   - Allows the user to include a profile picture in their CV.
2. **Personal Details**
   - Collects the user's name, phone number, and email address.
3. **About Me Section**
   - Adds a summary about the user.
4. **Work Experience Section**
   - Dynamically collects and adds multiple work experiences with company names, dates, and descriptions.
5. **Skills Section**
   - Allows the user to input multiple skills displayed in bullet points.
6. **Structured and Clean Output**
   - Generates a professionally formatted CV document (cv.docx).

---

## **Prerequisites**
Ensure you have the following installed:
- Python 3.x
- `python-docx` library (install via pip)

```bash
pip install python-docx
```

---

## **Project Structure**
```plaintext
python-cv-project/
│
├── my_app.py           # Main Python script to generate the CV
├── requirements.txt    # Project dependencies
├── pexels-rachel-claire-5490276.jpg   # Sample profile picture
├── README.md           # Documentation file
├── LICENSE             # License for the project
└── cv.docx             # Output CV file (generated dynamically)
```

---

## **How to Run the Project**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/stephenombuya/python-cv-project.git
   cd python-cv-project
   ```

2. **Install Dependencies**
   Use the provided `requirements.txt` file to install necessary libraries.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**
   Execute the Python script to generate your CV.
   ```bash
   python my_app.py
   ```

4. **Input Details**
   Follow the prompts to input:
   - Profile picture path
   - Name, phone number, and email
   - About Me section
   - Work Experience(s)
   - Skills

   Once done, the script will generate a **cv.docx** file in the project directory.

---

## Example Input/Output
### Input Prompts Example
```plaintext
What is your name? John Doe
What is your phone number? +1234567890
What is your email? john.doe@example.com
Tell me about yourself? I am a software developer with 5+ years of experience.

Enter company: ABC Corp
From Date: 2020
To Date: 2023
Describe your experience at ABC Corp: Developed web applications and managed deployments.

Do you have more experiences? Yes or No: No
Enter your skill: Python
Do you have more skills? Yes or No: Yes
Enter your skill: JavaScript
Do you have more skills? Yes or No: No
```

### Output Document Structure
- **Profile Picture** (2x2 inches)
- **Personal Details**: John Doe | +1234567890 | john.doe@example.com
- **About Me**: "I am a software developer with 5+ years of experience."
- **Work Experience**:
  - **ABC Corp (2020-2023)**: "Developed web applications and managed deployments."
- **Skills**:
  - Python
  - JavaScript

---

## **Improvements**
This version of the project includes:
- **Input Validation**: Ensures proper input formats (e.g., email validation).
- **Error Handling**: Handles errors for missing files, invalid input, or unexpected interruptions.
- **Dynamic Sections**: Allows users to add multiple work experiences and skills seamlessly.
- **Code Refactoring**: Cleaner and more modular code for better maintainability.

---

## **Future Enhancements**
Here are some ideas for improving the project further:
1. **Automatic File Naming**: Save each generated CV with a unique filename.
2. **PDF Export**: Add functionality to export the CV as a PDF document.
3. **GUI Integration**: Create a graphical user interface using Tkinter or PyQt.
4. **Template Support**: Allow users to choose from multiple CV templates.
5. **Skill Categories**: Organize skills under categories like Technical Skills, Soft Skills, etc.

---

## License
This project is licensed under the [GPL-3.0 License](LICENSE).

---

## Author
**Stephen Ombuya**
- GitHub: [Stephen Ombuya](https://github.com/stephenombuya)
- LinkedIn: [Stephen Ombuua](https://www.linkedin.com/in/stephen-ombuya-backend-web-engineer/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3B3jUSREkYTT%2B9BM%2BVEoO9kA%3D%3D)

---

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

Feel free to open an issue for feature requests or bug reports.

---

## Acknowledgments
- Profile picture from [Pexels](https://www.pexels.com)
- `python-docx` library for document generation.

---

Thank you for using the Python CV Project! 🚀
