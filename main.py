from pyrogram import Client, filters

api_id = 9063611
api_hash = "4ac77fe0baef38b8937f3339c2854663"
bot_token = "7855714549:AAFmz9jsFqZD-1XKKU6hCvvlkxFZGDjRgnA"

app = Client("mi_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Bot activo desde Koyeb! 🚀")

@app.on_message(filters.text & filters.private)
def echo(client, message):
    message.reply_text(f"Echo: {message.text}")

print(">> Bot en ejecución <<")
app.run()
