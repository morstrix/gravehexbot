import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8453653824:AAFr1Clio81FR2iW8m3UQXPIvunjm5L7qVw"
ASKPLEX_USERNAME = "@askplexbot"

logging.basicConfig(level=logging.INFO)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    if f"@{context.bot.username.lower()}" in text.lower():
        query = text.replace(f"@{context.bot.username}", "").strip()
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

        try:
            # Пересылаем запрос в @askplexbot
            askplex_msg = await context.bot.send_message(chat_id=ASKPLEX_USERNAME, text=query)

            # Сообщаем, что ждём ответ
            await update.message.reply_text("🌀 Запрос отправлен в Perplexity. Ожидаю ответ...")

        except Exception as e:
            logging.error(f"Ошибка при пересылке в @askplexbot: {e}")
            await update.message.reply_text("⚠️ Не удалось отправить запрос в Perplexity.")

application = ApplicationBuilder().token(BOT_TOKEN).build()
application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

async def main():
    await application.initialize()
    await application.start()
    print("🤖 GraveHexBot работает.")
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
