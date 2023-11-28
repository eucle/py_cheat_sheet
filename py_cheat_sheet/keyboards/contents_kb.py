from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_contents_keyboard(arg: tuple) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for section in arg:
        kb_builder.row(InlineKeyboardButton(
            text=f'{section[0]}',
            callback_data=str(section[1]),
        ))
    return kb_builder.as_markup()
