import asyncio
from pyrogram import Client, filters

@Client.on_message(filters.command("heart", ".") & filters.me)
async def heart(_, m):
    for f in ["🤍","💛","🧡","❤️","❤️‍🔥"]:
        await m.edit(f)
        await asyncio.sleep(0.6)
