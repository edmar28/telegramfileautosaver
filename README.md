
# Telegram File Auto-Saver 📥

A Python script that automatically downloads files sent to your Telegram "Saved Messages" or a bot directly to your PC. This is useful for scenarios where you need an automated way to transfer files from your phone to your computer using Telegram.


## Features
- Automatically downloads files sent to your Telegram "Saved Messages".
- Saves files to a specified directory on your PC.
- Uses the Telethon library for interacting with Telegram.
- Simple and easy-to-configure script.

## Table of Contents

- Prerequisites
- Installation
- Configuration
- Usage
- How It Works
- Troubleshooting
- Contributing
- License

## Prerequisites

Before using this script, make sure you have the following:
1. Python 3.7 or higher installed on your system.
2. A Telegram account.
3. API ID and API Hash from Telegram:
- Go to my.telegram.org and log in.
- Create a new application to get your API ID and API Hash.


## Installation
1. Clone the repository:

``` bash
git clone https://github.com/edmar28/telegram-file-auto-saver.git
cd telegram-file-auto-saver
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required Python packages:
```bash
pip install -r requirements.txt
```
Ensure Telethon is installed:
```bash
pip install telethon
```


## Configuration

Before running the script, you'll need to configure your Telegram API credentials.

1. Open the script telegram_file_saver.py and update the following variables:
```bash
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'  # e.g., +123456789
```

2. Update the download directory as per your preference:
```bash
download_folder = 'C:/path/to/save/folder'
```

## Usage
1. Run the script:
```bash
python telegram_file_saver.py
```

2. How to send files:
- Open Telegram on your phone.
- Send a file to your Saved Messages or the bot (depending on your script configuration).
- The file will be automatically saved to the specified folder on your PC.

### Example Output
```bash
Listening for new messages in Saved Messages...
New file received: sample_document.pdf
File saved to: C:/path/to/save/folder/sample_document.pdf
```

### How It Works
- The script uses the Telethon library to connect to your Telegram account.
- It listens for new messages in your "Saved Messages" chat.
- When a new file is detected, it downloads it automatically to the specified directory.

### Flowchart
```bash
Phone -> Telegram ("Saved Messages") -> Python Script (Telethon) -> Auto-Save to PC
```



## Troubleshooting
If you encounter issues, here are some common solutions:
1. Session Expired or Phone Verification:
- If the script asks for verification code repeatedly, delete the session_name.session file and re-run the script.

2. File Not Downloading:
- Ensure your API credentials (api_id and api_hash) are correct.
- Make sure your phone number is in the correct format, e.g., +123456789.

3. Telethon Import Error:
- Make sure Telethon is installed: pip install telethon.
