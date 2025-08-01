from telegram import Bot
import time

BOT_TOKEN = "8200878464:AAE6H-bM6uhNGE5TndW_xPVIHabcthPJAHQ"
bot = Bot(token=BOT_TOKEN)

print("Waiting for message...")

last_update_id = None

while True:
    updates = bot.get_updates(offset=last_update_id, timeout=10)
    for update in updates:
        if update.message:
            chat_id = update.message.chat.id
            text = update.message.text

            # Send response back to the user
            bot.send_message(chat_id=chat_id, text=f"You said: {text}")
            print(f"Responded to chat ID {chat_id}")

            # Move to next update
            last_update_id = update.update_id + 1

    time.sleep(2)
