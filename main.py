import os
from typing import  Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN:Final = os.getenv('token')
BOT_USERNAME:Final = os.getenv('BOT_USERNAME')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! How you're doing?")

async def update_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Understood! Data will be updated. Please hold on a second")

def handler_response(text:str) -> str:
    lowercase = text.lower()

    if 'beli' in lowercase:
        return 'Berikut adalah transaksi yang kamu masukkan.'

    return 'Masukkan data yang lebih mudah dipahami'

async def handler_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User {update.message.chat.id} in {message_type}: {text}')

    response = handler_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)

async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('update', update_command))

    app.add_handler(MessageHandler(filters.TEXT, handler_message))

    app.add_error_handler(error)

    print('Bot is polling....')
    app.run_polling(poll_interval=3)