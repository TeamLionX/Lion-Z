from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("LionZ Spam Bot Telethon String Generator")
print("")
API_KEY = "2096818"
API_HASH = "c6046095d89d12672af2755f157ee05e"

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("")
            session = client.session.save()
            client.send_message("me", f"`{session}`")
            print(
                "Your Telethon String session has been successfully stored in your telegram, Please check your Telegram Saved Messages"
            )
            print("")
    except:
        print("")
        print("Wrong phone number \n make sure its with correct  country code")
        print("")
        continue
    break
