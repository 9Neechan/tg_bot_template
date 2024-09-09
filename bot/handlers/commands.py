from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner

from sqlalchemy.ext.asyncio import AsyncSession

from bot.states.start import StartSG


commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
    msg: Message,
    state: FSMContext, 
    i18n: TranslatorRunner,
    dialog_manager: DialogManager,
    session: AsyncSession
) -> None:

    await dialog_manager.start(state=StartSG.choose_language, 
                               mode=StartMode.RESET_STACK)