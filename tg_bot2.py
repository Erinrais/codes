import telebot
import random
from random import choice
from telebot import types


hello_messages = [
    "Привет! Как я могу помочь?",
    "Здравствуйте! Чем могу быть полезен?",
    "Приветствую! Надеюсь, у вас хороший день.",
    "Hello! How can I assist you?",
    "Hey there! How can I help?",
    "Hi! What can I do for you?",
    "Привет! Чем я могу помочь?",
    "Здорово видеть вас! В чем возникла потребность?",
    "Приветствую! Что вас интересует?",
    "Hello! Is there something specific you need?",
    "Hi! How can I assist you today?",
    "Приветствую вас! Чем могу помочь?",
    "Hey! What can I help you with?",
    "Привет! Что вас привело сюда?",
    "Здравствуйте! Чем могу помочь?",
    "Доброго времени суток! Как я могу помочь?",
    "Приветствую! Готов помочь вам!",
    "Hello! How can I be of service?",
    "Hi there! What brings you here?",
    "Привет! Позвольте представиться вашему вниманию.",
    "Здравствуйте! Что вы хотели бы узнать?",
    "Приветствую вас! Чем могу быть полезен?",
    "Hello! What can I do for you today?",
    "Hi! Need any assistance?",
    "Привет! Рад вас видеть здесь!",
    "Здравствуйте! Чем я могу помочь вам?",
    "Приветствую! Как я могу облегчить ваш день?",
    "Hello! How can I assist you right now?",
    "Hi! How can I make your day better?",
    "Привет! Что бы вы ни искали, я здесь для вас.",
    "Здравствуйте! Чем могу помочь вам?",
    "Приветствую! Ваше обслуживание - моя цель!",
    "Hello! Need help with something?",
    "Hi there! What can I do for you today?",
    "Привет! Что бы вы ни нуждались, я здесь для вас.",
    "Здравствуйте! Как я могу сделать ваш день лучше?",
    "Приветствую! В чем я могу помочь?",
    "Hello! How may I assist you?",
    "Hi! Is there anything I can help you with?",
    "Привет! Чем я могу вам помочь сегодня?",
    "Здравствуйте! Чем я могу помочь вам сегодня?",
    "Приветствую! Готов помочь в любой ситуации.",
    "Hello! Need any assistance today?",
    "Hi! How can I make your day better?",
    "Привет! Какие у вас планы на сегодня?",
    "Здравствуйте! Чем я могу сделать ваш день лучше?",
    "Приветствую! Вам нужна помощь?",
    "Hello! Is there something you need help with?",
    "Hi there! How can I assist you today?",
    "Привет! Чем я могу помочь вам сегодня?",
    "Здравствуйте! Чем я могу быть полезен вам?",
    "Приветствую! Готов помочь вам сегодня.",
    "Hello! How can I assist you right now?",
    "Hi! What can I help you with?",
    "Привет! Что вас привело? Как я могу помочь?",
    "Здравствуйте! В чем я могу помочь?",
    "Приветствую! Чем я могу вам помочь?",
    "Hello! How can I assist you today?",
    "Hi! Is there something specific you need help with?",
    "Привет! Как я могу облегчить ваш день?",
    "Здравствуйте! Чем могу быть полезен?",
    "Приветствую! Чем я могу помочь вам?",
    "Hello! Is there something I can help you with?",
    "Hi there! How can I assist you today?",
    "Привет! Чем я могу вам помочь?",
    "Здравствуйте! Как я могу сделать ваш день лучше?",
    "Приветствую! Чем я могу быть полезен?",
    "Hello! How can I assist you right now?",
    "Hi! Need help with something?",
    "Привет! Чем могу помочь?",
    "Здравствуйте! Как я могу быть полезен вам сегодня?",
    "Приветствую! Чем я могу помочь вам сегодня?",
    "Hello! How may I assist you?",
    "Hi! Is there anything I can help you with?",
    "Привет! Какие у вас планы на сегодня?",
    "Здравствуйте! Чем я могу сделать ваш день лучше?",
    "Приветствую! Вам нужна помощь?",
    "Hello! Is there something you need help with?",
    "Hi there! How can I assist you today?",
    "Привет! Чем я могу помочь вам сегодня?",
    "Здравствуйте! Чем я могу быть полезен вам?",
    "Приветствую! Готов помочь вам сегодня.",
    "Hello! How can I assist you right now?",
    "Hi! What can I help you with?",
    "Привет! Что вас привело? Как я могу помочь?",
    "Здравствуйте! В чем я могу помочь"
]


bot = telebot.TeleBot('Токен')


@bot.message_handler(commands=['start'])
def start(message):
    for i in range(1):
        bot.send_message(message.chat.id, random.choice(hello_messages))


@bot.message_handler(content_types=['text', 'photo'])
def get_message(message):
    bot.send_message(message.chat.id, 'Я Вас не понимаю. Я могу только привествовать вас /start')


bot.infinity_polling()
