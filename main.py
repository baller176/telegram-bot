import os
print("BOT_TOKEN from env:", os.getenv("BOT_TOKEN"))
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKENdaily ✅\n"
        "3️⃣ Over 95% accuracy weekly 😍\n"
        "4️⃣ Analysis and trade setups ✅\n"
        "5️⃣ Volatility, Crash, Step, Boom and crypto signals\n\n"
        "💬 Contact admin 👉 @Gold_Scalper08",
        parse_mode="Markdown"
    )

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main()) 
