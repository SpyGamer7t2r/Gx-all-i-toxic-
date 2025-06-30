from pyrogram import filters
from pyrogram.types import Message
from config import MONGO_DB_URI, SUDOERS
from motor.motor_asyncio import AsyncIOMotorClient
from SONALI import app
import openai

client = AsyncIOMotorClient(MONGO_DB_URI)
db = client["ChatGPT_DB"]
chatbots = db["chatbot_status"]

# Check if chatbot is enabled in this chat
async def is_chatbot_enabled(chat_id: int) -> bool:
    return await chatbots.find_one({"chat_id": chat_id}) is not None

# Enable or disable chatbot in a chat
@app.on_message(filters.command(["chatbot"]) & filters.user(SUDOERS))
async def toggle_chatbot(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Use: `/chatbot on` or `/chatbot off`", quote=True)

    status = message.command[1].lower()
    chat_id = message.chat.id

    if status == "on":
        await chatbots.update_one({"chat_id": chat_id}, {"$set": {"chat_id": chat_id}}, upsert=True)
        await message.reply_text("✅ Chatbot is now enabled in this chat.")
    elif status == "off":
        await chatbots.delete_one({"chat_id": chat_id})
        await message.reply_text("❌ Chatbot has been disabled in this chat.")
    else:
        await message.reply_text("Invalid usage.\nUse: `/chatbot on` or `/chatbot off`")

# Handle all messages like a chatbot
@app.on_message(filters.text & ~filters.via_bot & ~filters.edited & ~filters.command(["chatbot"]))
async def chat_handler(_, message: Message):
    chat_id = message.chat.id
    if not await is_chatbot_enabled(chat_id):
        return

    # Avoid replying to other users, only reply to itself
    if message.reply_to_message and message.reply_to_message.from_user.id != (await app.get_me()).id:
        return

    reply = await get_ai_response(message.text)
    if reply:
        await message.reply_text(reply)

# Call OpenAI API and return result
async def get_ai_response(text: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful, human-like Telegram bot."},
                {"role": "user", "content": text}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return "😔 Sorry, I couldn't connect to the AI service."