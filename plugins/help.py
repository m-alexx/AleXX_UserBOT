from pyrogram import Client, filters

HELP = """
╭─❍ 『 ALEXX USERBOT 』 ❍─╮

💖 ROMANCE
.love .crush .romantic
.forher .forhim

💗 ANIMATED LOVE
.heart .lovetype .miss
.goodmorning .goodnight

🫶 AFFECTION
.hug .hugme
.kiss .kissme

🛡️ SYSTEM
.afk .pmpermit

╰──────────────╯
"""

@Client.on_message(filters.command("help", ".") & filters.me)
async def help(_, m):
    await m.edit(HELP)
