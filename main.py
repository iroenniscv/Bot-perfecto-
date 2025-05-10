from pyrogram import Client, filters
import asyncio
from datetime import datetime

# Configuración - usa variables de entorno en producción
api_id = 9063611
api_hash = "4ac77fe0baef38b8937f3339c2854663"
bot_token = "7855714549:AAHKZmpAa0Y0IBNFEV7ZmWSTnOuHzGvehYY"
admin_chat_id = "8197155469"  # Reemplaza con tu ID real

app = Client("mi_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def send_heartbeat():
    while True:
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await app.send_message(admin_chat_id, f"❤️ Bot activo ({now})")
            await asyncio.sleep(60)
        except Exception as e:
            print(f"Error en heartbeat: {e}")
            await asyncio.sleep(30)  # Reintentar después de 30 segundos

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("¡Bot en línea! Enviaré latidos cada minuto.")

# Manejar el inicio
async def main():
    await app.start()
    print("Bot iniciado")
    asyncio.create_task(send_heartbeat())
    await asyncio.Event().wait()  # Mantener el bot corriendo

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot detenido")
    finally:
        app.stop()
