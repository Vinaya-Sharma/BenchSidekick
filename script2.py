import os
import gdown
from PyPDF2 import PdfReader

# Google Drive folder URL
url = "https://drive.google.com/drive/folders/1nCTr3u63XRZ_sxF-Zdy4qD87LMgbsnZk?usp=sharing"

# Choose the subdirectory name within the root directory
subdirectory_name = "Google_Drive_Downloads"

# Create the subdirectory if it doesn't exist
target_directory = os.path.join(os.getcwd(), subdirectory_name)
if not os.path.exists(target_directory):
    os.mkdir(target_directory)

os.chdir(target_directory)
print(os.getcwd())

# Download the Google Drive folder
gdown.download_folder(url, quiet=True, use_cookies=False)

# Function to extract text from PDF files
def get_pdf_text(pdf_path):
    raw_text = ""
    pdf_reader = PdfReader(pdf_path)
    for page in pdf_reader.pages:
        raw_text += page.extract_text()
    return raw_text

# Loop through each folder and each file within the directory
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".pdf"):  # Ensure the file is a PDF
            pdf_path = os.path.join(root, file)
            pdf_text = get_pdf_text(pdf_path)
            print(f"Text extracted from {pdf_path}:")
            print(pdf_text)
