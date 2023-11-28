from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from loguru import logger

from keyboards.contents_kb import create_contents_keyboard
from db.db import user_dict_template, users_db
from filters.filters import IsDigitCallbackData
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon import LEXICON, LEXICON_CONTENTS
from services.text_handling import cheat_sheet


router = Router()


@router.message(CommandStart())
async def handle_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    logger.info(f"User {message.from_user.id} sent /start.")


@router.message(Command(commands='help'))
async def handle_help_command(message: Message):
    await message.answer(LEXICON[message.text])
    logger.info(f"User {message.from_user.id} sent /help.")


@router.message(Command(commands='contents'))
async def handle_contents_command(message: Message):
    await message.answer(
        text=LEXICON[message.text],
        reply_markup=create_contents_keyboard(
            LEXICON_CONTENTS,
        )
    )
    logger.info(f"User {message.from_user.id} sent /contents.")


@router.callback_query(F.data == 'forward')
async def handle_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] < len(cheat_sheet):
        users_db[callback.from_user.id]['page'] += 1
        text = cheat_sheet[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                'forward'
            )
        )
    await callback.answer(
        f'Страница {users_db[callback.from_user.id]["page"]} '
        f'из {len(cheat_sheet)}'
    )
    logger.info(
        f'User {callback.from_user.id} proceed forward to page '
        f'{users_db[callback.from_user.id]["page"]}.'
    )


@router.callback_query(F.data == 'backward')
async def handle_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        text = cheat_sheet[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                'forward'
            )
        )
    await callback.answer(
        f'Страница {users_db[callback.from_user.id]["page"]} '
        f'из {len(cheat_sheet)}'
    )
    logger.info(f'User {callback.from_user.id} proceed backward to page '
                f'{users_db[callback.from_user.id]["page"]}.')


@router.callback_query(IsDigitCallbackData())
async def handle_section_press(callback: CallbackQuery):
    text = cheat_sheet[int(callback.data)]
    users_db[callback.from_user.id]['page'] = int(callback.data)
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            'forward'
        )
    )
    await callback.answer(
        f'Страница {users_db[callback.from_user.id]["page"]} '
        f'из {len(cheat_sheet)}'
    )
    logger.info(
        f'User {callback.from_user.id} proceed to page '
        f'{users_db[callback.from_user.id]["page"]}.'
    )
