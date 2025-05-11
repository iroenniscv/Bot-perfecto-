from pyrogram import Client, filters

# Credenciales (¡Recuerda que esto NO es seguro para producción!)
api_id = 9063611
api_hash = "4ac77fe0baef38b8937f3339c2854663"
bot_token = "7853180813:AAE6Hch4qwXJ38E-iKmaBe3yZTjCys-hbe4"

app = Client("mi_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    """Maneja el comando /start"""
    await message.reply_text("🤖 Bot de prueba activo desde Koyeb! 🚀\n\nEnvíame cualquier mensaje y te lo repetiré.")

@app.on_message(filters.text & filters.private)
async def echo(client, message):
    """Repite los mensajes privados"""
    await message.reply_text(f"📢 Eco: {message.text}")

if __name__ == "__main__":
    print(">> Bot de prueba iniciado <<")
    app.run()
