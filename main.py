import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotSettings
from dotenv import load_dotenv
import asyncio

# Load .env variables (for local testing only)
load_dotenv()

# Get token from environment
API_TOKEN = os.getenv("BOT_TOKEN")
print("Loaded BOT_TOKEN:", API_TOKEN)

# Create bot with proper parse_mode setup for aiogram v3
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotSettings(parse_mode=ParseMode.HTML)
)

# Create dispatcher
dp = Dispatcher()

# Simple /start handler
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("<b>👋 Welcome!</b>\nThis is your VIP bot.", parse_mode=ParseMode.HTML)

# Simple /vip handler
@dp.message(Command("vip"))
async def vip_handler(message: Message):
    await message.answer(
        "⭐️ <b>VIP SUBSCRIPTION</b> ⭐️\n\n"
        "📉 Our services:\n"
        "1️⃣ 8000+ PIPS monthly\n"
        "2️⃣ 10-20 VIP signals daily\n"
        "3️⃣ Over 95% accuracy\n"
        "4️⃣ Trade setups & analysis\n"
        "5️⃣ Volatility, Boom/Crash, Crypto signals",
        parse_mode=ParseMode.HTML
    )

# Start the bot
async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
