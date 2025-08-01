import requests
import schedule
import time
from telegram import Bot

# Your test bot token and chat ID
BOT_TOKEN = "8200878464:AAE6H-bM6uhNGE5TndW_xPVIHabcthPJAHQ"
CHAT_ID = "YOUR_CHAT_ID_HERE"  # Replace this with your actual chat ID

bot = Bot(token=BOT_TOKEN)

def get_news():
    return "📰 Daily Update: The world is still spinning."

def send_news():
    news = get_news()
    bot.send_message(chat_id=CHAT_ID, text=news)

# Schedule to run every day at 8 AM
schedule.every().day.at("08:00").do(send_news)

print("Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
