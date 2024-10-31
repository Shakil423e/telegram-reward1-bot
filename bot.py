import telebot

# আপনার BotFather থেকে প্রাপ্ত টোকেনটি এখানে যুক্ত করুন
TOKEN = '7765052828:AAHvuTQI1eq6rMmNmWqvxf5MOjML9WIjlYw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Reward Bot!")

@bot.message_handler(commands=['balance'])
def balance(message):
    bot.send_message(message.chat.id, "Your balance is: 0 points")

@bot.message_handler(commands=['withdraw'])
def withdraw(message):
    bot.send_message(message.chat.id, "Withdrawal request received.")

bot.polling()