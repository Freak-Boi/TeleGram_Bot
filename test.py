import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7271494340:AAGlkgdfnDTwu2p211w1kCn-Ucv_Ms-f3pM'

# Base URL for redirection
BASE_REDIRECT_URL = 'http://example.com/'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    redirect_url = f"{BASE_REDIRECT_URL}{user_id}"
    
    keyboard = [
        [InlineKeyboardButton("Start", url=redirect_url)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Welcome! Click the button to be redirected:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'about':
        await query.edit_message_text(text="This bot redirects you to a specific website with your user ID.")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()