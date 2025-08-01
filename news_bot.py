from telegram import Bot
import time
import imghdr
import os

BOT_TOKEN = "8200878464:AAE6H-bM6uhNGE5TndW_xPVIHabcthPJAHQ"
bot = Bot(token=BOT_TOKEN)

print("Waiting for message...")

last_update_id = None

while True:
    updates = bot.get_updates(offset=last_update_id, timeout=10)
    for update in updates:
        if update.message:
            chat_id = update.message.chat.id

            # Handle text messages
            if update.message.text:
                text = update.message.text
                bot.send_message(chat_id=chat_id, text=f"You said: {text}")
                print(f"Responded to text from chat ID {chat_id}")

            # Handle image messages
            if update.message.photo:
                photo = update.message.photo[-1]  # Get highest resolution photo
                file = bot.get_file(photo.file_id)

                # Download image
                file_path = f"temp_{photo.file_id}.jpg"
                file.download(file_path)

                # Detect image type
                img_type = imghdr.what(file_path)
                bot.send_message(chat_id=chat_id, text=f"Received an image. Type: {img_type}")

                print(f"Received image of type: {img_type} from chat ID {chat_id}")

                # Clean up
                os.remove(file_path)

            # Update offset to avoid processing same message
            last_update_id = update.update_id + 1

    time.sleep(2)
