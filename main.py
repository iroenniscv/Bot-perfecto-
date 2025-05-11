# Instala los requisitos primero:
# pip install pyrogram openai python-dotenv tgcrypto

import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

# Configuración
API_ID = os.getenv("API_ID") or 123456
API_HASH = os.getenv("API_HASH") or "tu_api_hash"
BOT_TOKEN = os.getenv("BOT_TOKEN") or "tu_bot_token"
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY") or "sk-a15b913adb254aaeaa838f4092306e24"

# Inicializar clientes
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
app = Client("deepseek_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Diccionario para almacenar historial de conversaciones
conversations = {}

def get_deepseek_response(user_id: int, text: str) -> str:
    if user_id not in conversations:
        conversations[user_id] = [
            {"role": "system", "content": "Eres un asistente útil que responde en español."}
        ]
    
    conversations[user_id].append({"role": "user", "content": text})
    
    try:
        response = deepseek_client.chat.completions.create(
            model="deepseek-chat",
            messages=conversations[user_id],
            stream=False
        )
        
        assistant_reply = response.choices[0].message.content
        conversations[user_id].append({"role": "assistant", "content": assistant_reply})
        
        if len(conversations[user_id]) > 10:
            conversations[user_id] = conversations[user_id][-8:]
            
        return assistant_reply
        
    except Exception as e:
        print(f"Error con DeepSeek API: {e}")
        return "❌ Ocurrió un error al procesar tu solicitud."

# Comandos del bot
@app.on_message(filters.command(["start", "help"]))
async def start(client: Client, message: Message):
    await message.reply_text(
        "🤖 Hola! Soy un bot conectado a DeepSeek AI.\n\n"
        "Simplemente escribe tu mensaje y te responderé.\n\n"
        "Usa /new para comenzar una nueva conversación."
    )

@app.on_message(filters.command("new"))
async def new_chat(client: Client, message: Message):
    user_id = message.from_user.id
    conversations.pop(user_id, None)
    await message.reply_text("♻️ Nueva conversación iniciada. El historial anterior se ha borrado.")

# Corrección importante aquí:
@app.on_message(filters.private & ~filters.command(["start", "help", "new"]))
async def chat(client: Client, message: Message):
    user_id = message.from_user.id
    response = get_deepseek_response(user_id, message.text)
    await message.reply_text(response)

if __name__ == "__main__":
    print("Bot iniciado...")
    app.run()
