import logging
import os

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram.types import Message
from aiogram import types

from bot.db.requests.users import update_user_language, update_user_sex
from bot.utils import data_dicts
from python_projects.tg_bot_template.bot.utils.paths import users_photo_path


logger = logging.getLogger(__name__)


async def language_choose(c: types.CallbackQuery, 
                          button: Button, 
                          manager: DialogManager, 
                          id: id):
    manager.dialog_data.update(lang_chosen=True)

    lang = data_dicts.languages[id]
    session = manager.middleware_data['session']
    await update_user_language(session, c.from_user.id, lang)


async def sex_choose(c: types.CallbackQuery, 
                     button: Button, 
                     manager: DialogManager, 
                     id: id):
    manager.dialog_data.update(sex_chosen=True)

    sex = data_dicts.sexes[id]
    session = manager.middleware_data['session']
    await update_user_sex(session, c.from_user.id, sex)


async def uploaded_photo(message: Message, 
                         widget: MessageInput, 
                         dialog_manager: DialogManager):
    bot = message.bot
    photo = message.photo[-1]
    user_id = str(message.from_user.id)
    file_name = os.path.join(users_photo_path, f'{user_id}.jpg')
    
    await bot.download(photo, destination=file_name)
    await message.answer_photo(photo.file_id)
    await dialog_manager.next()