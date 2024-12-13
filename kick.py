from __init__ import *
from base_function import is_private_chat, check_admin, send_reply_message
from group import load_group_ids

async def kick_user_from_chat(context, update, user_id, chat_id):
    try:
        await context.bot.ban_chat_member(chat_id=chat_id, user_id=user_id)

        await context.bot.unban_chat_member(chat_id=chat_id, user_id=user_id)

        chat = await context.bot.get_chat(chat_id)
        group_name = chat.title
        await send_reply_message(update, f'Пользователь: {user_id}, удален из группы {group_name}.')
    except Exception as e:
        await send_reply_message(update, f'Ошибка при удалении пользователя: {user_id}, из группы {chat_id}: {str(e)}')

async def remove_user_from_file(user_id):
    try:
        with open(filenameUsersIds, 'r') as file:
            lines = file.readlines()

        with open(filenameUsersIds, 'w') as file:
            for line in lines:
                if not line.startswith(f'"{user_id}"'):
                    file.write(line)
    except Exception as e:
        print(f'Ошибка при удалении пользователя из файла: {str(e)}')

async def process_kick_command(update, context, group_ids=None, remove_from_file=False):
    if not is_private_chat(update):
        return

    if len(context.args) < 1 or (group_ids is None and len(context.args) != 2):
        await send_reply_message(update, 'Использование: /qkick <user_id> [<chat_id>]')
        return

    try:
        user_id = int(context.args[0])
    except ValueError:
        await send_reply_message(update, 'Пожалуйста, введите корректный ID пользователя.')
        return

    if await check_admin(context, user_id):
        await send_reply_message(update, 'Вы не можете удалить администратора группы, у вас тут нет таких прав!')
        return

    if group_ids:
        for group_id in group_ids:
            await kick_user_from_chat(context, update, user_id, group_id)
    else:
        try:
            chat_id = int(context.args[1])
            await kick_user_from_chat(context, update, user_id, chat_id)
        except ValueError:
            await send_reply_message(update, 'Пожалуйста, введите корректный ID группы.')

    # Удаляем пользователя из файла только при qkick_command
    if remove_from_file:
        await remove_user_from_file(user_id)


async def qkick_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    group_ids = load_group_ids()
    await process_kick_command(update, context, group_ids, remove_from_file=True)

async def kick_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await process_kick_command(update, context)
