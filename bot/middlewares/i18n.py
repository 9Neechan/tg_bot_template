import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub

from bot.db.requests.users import get_value_from_users

logger = logging.getLogger(__name__)


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)

        locale = user.language_code
        
        session = data.get('session')
        if session:
            res = await get_value_from_users(session, user.id, 'language')
            if res != None:
                locale = res

        hub: TranslatorHub = data.get('_translator_hub')
        data['i18n'] = hub.get_translator_by_locale(locale=locale)

        return await handler(event, data)