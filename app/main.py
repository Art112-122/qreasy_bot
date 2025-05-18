import asyncio
import logging
import sys
import pyqrcode
import validators
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from state import State_qrcode
from aiogram.types.bot_command import BotCommand
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

load_dotenv()

dp = Dispatcher()

BOT_START_COMMAND = BotCommand(command="start", description="Стартове меню")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Створити QR-код📲")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)


@dp.message(F.text == "Створити QR-код📲")
async def qr_code_start(ms: Message, state: FSMContext) -> None:
    await state.set_state(State_qrcode.qr)
    await ms.answer(html.bold('Введіть посилання'))


@dp.message(State_qrcode.qr)
async def qr_code(ms: Message, state: FSMContext) -> None:
    try:
        link = ms.text
        if "!exit" in link:
            await ms.answer(f"{html.italic('Генерацію призупинено')}")
            await state.clear()
        elif validators.url(link):
            filename = "qr_code_for_bot.png"
            qr = pyqrcode.create(link)
            qr.png(filename, scale=8)
            qr_img = FSInputFile(filename)
            msg = f"Ваш {html.bold('QR-код')} за {html.link('посиланням', link)}"
            await ms.answer_photo(qr_img, caption=msg)
            os.remove(filename)
            await state.clear()
        else:
            await ms.answer(
                f"{html.bold('Посилання недійсне! Введіть правильне посилання. (Щоб вийти — !exit)')}")
    except TypeError:
        await ms.answer("Критична помилка!")


@dp.message(CommandStart)
async def start(message: Message) -> None:
    await message.answer(
        f'Привіт, {message.from_user.first_name}! Я — бот, що допоможе тобі швидко та зручно створити {html.bold("QR-код")}\n\n'
        f'{html.bold("Навігація")}\n'
        f'/start - {html.italic("Меню")}\n', reply_markup=keyboard)


async def main() -> None:
    bot = Bot(token=os.environ.get("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands([BOT_START_COMMAND])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
