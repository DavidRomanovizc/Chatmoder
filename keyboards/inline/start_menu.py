from aiogram import types


# Создаем клавиатуру
start_markup = types.InlineKeyboardMarkup(row_width=3)

# Кнопки с CallBack Data
text_and_data = (
    ('Список комманд', 'help'),
)

# Добавляем кнопки с Callback Data
row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
start_markup.row(*row_btns)

# Добавляем обычные кнопки
start_markup.add(
    types.InlineKeyboardButton('Мой github', url='https://github.com/DavidRomanovizc'),
    types.InlineKeyboardButton('Чат', url='https://t.me/joinchat/GhZKbBi0KvGAlrMZ'),
)


source_markup = types.InlineKeyboardMarkup()
source_markup.insert(
    types.InlineKeyboardButton('Бот', url='https://github.com/DavidRomanovizc/Chatmoder'),
)
