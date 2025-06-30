from typing import Dict

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

# Initialize MongoDB client and database
mongo = AsyncIOMotorClient(MONGO_DB_URI)
db = mongo["SONALI"]

# Collections
coupledb = db["couple"]
afkdb = db["afk"]
nightmodedb = db["nightmode"]
notesdb = db["notes"]
filtersdb = db["filters"]

# --- COUPLE SYSTEM ---

async def _get_lovers(cid: int) -> Dict:
    data = await coupledb.find_one({"chat_id": cid})
    return data["couple"] if data and "couple" in data else {}

async def _get_image(cid: int) -> str:
    data = await coupledb.find_one({"chat_id": cid})
    return data.get("img", "") if data else ""

async def get_couple(cid: int, date: str):
    lovers = await _get_lovers(cid)
    return lovers.get(date, False)

async def save_couple(cid: int, date: str, couple: dict, img: str):
    lovers = await _get_lovers(cid)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": cid},
        {"$set": {"couple": lovers, "img": img}},
        upsert=True
    )

# You can define more async DB functions here (e.g. for AFK, Notes, etc.)