from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from db import get_site_elements
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для проверки выполнимости интернет-магазина 💻")

async def site_elements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    elements = get_site_elements()
    if not elements:
        await update.message.reply_text("В базе нет элементов сайта 😕")
        return
    
    text = "📋 Элементы сайта:\n"
    for el in elements:
        text += f"• {el[1]} ({el[2]})\n"
    await update.message.reply_text(text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("site_elements", site_elements))
    app.run_polling()

if __name__ == "__main__":
    main()
