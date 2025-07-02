import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("7211206928:AAF2EA_PLC5zUlPwvxWh4WGiX_uWTU2RBcs")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("👋 Welcome to UK_Gold_Scalper VIP Bot!\n\nType /vip to view our subscription plans.")

@dp.message(Command("vip"))
async def vip_handler(message: Message):
    await message.answer(
        "⭐️ *VIP SUBSCRIPTION*\n"
        "#UK_Gold_scalper_premium_membership\n\n"
        "📉👇 *Our services rendered* 👇\n"
        "1️⃣ 8000+ PIPS guaranteed monthly 💹\n"
        "2️⃣ 10-20 VIP signals posted daily ✅\n"
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
