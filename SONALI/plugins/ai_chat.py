import openai
from pyrogram import filters
from pyrogram.types import Message
from config import OPENAI_API_KEY
from SONALI import app
from SONALI.utils.database import is_chatbot_enabled

openai.api_key = OPENAI_API_KEY

@app.on_message(filters.text & ~filters.command(["chatbot"]) & filters.private | filters.group)
async def ai_chat(client, message: Message):
    chat_id = message.chat.id

    # Check if chatbot is enabled
    if not await is_chatbot_enabled(chat_id):
        return

    if message.from_user and message.from_user.is_bot:
        return

    try:
        reply = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        text = reply['choices'][0]['message']['content']
        await message.reply_text(text)
    except Exception as e:
        await message.reply_text("❌ ChatGPT Error: " + str(e))