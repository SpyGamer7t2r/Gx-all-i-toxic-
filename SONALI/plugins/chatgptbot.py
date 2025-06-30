from pyrogram import filters
from pyrogram.types import Message
from config import MONGO_DB_URI
from pymongo import MongoClient
from SONALI import app
import openai

client = MongoClient(MONGO_DB_URI)
db = client["ChatGPT_DB"]
chatbots = db["chatbot_status"]

def is_chatbot_enabled(chat_id: int) -> bool:
    return chatbots.find_one({"chat_id": chat_id}) is not None

@app.on_message(filters.command(["chatbot"]) & filters.user(SUDOERS))
async def toggle_chatbot(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Use: `/chatbot on` or `/chatbot off`", quote=True)

    status = message.command[1].lower()
    chat_id = message.chat.id

    if status == "on":
        chatbots.update_one({"chat_id": chat_id}, {"$set": {"chat_id": chat_id}}, upsert=True)
        await message.reply_text("✅ Chatbot is now enabled in this chat.")
    elif status == "off":
        chatbots.delete_one({"chat_id": chat_id})
        await message.reply_text("❌ Chatbot has been disabled in this chat.")
    else:
        await message.reply_text("Invalid usage.\nUse: `/chatbot on` or `/chatbot off`")

@app.on_message(filters.text & ~filters.via_bot & ~filters.edited & ~filters.command(["chatbot"]))
async def chat_handler(_, message: Message):
    chat_id = message.chat.id
    if not is_chatbot_enabled(chat_id):
        return

    if message.reply_to_message and message.reply_to_message.from_user.id != (await app.get_me()).id:
        return

    reply = await get_ai_response(message.text)
    if reply:
        await message.reply_text(reply)

async def get_ai_response(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a smart, helpful and friendly chatbot."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return "Error contacting AI service."