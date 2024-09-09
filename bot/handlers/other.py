import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import DialogManager, StartMode
from fluentogram import TranslatorRunner

#from bot.config_data.config import db
from bot.states.start import StartSG

other_router = Router()


class Actions(StatesGroup):
    base_state = State()


# Этот хэндлер будет срабатывать на любые сообщения и
# отправлять пользователю их копию
'''@other_router.message()
async def send_echo(message: Message, i18n: TranslatorRunner):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=i18n.no.copy())'''

