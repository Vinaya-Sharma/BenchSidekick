import os
import gdown

# Google Drive folder URL
url = "https://drive.google.com/drive/folders/1P-xVlgYdZNdGW61cvFhI79ptTK5LS_Cj?usp=sharing"

# Choose the subdirectory name within the root directory
subdirectory_name = "Google_Drive_Downloads"

# Create the subdirectory if it doesn't exist
target_directory = os.path.join(os.getcwd(), subdirectory_name)
if not os.path.exists(target_directory):
    os.mkdir(target_directory)
    
os.chdir(target_directory)
print(os.getcwd() + "kr2nrj")

# Download the Google Drive folder
gdown.download_folder(url, quiet=True, use_cookies=False)

