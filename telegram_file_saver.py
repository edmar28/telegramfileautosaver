from telethon import TelegramClient, events
import os

# Replace these with your own values from my.telegram.org
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'  # Format: +123456789

# Create a Telegram Client
client = TelegramClient('session_name', api_id, api_hash)

# Define the directory to save files
download_folder = 'C:/path/to/save/folder'  # Change this to your preferred folder

# Ensure the folder exists
os.makedirs(download_folder, exist_ok=True)

# Function to display the banner
def display_banner():
    banner = """
    ===========================================
       Telegram File Auto-Saver
       Developed by MrPepe
    ===========================================
    """
    print(banner)

# Display the banner
display_banner()

@client.on(events.NewMessage(chats='me'))  # 'me' refers to your "Saved Messages"
async def handler(event):
    if event.message.file:  # Check if the message has a file
        print(f"New file received: {event.message.file.name}")
        # Download the file
        file_path = await event.message.download_media(file=download_folder)
        print(f"File saved to: {file_path}")

async def main():
    # Start the client and log in
    await client.start(phone=phone_number)
    print("Listening for new messages in Saved Messages...")

    # Run indefinitely
    await client.run_until_disconnected()

# Run the client
with client:
    client.loop.run_until_complete(main())
