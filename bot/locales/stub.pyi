from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    choose: Choose
    upload: Upload
    generation: Generation
    button: Button
    preview: Preview
    result: Result
    waiting: Waiting

    @staticmethod
    def next() -> Literal["""Далее ▶️"""]: ...

    @staticmethod
    def back() -> Literal["""◀️ Назад"""]: ...

    @staticmethod
    def done() -> Literal["""Готово ✅"""]: ...

    @staticmethod
    def generate() -> Literal["""Примерить👔"""]: ...

    @staticmethod
    def menu() -> Literal["""Меню"""]: ...

    @staticmethod
    def forbidden() -> Literal["""Недостаточно прав 🚫
Вернитесь к основному функционалу бота прописав команду /start"""]: ...


class Hello:
    @staticmethod
    def user(*, username) -> Literal["""Привет, { $username }! 👋
Я - бот, который поможет подобрать и примерить одежду. 👚👕
Давай начнем с заполнения данных, которые помогут сделать мою работу качественней."""]: ...


class Choose:
    sex: ChooseSex

    @staticmethod
    def language() -> Literal["""Выберите язык:"""]: ...

    @staticmethod
    def cathegory() -> Literal["""Выберите категорию:"""]: ...


class ChooseSex:
    @staticmethod
    def __call__() -> Literal["""Выберите пол:"""]: ...

    @staticmethod
    def male() -> Literal["""Мужчина 🚹"""]: ...

    @staticmethod
    def female() -> Literal["""Женщина 🚺"""]: ...


class Upload:
    photo: UploadPhoto


class UploadPhoto:
    @staticmethod
    def __call__() -> Literal["""Загрузите вашу фотографию. 🖼
Для точного подбора стиля, загрузите фото с хорошим освещением, естественной позой, где хорошо видны лицо и верхняя часть тела. 
Рекомендуем загрузить фото в одежде, похожей на ту, что вы хотите примерить. Избегайте фото с поднятыми руками.
Соблюдение рекомендаций улучшит качество генерации одежды."""]: ...

    @staticmethod
    def example() -> Literal["""Пример фото:"""]: ...

    @staticmethod
    def user() -> Literal["""Ваше фото:
Если хотите поменять фото - нажмите &#34;Назад&#34;."""]: ...

    @staticmethod
    def fitting() -> Literal["""Рекомендуем загрузить фото одежды на однотонном фоне. (Отправьте боту фото 📤)
После отправки результат будет готов в течение 30 секунд."""]: ...


class Generation:
    @staticmethod
    def menu() -> Literal["""Выберите способ генерации ✨"""]: ...


class Button:
    menu: ButtonMenu
    generation: ButtonGeneration


class ButtonMenu:
    change: ButtonMenuChange
    find: ButtonMenuFind


class ButtonMenuChange:
    @staticmethod
    def language() -> Literal["""Изменить язык 🌎"""]: ...

    @staticmethod
    def sex() -> Literal["""Изменить пол 🚹🚺"""]: ...

    @staticmethod
    def photo() -> Literal["""Изменить фото 🖼"""]: ...


class ButtonMenuFind:
    @staticmethod
    def look() -> Literal["""Подобрать образ 🔎"""]: ...


class ButtonGeneration:
    menu: ButtonGenerationMenu


class ButtonGenerationMenu:
    @staticmethod
    def catalog() -> Literal["""Образ из каталога 📕"""]: ...

    @staticmethod
    def fitting() -> Literal["""Примерить одежду с фото 📸"""]: ...


class Preview:
    @staticmethod
    def catalog() -> Literal["""В данном режиме вам будет предоставлен каталог вещей, которые вы сможете примерить на себя.
К каждой вещи прикреплена ссылка, по которой можно ее приобрести.
Генерация занимает до 30 секунд."""]: ...

    @staticmethod
    def fitting() -> Literal["""С помощью данного режима вы сможете примерить на себя одежду с фото, которое загрузите!"""]: ...


class Result:
    no: ResultNo

    @staticmethod
    def catalog() -> Literal["""Прекрасный выбор! Вот ваш лук ✨"""]: ...

    @staticmethod
    def fitting() -> Literal["""Вот ваш лук ✨"""]: ...


class ResultNo:
    validated: ResultNoValidated


class ResultNoValidated:
    @staticmethod
    def __call__() -> Literal["""Ваше фото вещи для примерки не подходит. Загрузите новое 📤."""]: ...

    @staticmethod
    def catalog() -> Literal["""Ваше фото пользователя не подходит. Загрузите новое 📤."""]: ...


class Waiting:
    @staticmethod
    def result() -> Literal["""Ждем окончание генерации лука. Это займет до 1 минуты."""]: ...

