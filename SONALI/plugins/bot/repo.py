from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗗𝗔𝗥𝗞 𝗕𝗢𝗧𝗦 [🇮🇳]" 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @Gx_toxic_git ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗕ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/dark_x_knight_musiczz_support"),
          InlineKeyboardButton("メ♡ 𝐈𝐍𝐅𝐈𝐍𝐈𝐓𝐘 ❘ ❯ </𝟑𓂃ֶꪳ♾️", url="https://t.me/Destiny_Infinity_Og"),
          ],
               [
                InlineKeyboardButton("𝗗𝗔𝗥𝗞 𝗕𝗢𝗧𝗦 [🇮🇳]", url=f"https://t.me/dark_x_knight_musiczz_support"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/Leo_musicz_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/f202298de2e7f7a025820-bbc764222493f10071.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
