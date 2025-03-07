import requests
import json

# Replace with your Discord webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1347623708662956034/J1_Dz9Q457JVvRc5oHcIriyJak1F80h6o4PYplePotZLG3ygWjCCa61JLXhmsyLb25pi"

# Replace with your Google Apps Script Web App URL
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxyjpn99F8ff0wr1OxaW04-DGyqTAsT00SDByLpzhir0kiipznl_zNaSCPmP-c0Farttw/exec"

def send_log(username, daily_amount, event_supervisions, author):
    # Format data for Google Apps Script
    payload = {
        "username": username,
        "daily_amount": daily_amount,
        "event_supervisions": event_supervisions,
        "author": author
    }

    # Send data to Google Apps Script
    response = requests.post(GOOGLE_SCRIPT_URL, json=payload)
    
    if response.status_code == 200:
        print("Log sent successfully to Google Sheets!")
    else:
        print(f"Failed to send log: {response.status_code}, {response.text}")

def listen_to_discord():
    # Simulate a received Discord message (Modify this for real Discord bot integration)
    discord_message = {
        "username": "Jackweilison",
        "daily_amount": 10,
        "event_supervisions": {"William7424": 5, "Jackson8742": 5},
        "author": "Jackweilison"
    }

    # Extract data and send to Google Sheets
    send_log(
        username=discord_message["username"],
        daily_amount=discord_message["daily_amount"],
        event_supervisions=discord_message["event_supervisions"],
        author=discord_message["author"]
    )

if __name__ == "__main__":
    listen_to_discord()
