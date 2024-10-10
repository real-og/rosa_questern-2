from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts

begin_kb = ReplyKeyboardMarkup([[texts.begin_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

continue_kb = ReplyKeyboardMarkup([[texts.continue_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
