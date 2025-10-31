import os
import json
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8417989121:AAG4eHplnHWyPXc3vjpv2QdsYjeJ_fRCGkE")
ADSTERA_LINK = os.getenv("https://url-shortener.me/8C7Y£")
CHANNEL_ID = "@VIRRSOS"
DATA_FILE = "data.json"

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ VirsosBot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id not in data:
        data[user_id] = {"clicked": False}
        save_data(data)
    keyboard = [[InlineKeyboardButton("🔗 Klik untuk lanjut", url=https://url-shortener.me/8C7Y)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Halo! Klik link di bawah ini dulu sebelum promote:",
                                    reply_markup=reply_markup)

async def promote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if not data.get(user_id, {}).get("clicked"):
        await update.message.reply_text("⚠️ Kamu belum klik link Adstera! Silakan /start dulu.")
        return
    msg = update.message.text.replace("/promote", "").strip()
    if not msg:
        await update.message.reply_text("Tulis pesan promote setelah /promote ya!")
        return
    promote_text = f"{msg}\n\n💸 Link sponsor: {https://url-shortener.me/8C7Y}"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=promote_text)
    await update.message.reply_text("✅ Promote kamu sudah dikirim ke channel!")

def main():
    app_bot = ApplicationBuilder().token(8417989121:AAG4eHplnHWyPXc3vjpv2QdsYjeJ_fRCGkE).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CommandHandler("promote", promote))
    keep_alive()
    app_bot.run_polling()

if __name__ == "__main__":
    main()
