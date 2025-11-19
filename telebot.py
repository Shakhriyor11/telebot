import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Replace with your bot's token
bot = telebot.TeleBot('8595535041:AAGuUW_Nj5UzSCyl8ylE6NSOKBAnQPoGRBU')

# Define the menu buttons
def get_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # Menu with 2 buttons per row
    btn_menu = KeyboardButton('Menu')  # Button for "Menu"
    btn_aksiya = KeyboardButton('Aksiya')  # Button for "Aksiya" (promotions)
    btn_buyurtmalarim = KeyboardButton('Buyurtmalarim')  # Button for "Buyurtmalarim" (my orders)
    btn_boglanish = KeyboardButton("Bog'lanish")  # Button for "Bog'lanish" (contact)
    
    markup.add(btn_menu, btn_aksiya, btn_buyurtmalarim, btn_boglanish)
    return markup

# Handler for /start command - shows the menu
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Xush kelibsiz! Quyidagi menyudan tanlang:", reply_markup=get_main_menu())

# Handlers for button clicks (add logic here as needed)
@bot.message_handler(func=lambda message: message.text == 'Menu')
def handle_menu(message):
    bot.send_message(message.chat.id, "Menu bo'limi: Bu yerda menyu haqida ma'lumotlar.")  # Add your logic

@bot.message_handler(func=lambda message: message.text == 'Aksiya')
def handle_aksiya(message):
    bot.send_message(message.chat.id, "Aksiya bo'limi: Joriy aksiyalar haqida.")  # Add your logic

@bot.message_handler(func=lambda message: message.text == 'Buyurtmalarim')
def handle_buyurtmalarim(message):
    bot.send_message(message.chat.id, "Buyurtmalarim bo'limi: Sizning buyurtmalaringiz ro'yxati.")  # Add your logic

@bot.message_handler(func=lambda message: message.text == "Bog'lanish")
def handle_boglanish(message):
    bot.send_message(message.chat.id, "Bog'lanish bo'limi: Admin bilan bog'lanish uchun @admin_username.")  # Add your logic

# Start the bot
bot.infinity_polling()