import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("8738502248:AAHlAi-h59fWgjxthMdymhTRtTw0xoHfLPM")
WEB_APP_URL = "https://riderdead.github.io/slr_game/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[
        InlineKeyboardButton(
            text="🎮 ЗАПУСТИТЬ SLR 2",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        text=f"Привет, {update.effective_user.first_name}!\n"
             f"Мы с кентом разработали кроссплатформенный клон Slay the Spire II.\n\n"
             f"Нажимай кнопку ниже, чтобы начать играть прямо внутри Telegram!",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен!")
    app.run_polling()
