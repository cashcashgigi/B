import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("7557223354:AAEcRHyRvSMr0wsmeDlHzAeQ5k0KCaj8ZsA")  # Récupère le token depuis Railway

def start(update, context):
    user = update.message.from_user
    name = user.first_name or "Inconnu"
    username = f"@{user.username}" if user.username else "Aucun"
    chat_id = update.message.chat_id
    language = user.language_code or "Non défini"

    message = f"👤 Name: {name}\n🆔 Username: {username}\n📱 Chat ID: {chat_id}\n🉐 Language: {language}"
    update.message.reply_text(message)

bot = Bot(token=TOKEN)
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
