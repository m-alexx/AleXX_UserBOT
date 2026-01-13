import asyncio
from pyrogram import Client, filters

@Client.on_message(filters.command("kiss", ".") & filters.me)
async def kiss(_, m):
    frames = ["😊","😊💋","😘","💋❤️"]
    for f in frames:
        await m.edit(f)
        await asyncio.sleep(0.7)
