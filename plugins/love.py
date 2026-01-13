import random
from pyrogram import Client, filters

QUOTES = [
    "I found my peace in you ❤️",
    "You are my favorite feeling 💫",
    "Loving you is easy 💕",
]

@Client.on_message(filters.command("love", ".") & filters.me)
async def love(_, m):
    await m.edit(random.choice(QUOTES))
