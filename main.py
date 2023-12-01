# # import openai
# # openai.api_key = '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'

# # import telebot

# # import database

# # import buttons

# # import random

# # TOKEN = '6576260904:AAFFlaQ4l8oqSVe-peUdkGvCQIx0NTR-Msk'

# # bot = telebot.TeleBot(TOKEN)

# # @bot.message_handler(commands=['start'])
# # def start_message(message):
# #     user = database.check_user(message.from_user.id)
    
# #     if user:
# #         bot.send_message(message.from_user.id,'To use chatGPT press start button',reply_markup=buttons.start_chatGPT_button())

# #     else:
# #         bot.send_message(message.from_user.id, 'To start using bot pls share contact!',reply_markup=buttons.contact_button())
        
# #     bot.send_message(message.from_user.id, 'To start using bot pls share contact!',reply_markup=buttons.contact_button())
# #     bot.register_next_step_handler(message,get_contact)
    
# # def get_contact(message):
# #     if message.contact:
# #         user_phone = message.contact.phone_number
# #         first_name = message.contact.first_name
# #         tg_id = message.from_user.id
        
# #         database.register_user(tg_id,first_name,user_phone)
        
# #         bot.send_message(message.from_user.id, 'To use the button', reply_markup=buttons.start_chatGPT_button())
        
# #     else:
# #         bot.send_message(message.from_user.id, 'Place to share your contact use the button', reply_markup=buttons.contact_button())
# #         bot.register_next_step_handler(message,get_contact) 


# # @bot.message_handler(content_types=['text'])
# # def start_chatGPT(message):
# #     list = ['savolingizni kriring','savol yozing','nmani bilishni hohlaysiz']
# #     bot.send_message(message.from_user.id, random.choice(list), reply_markup=buttons.save_chatGPT_answer_button())
              
# # @bot.message_handler(content_types=['text'])
# # def text_message(message):
# #     user = database.check_user(message.from_user.id)
# #     if message.text.lower() == 'start chatgpt' and user:
# #         reply = ''
# #         response = openai.ChatCompletion.create(
# #             model = 'gpt-3.5-turbo',
# #             message = [{'role':'user', 'content':message.text}],
# #             timout = 15,
# #         )
    
# #         if response and response.choices:
# #             reply = response.choices[0]['message']['content']
        
# #         else:
# #             reply ='Nmani xolisiz bilishini((('
    
# #         bot.send_message(message.from_user.id, reply)
# #     else:
# #         bot.send_message(message.from_user.id, 'Javob olish uchun reistiratsiyadan oting')
# #         # bot.register_next_step_handler(message,get_contact)
    
    
    
# # # bot.polling()
# # import openai

# # # Set your OpenAI GPT-3 API key
# # openai.api_key = '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'

# # def chat_with_gpt3(prompt):
# #     # Define the prompt for the chatbot
# #     # You can customize the prompt based on your application
# #     prompt = f'User: {prompt}\nChatGPT:'

# #     # Make a request to the OpenAI GPT-3 API
# #     response = openai.Completion.create(
# #         engine="text-davinci-003",  # Choose the GPT-3 engine
# #         prompt=prompt,
# #         max_tokens=150,  # Adjust the max_tokens parameter based on your needs
# #         temperature=0.7,  # Adjust the temperature parameter for creativity
# #     )

# #     # Extract and return the generated response
# #     return response.choices[0].text.strip()

# # # Example usage
# # user_input = "Tell me a joke."
# # bot_response = chat_with_gpt3(user_input)
# # print(f"User: {user_input}")
# # print(f"ChatGPT: {bot_response}")







# import logging
# import telebot
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
# from telegram import Filters


# import openai

# # Set your OpenAI GPT-3 API key
# openai.api_key = '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'

# # Set your Telegram bot token
# TELEGRAM_BOT_TOKEN = '6576260904:AAE6tQIle00ahAFZ1IINY80B65uUeB6otds'

# # Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# logger = logging.getLogger(__name__)

# # Define the function to handle incoming messages
# def handle_message(update: Update, context: CallbackContext) -> None:
#     user_input = update.message.text
#     bot_response = chat_with_gpt3(user_input)
#     update.message.reply_text(f"ChatGPT: {bot_response}")

# # Define the function to chat with GPT-3
# def chat_with_gpt3(prompt):
#     prompt = f'User: {prompt}\nChatGPT:'
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150,
#         temperature=0.7,
#     )
#     return response.choices[0].text.strip()

# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Hi! I am your ChatGPT bot. Send me a message, and I will respond.')

# def main() -> None:
#     updater = Updater(TELEGRAM_BOT_TOKEN)

#     dp = updater.dispatcher

#     # Define the command handlers
#     dp.add_handler(CommandHandler("start", start))

#     # Define the message handler
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

#     # Start the Bot
#     updater.start_polling()

#     # Run the bot until you send a signal to stop it
#     updater.idle()

# if __name__ == '__main__':
#     main()




# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# def start(update, context):
#     update.message.reply_text('Hello! This is your bot.')

# def handle_text_message(update, context):
#     text_received = update.message.text
#     # Your logic here based on the received text
#     update.message.reply_text(f'You said: {text_received}')

# def main():
#     updater = Updater("6576260904:AAE6tQIle00ahAFZ1IINY80B65uUeB6otds", use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text_message))

#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()













import telebot
import openai

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

# Set your Telegram bot token
TELEGRAM_BOT_TOKEN = '6576260904:AAE6tQIle00ahAFZ1IINY80B65uUeB6otds'

# Initialize the bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Define the start command handler
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hi! I am your ChatGPT bot. Send me a message, and I will respond.")

# Define the message handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    bot_response = chat_with_gpt3(user_input)
    bot.reply_to(message, f"ChatGPT: {bot_response}")

# Define the function to chat with GPT-3
def chat_with_gpt3(prompt):
    prompt = f'User: {prompt}\nChatGPT:'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Polling loop to keep the bot running
bot.polling()
