from pyrogram import Client, filters

AFK = False
REASON = ""

@Client.on_message(filters.command("afk", ".") & filters.me)
async def afk(_, m):
    global AFK, REASON
    REASON = m.text.split(maxsplit=1)[1] if len(m.text.split()) > 1 else "AFK"
    AFK = True
    await m.edit(f"💤 AFK\nReason: {REASON}")

@Client.on_message(filters.me)
async def back(_, m):
    global AFK
    if AFK:
        AFK = False
        await m.reply("✅ Back online")
