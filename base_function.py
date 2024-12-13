from group import *
from users import *

# Проверка, что команда выполняется в личном чате
def is_private_chat(update: Update) -> bool:
    return update.message.chat.type == 'private'

# отправка сообщения в чат с заменой
async def send_reply_message(update, message):
    await update.message.reply_text(message)

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("start______")
    if not is_private_chat(update):
        return

    print(update)
    print(update.effective_user)
    user_id = update.effective_user.id  # Получаем ID пользователя
    username = update.effective_user.username
    full_name = update.effective_user.first_name + " " + update.effective_user.last_name
    #await update.message.reply_text(f'{username}: ваш ID: {user_id}')

    await send_reply_message(update, f'Ваш ID: {user_id}, Username: @{username}, Полное имя: {full_name}')

    # Читаем существующие user_id из файла
    user_ids = []
    try:
        with open(filenameUsersIds, "r") as file:
            user_ids = [line.strip() for line in file]  # Считываем все user_id в список
    except FileNotFoundError:
        pass  # Если файл не найден, просто продолжаем

    # Форматируем строку для записи
    entry = f"\"{user_id}\"_\"@{username}\"_\"{full_name}\""

    # Проверяем, существует ли запись с таким user_id
    for i, uid in enumerate(user_ids):
        if f"\"{user_id}\"" in uid:
            user_ids[i] = entry  # Заменяем запись
            break
    else:
        user_ids.append(entry)  # Если не нашли, добавляем новую запись

    # Записываем обновленный список user_id обратно в файл
    with open(filenameUsersIds, "w") as file:
        for uid in user_ids:
            file.writelines(uid+"\n")  # Записываем каждую запись на новой строке

    if await check_admin(context, user_id):
        keyboard = [
            [InlineKeyboardButton("Помощь", callback_data='/help')],
            #[InlineKeyboardButton("Команды чата", callback_data='/command_chat')],
            [InlineKeyboardButton("Команды", callback_data='/command')],
            [InlineKeyboardButton("Список групп", callback_data='/group')],
            [InlineKeyboardButton("Список админов", callback_data='/admin')],
            [InlineKeyboardButton("Список пользователей", callback_data='/users_list')],
            [InlineKeyboardButton("Добавить группу", callback_data='/add_group')],
            [InlineKeyboardButton("Удалить группу", callback_data='/remove_group')],
            [InlineKeyboardButton("Получить ID группу", callback_data='/help_group')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Авторизация прошла успешно, вам выдана роль - привилегированный пользователь!',
                                        reply_markup=reply_markup)
    else:
        await send_reply_message(update, f'Авторизация прошла успешно, вам выдана роль - обычный пользователь.')
        #keyboard = [
        #    [InlineKeyboardButton("Помощь", callback_data='/help_user')]
        #]


# Функция для обработки нажатия кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == '/help':
        await query.edit_message_text(text=HELP_TEXT)
    elif query.data == '/help_user':
        await query.edit_message_text(text=HELP_USER_TEXT)
    #elif query.data == '/command_chat':
    #    await query.edit_message_text(text=COMMAND_TEXT)
    elif query.data == '/command':
        await query.edit_message_text(text=COMMAND_BOT_TEXT)
    elif query.data == '/group':
        await query.edit_message_text(text=await get_group_info(context))
    elif query.data == '/admin':
        await query.edit_message_text(text=await get_admin_info(context))
    elif query.data == '/users_list':
        await query.edit_message_text(text=await get_users_list())
    elif query.data == '/add_group':
        await query.edit_message_text(text=await add_group(context))
    elif query.data == '/remove_group':
        await query.edit_message_text(text=await remove_group(context))
    elif query.data == '/help_group':
        await query.edit_message_text(text=HELP_GROUP_TEXT)


# Функции для команд
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_private_chat(update):
        await send_reply_message(update, HELP_TEXT)

#async def command_chat_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    if is_private_chat(update):
#        await send_reply_message(update, COMMAND_TEXT)
async def command_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_private_chat(update):
        await send_reply_message(update, COMMAND_BOT_TEXT)

async def help_group_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_private_chat(update):
        await send_reply_message(update, HELP_GROUP_TEXT)

async def group_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_private_chat(update):
        await send_reply_message(update, get_group_info(context))

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_private_chat(update):
        await send_reply_message(update, await get_admin_info(context))

async def add_group_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_private_chat(update):
        await send_reply_message(update, await add_group(context))

async def remove_group_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_private_chat(update):
        await send_reply_message(update, await remove_group(context))

async def get_users_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_private_chat(update):
        await send_reply_message(update, await get_users_list())

#async def get_group_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    if is_private_chat(update):
#        await send_reply_message(update, await get_group_list(context))
#        #await update.message.reply_text(await get_group_info(context))
