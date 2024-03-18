import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from keys import main_keyboard, free_keyboard, paid_keyboard
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from tgmiddlewares import LoggingMiddleware
import os
from dotenv import load_dotenv


# Don't forget to fill in your information
load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
redis = Redis(host='')
storage = RedisStorage(redis=redis)
dp = Dispatcher()
ADMIN_ID = ""  # Telegram ID of your shop manager that will receive incoming orders
dp.message.middleware(LoggingMiddleware())


class SupportState(StatesGroup):
    WAITING_FOR_MESSAGE = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Welcome to the shop! \n Use buttons for navigation",
                         reply_markup=main_keyboard)


@dp.callback_query(F.data == 'free_request')
async def free(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "<b>You can test our products before buying them.",
                           reply_markup=free_keyboard)


@dp.callback_query(F.data == 'buy_request')
async def paid(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Make your choice",
                           reply_markup=paid_keyboard)


@dp.callback_query(F.data.in_(['good1_free', 'good2_free', 'good3_free', 'good4_free']))
async def free_selected(message: types.Message):
    message_to_admin = (f"Free test request:\n"
                        f"Name: {message.from_user.full_name}\n"
                        f"Telegram: @{message.from_user.username if message.from_user.username else 'no'}\n"
                        f"Product: {F.data}")

    await bot.send_message(ADMIN_ID, message_to_admin)


@dp.message(F.text.in_(["good1_paid", "good2_paid", "good3_paid", "good4_paid"]))
async def paid_selected(message: types.Message):
    message_to_admin = (f" New order!:\n"
                        f"Name: {message.from_user.full_name}\n"
                        f"Telegram: @{message.from_user.username if message.from_user.username else 'no'}\n"
                        f"Product: {message.text}")

    await bot.send_message(ADMIN_ID, message_to_admin)


@dp.callback_query(F.data == 'support_request')
async def contact_support(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id,
                           "Send your message to our support team")
    await state.set_state(SupportState.WAITING_FOR_MESSAGE)


@dp.message(StateFilter(SupportState.WAITING_FOR_MESSAGE))
async def process_message(message: types.Message, state: FSMContext):
    await bot.send_message(ADMIN_ID, f"Message from {message.from_user.id}: {message.text}")
    await message.answer("Your message was delivered to our support team.")
    await state.clear()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
