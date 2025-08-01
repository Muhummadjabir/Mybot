import os
import requests
import schedule
import time
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def get_news():
    # Example placeholder for news API
    news = "📰 Daily Update: The world is still spinning."
    return news

def send_news():
    news = get_news()
    bot.send_message(chat_id=CHAT_ID, text=news)

schedule.every().day.at("08:00").do(send_news)

print("Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
