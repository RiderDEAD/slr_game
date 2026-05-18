import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# ВСТАВЬ СЮДА ТОКЕН СВОЕГО БОТА ИЗ @BotFather
TOKEN = "8738502248:AAHlAi-h59fWgjxthMdymhTRtTw0xoHfLPM"

# ВСТАВЬ СЮДА ССЫЛКУ НА СВОЙ INDEX.HTML (с Render или GitHub)
WEB_APP_URL = "https://riderdead.github.io/slr_game/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаем кнопку запуска мини-приложения
    keyboard = [
        [
            InlineKeyboardButton(
                text="🎮 ЗАПУСТИТЬ SLR 2", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text=f"Привет, {update.effective_user.first_name}!\n"
             f"Мы с кентом разработали кроссплатформенный клон Slay the Spire II.\n\n"
             f"Нажимай кнопку ниже, чтобы начать играть прямо внутри Telegram!",
        reply_markup=reply_markup
    )

def main():
    # Настройка порта для Render (чтобы он видел, что приложение живо)
    port = int(os.environ.get("PORT", 8000))
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print(f"Бот успешно поднят на порту {port} и готов крутиться 24/7!")
    
    # Запуск бота в режиме вебхука или полинга. 
    # Для бесплатного деплоя на Render полинг отлично подходит:
    app.run_polling()

if __name__ == "__main__":
    main()