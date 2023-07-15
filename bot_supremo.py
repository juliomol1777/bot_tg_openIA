import telegram
import telegram.ext
import openai

# Configura el token de acceso de tu bot de Telegram
bot_token = "aqui va el token"

# Configura tu clave de API de GPT-3
openai.api_key = "aqui va el token"

# Define una función para manejar los mensajes que reciba tu bot
def handle_message(update, context):
    # Obtiene el texto del mensaje recibido
    message_text = update.message.text
    
    # Envía el mensaje recibido a la API de GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message_text,
        max_tokens=200,
        temperature=0.2
    )
    
    # Obtiene la respuesta generada por la API de GPT-3
    response_text = response.choices[0].text.strip()
    
    # Envía la respuesta a Telegram
    update.message.reply_text(response_text)

# Crea un "telegram.ext.Updater" y registra la función "handle_message" como manejador de mensajes
updater = telegram.ext.Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# Inicia el bot
updater.start_polling()