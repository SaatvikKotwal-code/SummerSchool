import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

# Load .env if needed
load_dotenv()

# Replace with your actual keys or load from environment
API_TOKEN = "8327510863:AAGCUzDzTELThpR4w9Uc_G-ToZ3vA6MC82k"
OPENAI_API_KEY = "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"


# Initialize bot and OpenAI client
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

# Inline keyboard
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Click Me!", callback_data="button_clicked")]
])

# /start command
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("👋 Hello! Ask me anything or click the button below.", reply_markup=keyboard)

# Handle normal messages with OpenAI
@dp.message()
async def chat_handler(message: types.Message):
    user_input = message.text
    await message.answer("🤖 Thinking...")

    try:
        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" / "gpt-4o" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        reply = response.choices[0].message.content.strip()
        await message.answer(reply)

    except Exception as e:
        await message.answer(f"⚠️ Error talking to OpenAI:\n{e}")

# Handle inline button clicks
@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    if callback.data == "button_clicked":
        await callback.answer("You clicked the button!", show_alert=True)
        await callback.message.answer("✅ Button click acknowledged.")

# Main function
async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
