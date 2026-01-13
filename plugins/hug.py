import asyncio
from pyrogram import Client, filters

@Client.on_message(filters.command("hug", ".") & filters.me)
async def hug(_, m):
    frames = ["🤍","🫶","🫂","🫂 Tight hug ❤️"]
    for f in frames:
        await m.edit(f)
        await asyncio.sleep(0.7)
