from typing import TYPE_CHECKING

from aiogram.types import User
from aiogram_dialog import DialogManager

from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner


async def get_choose_language(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    return {
        "choose_language": i18n.choose.language(),
        'languages': [('Русский 🇷🇺', '1'), ('English 🇦🇺', '2')],
        'next': i18n.next(),
        'back': i18n.back(),
        'done': i18n.done(),
        'lang_chosen': dialog_manager.dialog_data.get('lang_chosen')
    }


async def get_preview(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    return {
        "hello": i18n.hello.user(username=event_from_user.first_name),
        'next': i18n.next(),
        'back': i18n.back()
    }


async def get_choose_sex(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    return {
        'choose_sex': i18n.choose.sex(),
        'sexes': [(i18n.choose.sex.female(), '1'), (i18n.choose.sex.male(), '2')],
        'next': i18n.next(),
        'back': i18n.back(),
        'done': i18n.done(), 
        'sex_chosen': dialog_manager.dialog_data.get('sex_chosen')
    }


async def get_upload_photo(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    return {
        "text": i18n.upload.photo(),
        'example': i18n.upload.photo.example(),
        'user': i18n.upload.photo.user(),
        'next': i18n.next(),
        'back': i18n.back(),
    }


async def get_confirm_photo(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    '''user_id = event_from_user.id
    file_name = os.path.join(users_photo_path, f'{user_id}.jpg')

    image = MediaAttachment(ContentType.PHOTO, path=file_name)'''

    return {
        "text": i18n.upload.photo(),
        'example': i18n.upload.photo.example(),
        'user': i18n.upload.photo.user(),
        'next': i18n.next(),
        'back': i18n.back(),
        'done': i18n.done(),
        #'user_photo': image,
        #'user_photo1': file_name
    }