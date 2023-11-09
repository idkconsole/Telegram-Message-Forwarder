# Telegram Message Forwarder

## Overview
The Telegram Message Forwarder is a Python script that automatically forwards messages from a specified message ID to a list of designated group or shop IDs on Telegram. This tool utilizes the Telegram API to streamline message distribution for shop announcements, updates, or any other relevant content.

## Prerequisites
- A Telegram account
- Python 3.x installed on your system

## Warning
Be aware that automated message forwarding is subject to Telegram's terms of service. Misuse of this tool may lead to account limitations. Use it responsibly and ensure you have the recipients' consent to receive messages.

## Getting Started

1. **Create Your Telegram API Credentials:**
   - Navigate to [Telegram API Development Tools](https://my.telegram.org).
   - Log in with your Telegram account credentials.
   - Click on "API development tools" and complete the form to obtain your `api_id` and `api_hash`.

2. **Configure the Script:**
   - Clone/download the repository to your local machine.
   - Open `main.py` in a text editor or IDE.
   - Replace the placeholders in line 6 and 7 with your `api_id` and `api_hash` received from step 1.

3. **Set Your Parameters:**
   - Enter the link to your shop and the message ID you wish to forward on lines 14 and 15, respectively.
   - On line 19, add the group/shop IDs where the message should be forwarded.

4. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the script by typing `python main.py` and pressing Enter.

## Support
If you encounter any issues or have questions, please open an issue on the project's GitHub page.
