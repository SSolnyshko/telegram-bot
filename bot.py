import json
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import os
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

with open('slang.json', 'r', encoding='utf-8') as f:
    slang = json.load(f)

@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer(
        "Сәлем, бро! 👋\n\n"
        "Мен орыс сленгін қазақ тіліне аударам.\n"
        "Тек маған кез келген сөзді жаз, мысалы: *краш*, *рофл*, *чекать*.\n\n"
        "Бастайық! 🚀",
        parse_mode="Markdown"
    )

@dp.message()
async def translate(msg: Message):
    word = msg.text.lower().strip()
    if word in slang:
        await msg.reply(f"📘 {word} — {slang[word]}")
    else:
        await msg.reply("❌ Бұл сөз тізімде жоқ, бро 😔")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
