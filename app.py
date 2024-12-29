
from flask import Flask, request, jsonify, render_template
import os
from openai import AzureOpenAI
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
import pytesseract
from PIL import Image

app = Flask(__name__)

# Azure OpenAI Configuration
client = AzureOpenAI(
    api_key=os.getenv('AZURE_OPENAI_KEY'),
    api_version='2024-06-01',
    azure_endpoint='https://resourc_name.openai.azure.com/' #Put your endpoint
)

# Path to Tesseract OCR executable (update if required)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\x\y'  # Update this path for your system


def read_file_content(file):
    """
    Read content from supported file types (.txt, .pdf, .docx, .jpg, .png).
    """
    try:
        if file.filename.endswith('.txt'):
            return file.read().decode('utf-8')

        elif file.filename.endswith('.pdf'):
            with open(file.filename, 'wb') as temp_file:
                temp_file.write(file.read())
            return extract_pdf_text(file.filename)

        elif file.filename.endswith('.docx'):
            with open(file.filename, 'wb') as temp_file:
                temp_file.write(file.read())
            doc = Document(file.filename)
            return '\n'.join([para.text for para in doc.paragraphs])

        elif file.filename.endswith(('.jpg', '.jpeg', '.png')):
            image = Image.open(file.stream)
            return pytesseract.image_to_string(image)

        else:
            return f"Unsupported file format: {file.filename}. Only .txt, .pdf, .docx, .jpg, and .png files are supported."

    except Exception as e:
        return f"Error reading file {file.filename}: {str(e)}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare_inputs():
    # Retrieve text inputs
    text1 = request.form.get('text1', '')
    text2 = request.form.get('text2', '')

    # Retrieve file uploads
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    # Read and append file contents if available
    if file1 and file1.filename:
        text1 += f"\n\n[File Content: {file1.filename}]\n{read_file_content(file1)}"
    if file2 and file2.filename:
        text2 += f"\n\n[File Content: {file2.filename}]\n{read_file_content(file2)}"

    if not text1.strip() or not text2.strip():
        return jsonify({"error": "Both inputs (text or file content) must have valid content to compare."}), 400

    try:
        # Send combined inputs to Azure OpenAI for comparison
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Replace with whatever model you use(deployment name)
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert legal assistant. Compare the following two pieces of text/documents and highlight the key meaning-related differences. Avoid pointing out trivial differences like spaces, punctuation, or formatting."
                },
                {
                    "role": "user",
                    "content": f"Compare these two texts:\n\nText 1:\n{text1}\n\nText 2:\n{text2}"
                }
            ]
        )

        result = response.choices[0].message.content
        return jsonify({"message": result})

    except Exception as e:
        print("Azure OpenAI Error:", e)
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
