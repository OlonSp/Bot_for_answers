from os import name
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import random

BOT_TOKEN = 'Bot token here'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def Process_Start_Command(message: Message):
    await message.answer("Привет, введи номер вопроса, чтобы получить на него ответ, или 'Вопросы', чтобы получить список вопросов")

async def Process_sv(message: Message):
    with open("Список вопросов.txt", encoding = 'utf-8', mode = 'r') as f:
        s = ""
        for i in range(25):
            s += f.readline()
        await message.answer(s)
        s = ""
        for i in range(30):
            s += f.readline()
        await message.answer(s)

async def Process_long(message: Message):
    file = message.text + ".txt"
    with open(file, encoding = 'utf-8', mode = 'r') as f:
        s = ""
        for i in f:
            if len(s + i) < 4096:
                s += i
            else:
                await message.answer(s)
                s = i
    await message.answer(s)

async def Process_num(message: Message):
    file = message.text + ".txt"
    with open(file, encoding = 'utf-8', mode = 'r') as f:
        s = f.read()
    await message.answer(s)

async def Process_other_message(message: Message):
    await message.answer("Я не понимаю, что ты пишешь. Напиши да или нет")

dp.message.register(Process_Start_Command, Command(commands='start'))
dp.message.register(Process_sv, lambda x: x.text.lower() == "вопросы")
dp.message.register(Process_long, lambda x: int(x.text) == 26 or int(x.text) == 40 or int(x.text) == 51 or int(x.text) == 55)
dp.message.register(Process_num, lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 55)
dp.message.register(Process_other_message)

if __name__ == '__main__':
    dp.run_polling(bot)
