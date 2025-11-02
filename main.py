from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from db import get_site_elements
from factory import TaskFactory
from adapter import ElementDB, ElementAdapter
from chain import ComplexityHandler, DeveloperHandler, DefaultHandler
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот проверки выполнимости интернет-магазина 💻")

async def list_elements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_site_elements()
    adapter = ElementAdapter(ElementDB(data))
    elements = adapter.list_names()
    await update.message.reply_text("Элементы сайта:\n" + "\n".join(elements))

async def task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("Укажи тип задачи: /task frontend или /task backend")
        return
    try:
        task = TaskFactory.create_task(args[0])
        await update.message.reply_text(task.execute())
    except ValueError as e:
        await update.message.reply_text(str(e))

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    handler_chain = ComplexityHandler(DeveloperHandler(DefaultHandler()))
    response = handler_chain.handle(text)
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("elements", list_elements))
    app.add_handler(CommandHandler("task", task))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("🚀 Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()

