import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Button, Radio, Row
from aiogram.enums import ContentType
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.media import StaticMedia

from bot.dialogs.start.getters import (
    get_choose_language, 
    get_preview, 
    get_choose_sex, 
    get_upload_photo, 
    get_confirm_photo
)
from bot.dialogs.start.handlers import uploaded_photo, language_choose, sex_choose
from bot.states.start import StartSG
from bot.dialogs.common.handlers import go_next, go_back, go_menu
from python_projects.tg_bot_template.bot.utils.paths import (
    example_photo_path, 
    sexes_photo_path, 
    language_photo_path, 
    hello_photo_path
)

start_dialog = Dialog(
    Window(
        StaticMedia(
            path=Format(language_photo_path),
            type=ContentType.PHOTO
        ),
        Format(text='{choose_language}'),
        Radio(
            Format("🔘 {item[0]}"),  # E.g `🔘 Apple`
            Format("⚪️ {item[0]}"), 
            id='language', 
            item_id_getter=operator.itemgetter(1),
            items='languages',
            on_state_changed=language_choose
        ),
        Button(Format('{next}'), id='b_next', on_click=go_next, when='lang_chosen'),
        state=StartSG.choose_language,
        getter=get_choose_language,
    ),

    Window(
        StaticMedia(
            path=Format(hello_photo_path),
            type=ContentType.PHOTO
        ),
        Format(text='{hello}'),
        Row(
            Button(Format('{back}'), id='b_back', on_click=go_back),
            Button(Format('{next}'), id='b_next', on_click=go_next),
        ),
        state=StartSG.preview,
        getter=get_preview,
    ),

    Window(
        StaticMedia(
            path=Format(sexes_photo_path),
            type=ContentType.PHOTO
        ),
        Format(text='{choose_sex}'),
        Radio(
            Format("🔘 {item[0]}"),  # E.g `🔘 Apple`
            Format("⚪️ {item[0]}"), 
            id='sex', 
            item_id_getter=operator.itemgetter(1),
            items='sexes',
            on_state_changed=sex_choose
        ),
        Row(
            Button(Format('{back}'), id='b_back', on_click=go_back),
            Button(Format('{next}'), id='b_next', on_click=go_next, when='sex_chosen'),
        ),
        state=StartSG.choose_sex,
        getter=get_choose_sex,
    ),

    Window(
        Format(text='{example}'),
        Format(text='{text}'),
        StaticMedia(
            path=Format(example_photo_path),
            type=ContentType.PHOTO
        ),
        MessageInput(
            func=uploaded_photo,
            content_types=ContentType.PHOTO,
        ),
        state=StartSG.upload_photo,
        getter=get_upload_photo,
    ),

    Window(
        Format(text='{user}'), 
        Row(
            Button(Format('{back}'), id='b_back', on_click=go_back),
            Button(Format('{next}'), id='b_next', on_click=go_menu),
        ),
        state=StartSG.confirm_photo,
        getter=get_confirm_photo,
    ),
)