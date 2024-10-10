from loader import dp, bot, FEEDBACK_GROUP_ID
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import asyncio


@dp.message_handler(state=State.waiting_for_start)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.begin_btn:
        await message.answer(texts.task_1)
        await message.answer(texts.find_flower)
        await State.task_1.set()
    else:
        await message.answer(texts.use_kb)


@dp.message_handler(state=State.task_1)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = message.text
    if ans.lower() == 'n':
        with open('images/n.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.succes_1)
        await message.answer(texts.button_continue, reply_markup=kb.continue_kb)
        await State.after_task_1.set()
    else:
        await message.answer(texts.wrong_answer)



@dp.message_handler(state=State.after_task_1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.task_2)
        await message.answer(texts.find_flower)
        await State.task_2.set()
    else:
        await message.answer(texts.use_kb)


@dp.message_handler(state=State.task_2)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = message.text
    if ans.lower() in ['o', 'о', '0']:
        with open('images/o.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.succes_2)
        await message.answer(texts.button_continue, reply_markup=kb.continue_kb)
        await State.after_task_2.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.after_task_2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.task_3)
        await message.answer(texts.find_flower)
        await State.task_3.set()
    else:
        await message.answer(texts.use_kb)


@dp.message_handler(state=State.task_3)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = message.text
    if ans == '1':
        await message.answer(texts.wrong_letter)
        return
    if ans.lower() == 'i':
        with open('images/i.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.succes_3)
        await message.answer(texts.button_continue, reply_markup=kb.continue_kb)
        await State.after_task_3.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.after_task_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.task_4)
        await message.answer(texts.find_flower)
        await State.task_4.set()
    else:
        await message.answer(texts.use_kb)


@dp.message_handler(state=State.task_4)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = message.text
    if ans.lower() == 'n':
        with open('images/n.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.succes_4)
        await message.answer(texts.button_continue, reply_markup=kb.continue_kb)
        await State.after_task_4.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.after_task_4)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.task_5)
        await message.answer(texts.find_flower)
        await State.task_5.set()
    else:
        await message.answer(texts.use_kb)


@dp.message_handler(state=State.task_5)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = message.text
    if ans.lower() in ['o', 'о', '0']:
        with open('images/o.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.succes_2)
        await message.answer(texts.final_task)
        await State.after_task_5.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.after_task_5)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == 'onion':
        with open('images/onion.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.ending)
        await State.feedback.set()
        await asyncio.sleep(2 * 60)
        await message.answer(texts.ask_feedback)
    else:
        await message.answer(texts.wrong_final)


@dp.message_handler(state=State.feedback, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    try:
        await bot.forward_message(FEEDBACK_GROUP_ID, message.chat.id, message.message_id)
    except:
        await bot.send_message(FEEDBACK_GROUP_ID, f'Ошибка пересылки от {message.from_id}')
    await message.answer(texts.thanks)
    with open('images/discont.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.disc)
    await State.end.set()
