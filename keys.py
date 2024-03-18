from aiogram import types

main_kb = [
    [types.InlineKeyboardButton(text="Button1", callback_data='free_request')],
    [types.InlineKeyboardButton(text="Button2", callback_data='buy_request')],
    [types.InlineKeyboardButton(text="Button3", callback_data='support_request')]
]
main_keyboard = types.InlineKeyboardMarkup(inline_keyboard=main_kb)


free_chosen = [
    [types.InlineKeyboardButton(text="Button4", callback_data='good1_free')],
    [types.InlineKeyboardButton(text="Button5", callback_data='good2_free')],
    [types.InlineKeyboardButton(text="Button6", callback_data='good3_free')],
    [types.InlineKeyboardButton(text="Button7", callback_data='good4_free')]
]
free_keyboard = types.InlineKeyboardMarkup(inline_keyboard=free_chosen)

paid_chosen = [
    [types.InlineKeyboardButton(text="Button8", callback_data='good1_paid')],
    [types.InlineKeyboardButton(text="Button9", callback_data='good2_paid')],
    [types.InlineKeyboardButton(text="Button10", callback_data='good3_paid')],
    [types.InlineKeyboardButton(text="Button11", callback_data='good4_paid')]
]
paid_keyboard = types.InlineKeyboardMarkup(inline_keyboard=paid_chosen)