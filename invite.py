from __init__ import *
from base_function import is_private_chat, send_reply_message
from group import load_group_ids
import time

async def invite_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("invite_button_handler")
    query = update.callback_query
    await query.answer()
    print(query)
    data = query.data.split('_')
    print(data)
    if len(data) != 4 or data[0] != 'add':
        print("Invalid callback data")
        return

    user_id = int(data[1])
    chat_id = int(data[2])
    chat_name = data[3]

    print(chat_id)
    try:
        # Устанавливаем время жизни ссылки (например, 1 день) и количество использований (например, 1)
        expire_in_seconds = 86400  # 1 day
        expire_date = int(time.time()) + expire_in_seconds

        # Create the invite link without setting expire_date if you don't want it to expire
        invite_link = await context.bot.create_chat_invite_link(
            chat_id=chat_id,
            expire_date=expire_date,  # Set the expire date to a future timestamp
            member_limit=1  # Set the limit on the number of uses
        )

        # Отправляем ссылку пользователю
        await context.bot.send_message(chat_id=user_id,
                                       text=f'Вот ваша ссылка для присоединения к группе: {invite_link.invite_link}')
        # Отправляем ответ в чат, если нужно
        await query.message.reply_text(f'Ссылка на приглашение в {chat_name} отправлена пользователю в личные сообщения.')
    except Exception as e:
        await query.message.reply_text(f'Ошибка при отправке ссылки на приглашение в группу {chat_name}: {str(e)}')

async def invite_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("invite_command")
    if not is_private_chat(update):
        return

    group_ids = load_group_ids()

    if len(context.args) < 1 or (group_ids is None and len(context.args) != 2):
        await send_reply_message(update, 'Использование: /invite <user_id>')
        return

    try:
        user_id = int(context.args[0])
    except ValueError:
        await send_reply_message(update, 'Пожалуйста, введите корректный ID пользователя.')
        return

    group_names = []
    for group_id in group_ids:
        chat = await context.bot.get_chat(group_id)
        group_names.append(chat.title)

    keyboard = [
        [InlineKeyboardButton(text=f'Добавить в группу {group_name}',
                              callback_data=f'add_{user_id}_{group_id}_{group_name}')]
        for group_name, group_id in zip(group_names, group_ids)
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Выберите чат для добавления пользователя:', reply_markup=reply_markup)
