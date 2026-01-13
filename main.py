from pyrogram import Client
import config
import os

app = Client(
    name="allexx",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.SESSION,
    plugins=dict(root="plugins")
)

print("🔥 ALEXX USERBOT STARTED 🔥")

app.run()
