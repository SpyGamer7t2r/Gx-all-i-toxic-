# SONALI/plugins/ai_chat.py
import openai
from pyrogram import filters
from pyrogram.types import Message
from config import OPENAI_API_KEY
from SONALI import app
from SONALI.utils.database import is_chatbot_enabled

openai.api_key = OPENAI_API_KEY

@app.on_message((filters.text & ~filters.command(["chatbot"])) & (filters.private | filters.group))
async def ai_chat(client, message: Message):
    chat_id = message.chat.id
    if not await is_chatbot_enabled(chat_id):
        return
    if message.from_user and message.from_user.is_bot:
        return
    if message.chat.type != "private":
        if not message.reply_to_message or message.reply_to_message.from_user.id != (await app.get_me()).id:
            return
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a smart, helpful and friendly chatbot."},
                      {"role": "user", "content": message.text}]
        )
        await message.reply_text(response["choices"][0]["message"]["content"])
    except Exception as e:
        await message.reply_text(f"❌ ChatGPT Error:\n`{e}`")