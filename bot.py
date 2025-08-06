from deepseek import ask_deepseek

@dp.message_handler(commands=['ask'])
async def handle_ask(message: types.Message):
    prompt = message.get_args()
    if not prompt:
        await message.reply("Напиши запрос после /ask")
        return
    await message.reply("⏳ Думаю...")

    try:
        reply = ask_deepseek(prompt)
        await message.reply(reply)
    except Exception as e:
        await message.reply(f"Ошибка: {e}")
