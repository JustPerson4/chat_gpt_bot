from telebot.types import ReplyKeyboardMarkup,KeyboardButton

def contact_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button = KeyboardButton('share button',request_contact=True)
    kb.add(button)
    return kb

def start_chatGPT_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button = KeyboardButton('START')
    kb.add(button)
    return kb

def save_chatGPT_answer_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button = KeyboardButton('SAVE')
    kb.add(button)
    return kb
