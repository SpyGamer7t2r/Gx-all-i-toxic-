import openai
from pyrogram import filters
from pyrogram.types import Message
from config import OPENAI_API_KEY
from SONALI import app
from SONALI.utils.database import is_chatbot_enabled

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

# AI Chat handler for private and group chats (if chatbot is enabled)
@app.on_message(filters.text & ~filters.command(["chatbot"]) & (filters.private | filters.group))
async def ai_chat(client, message: Message):
    chat_id = message.chat.id

    # Skip if chatbot is disabled
    if not await is_chatbot_enabled(chat_id):
        return

    # Ignore bot messages
    if message.from_user and message.from_user.is_bot:
        return

    # Avoid replying unless it's a direct reply to the bot or PM
    if message.chat.type != "private":
        if not message.reply_to_message:
            return
        if message.reply_to_message.from_user.id != (await app.get_me()).id:
            return

    try:
        # Make request to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a smart, helpful and friendly chatbot."},
                {"role": "user", "content": message.text}
            ]
        )
        reply_text = response["choices"][0]["message"]["content"]
        await message.reply_text(reply_text)

    except Exception as e:
        await message.reply_text(f"❌ ChatGPT Error:\n`{str(e)}`")