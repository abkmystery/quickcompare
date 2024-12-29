QuickCompare

QuickCompare is a web application that allows users to compare text from multiple sources, including:

Manually entered text
Uploaded text files (.txt)
Uploaded document files (.pdf, .docx)
Uploaded image files (.jpg, .jpeg, .png) using OCR technology
It utilizes Azure OpenAI Service for intelligent and contextual text comparison.

Features

Supports manual text input and file uploads (.txt, .pdf, .docx, .jpg, .jpeg, .png)
Extracts text from PDFs, Word documents, and images (via OCR)
Performs semantic comparison to highlight key thematic differences
Provides results through an easy-to-use web interface
Tech Stack

Frontend: HTML5, CSS3, JavaScript
Backend: Python (Flask)
AI Service: Azure OpenAI
File Handling: PyPDF2, python-docx, pytesseract

Setup Instructionsgi

Clone the Repository
git clone https://github.com/abkmystey/quickcompare.git
cd quickcompare

Set Up Virtual Environment
python -m venv venv
source venv/bin/activate (macOS/Linux)
venv\Scripts\activate (Windows)

Install Dependencies
pip install -r requirements.txt

Set Environment Variables
Create a .env file in the project root and add the following:
AZURE_OPENAI_KEY=your_openai_key
AZURE_OPENAI_ENDPOINT=https://your_openai_endpoint
AZURE_OPENAI_API_VERSION=2024-02-15-preview

Run the Application
python app.py

The application will be available at:
http://127.0.0.1:5000/

Testing

Input text or upload supported files in the provided fields.
Click Compare to view results.
Verify responses and logs in the Flask terminal.
Deployment on GitHub Pages or Azure App Service

Follow deployment guidelines from Azure App Service documentation or any preferred deployment platform.
File Structure

quickcompare/
├── app.py (Backend API and Flask app)
├── templates/
│ ├── index.html (Frontend UI)
├── static/
│ ├── style.css (Styling if applicable)
├── .env (Environment variables)
├── README.md (Project documentation)
├── requirements.txt (Required Python libraries)
└── venv/ (Virtual environment)

Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Submit a Pull Request.

License

This project is licensed under the MIT License.

Contact

For questions or suggestions, reach out to:

Email: ahmed.khalid2108@gmail.com
GitHub: https://github.com/abkmystery