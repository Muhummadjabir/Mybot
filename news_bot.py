from telegram import Bot
import time

# Your Bot Token
BOT_TOKEN = "8200878464:AAE6H-bM6uhNGE5TndW_xPVIHabcthPJAHQ"

# Create the bot
bot = Bot(token=BOT_TOKEN)

print("Bot is running...")

# Keep track of last message
last_update_id = None

while True:
    # Get new updates
    updates = bot.get_updates(offset=last_update_id, timeout=10)

    for update in updates:
        message = update.message
        if message:
            chat_id = message.chat.id
            text = message.text

            # Reply with the same message
            bot.send_message(chat_id=chat_id, text=f"You said: {text}")
            print(f"Replied to: {text}")

            # Update offset
            last_update_id = update.update_id + 1

    time.sleep(1)
