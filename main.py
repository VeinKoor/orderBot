import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(f'Hello {message.from_user.username}')


@dp.message(Command('help'))
async def help(message: types.Message):
    await message.answer('Я простой бот')









async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())