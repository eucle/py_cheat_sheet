from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def send_echo(message: Message):
    await message.answer(
        'Эту команду я не понимаю. Пожалуйста, повтори ввод или'
        ' воспользуйся помощью - /help.'
    )
