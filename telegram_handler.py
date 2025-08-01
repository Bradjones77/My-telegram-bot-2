from telegram import Update
from telegram.ext import ContextTypes
from signals import get_trade_signal

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "/signal - Get a general trade signal\n"
        "/signal.s - Get a short-term trade signal\n"
        "/signal.l - Get a long-term trade signal\n"
        "#tradeid - Confirm a trade you entered (e.g. #123)\n"
        "/help - Show this help message"
    )
    await update.message.reply_text(text)

async def signal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sig = get_trade_signal("general")
    await update.message.reply_text(format_signal(sig))

async def signal_short(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sig = get_trade_signal("short")
    await update.message.reply_text(format_signal(sig))

async def signal_long(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sig = get_trade_signal("long")
    await update.message.reply_text(format_signal(sig))

async def confirm_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    if msg.startswith("#"):
        trade_id = msg[1:]
        await update.message.reply_text(f"✅ Trade {trade_id} confirmed! Tracking started.")

def format_signal(sig):
    return (
        f"📊 Trade Signal\n"
        f"Coin: {sig['coin']}\n"
        f"Action: {sig['action']}\n"
        f"Stop Loss: {sig['stop_loss']}%\n"
        f"Confidence: {sig['confidence']}%\n"
        f"Type: {sig['type']}"
    )
