import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram_handler import help_command, signal_command, signal_short, signal_long, confirm_trade
from config import TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("signal", signal_command))
    app.add_handler(CommandHandler("signal.s", signal_short))
    app.add_handler(CommandHandler("signal.l", signal_long))
    app.add_handler(MessageHandler(filters.Regex("^#"), confirm_trade))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
