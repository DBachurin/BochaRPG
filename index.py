import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo



# PROXY_URL = "http://proxy.server:3128"
# bot = Bot(token=BOT_TOKEN, parse_mode="HTML",
#           proxy=PROXY_URL
#           )

bot = Bot(token=os.environ["BOT_TOKEN"])


dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open suka', web_app=WebAppInfo(url='https://rawcdn.githack.com/DBachurin/BochaRPG/c73749d22bd7176988ebbde060626ea9bbb1d288/game_tg.html')))

    await message.answer('Hi lolo', reply_markup=markup)


##executor.start_polling(dp, skip_updates=True)
executor.start_polling(dp)


