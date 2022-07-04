# pip install python-telegram-bot --upgrade

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Напиши мне город, а я отправлю погоду в нём."
    )

async def send_weather(update, context):
    message_text = update.message.text

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Хочешь посмотреть в городе {message_text}?',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Посмотреть...', web_app=WebAppInfo(f'https://wttr.in/{message_text}'))]]
        )
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token('5475995602:AAEJPKAsmIY2pkcQKZI1xDI_grpe0vLZb0o').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    weather_sender = MessageHandler(filters.TEXT, send_weather)
    application.add_handler(weather_sender)
    
    application.run_polling()
else:
    print(f"{__name__=}")