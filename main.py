from pyrogram import Client, filters
import asyncio
from datetime import datetime

# Configuración (usa variables de entorno en Koyeb)
api_id = 9063611
api_hash = "4ac77fe0baef38b8937f3339c2854663"
bot_token = "7855714549:AAHKZmpAa0Y0IBNFEV7ZmWSTnOuHzGvehYY"
admin_chat_id = "TU_CHAT_ID"  # Reemplaza con tu ID de chat (obténlo con @userinfobot)

app = Client("mi_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Función para enviar mensajes automáticos
async def send_heartbeat():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await app.send_message(admin_chat_id, f"❤️ Latido del bot - Activo ({now})")
        await asyncio.sleep(2)  # Espera 60 segundos

# Comando /start
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("¡Bot activo! Recibirás un latido cada minuto.")

# Iniciar el temporizador al arrancar el bot
@app.on_startup()
async def startup():
    app.loop.create_task(send_heartbeat())

print(">> Bot + Temporizador activo <<")
app.run()
