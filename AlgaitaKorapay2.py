import telebot
import os

# 👉 Dauko token daga Render ENV
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot yana aiki lafiya!")

# =========================
# TEST MESSAGE
# =========================
@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Na karɓa 👍")

# =========================
# RUN BOT
# =========================
print("Bot started...")
bot.infinity_polling()