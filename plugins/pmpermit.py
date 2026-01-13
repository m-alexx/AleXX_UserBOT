from pyrogram import Client, filters

ALLOWED = set()

@Client.on_message(filters.private & ~filters.me)
async def pmpermit(_, m):
    if m.from_user.id not in ALLOWED:
        await m.reply(
            "⚠️ This is a protected PM.\n"
            "Please wait for approval.\n"
            "— ALEXX USERBOT"
        )

@Client.on_message(filters.command("approve", ".") & filters.me)
async def approve(_, m):
    if m.reply_to_message:
        ALLOWED.add(m.reply_to_message.from_user.id)
        await m.edit("✅ User approved")
