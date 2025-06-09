import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [["\u270A Включить сервер"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        "Добро пожаловать! Нажмите кнопку ниже, чтобы включить сервер.",
        reply_markup=reply_markup,
    )

def poweron(update: Update, context: CallbackContext) -> None:
    mac = os.environ.get("PROXMOX_SERVER_MAC")
    if not mac:
        update.message.reply_text("MAC-адрес не задан")
        return
    os.system(f"wakeonlan {mac}")
    update.message.reply_text("Запрос на включение отправлен")

def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Set TELEGRAM_BOT_TOKEN environment variable")
        return
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("\u270A Включить сервер", poweron))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
