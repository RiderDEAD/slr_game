import os
import asyncio  # Добавляем этот импорт в самый верх файла!
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

async def main():
    # Настройка порта для Render
    port = int(os.environ.get("PORT", 8000))
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print(f"Бот успешно поднят на порту {port} и готов крутиться 24/7!")
    
    # Инициализируем приложение перед запуском
    await app.initialize()
    await app.updater.start_polling()
    await app.start()
    
    # Держим бота запущенным, пока сервер работает
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    # Вот этот метод создаст нужный Event Loop в Python 3.14+ автоматически!
    asyncio.run(main())
