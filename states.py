from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    waiting_for_start = State()
    task_1 = State()
    task_2 = State()
    task_3 = State()
    task_4 = State()
    task_5 = State()

    after_task_1 = State()
    after_task_2 = State()
    after_task_3 = State()
    after_task_4 = State()
    after_task_5 = State()
    after_onion = State()

    feedback = State()
    end = State()