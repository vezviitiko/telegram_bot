from __init__ import *
from group import load_group_ids

# функция для получения информации об администраторах групп
async def get_admin_info(context: ContextTypes.DEFAULT_TYPE) -> str:
    group_ids = load_group_ids()
    unique_users = ["Список администраторов по группам:"]
    for group_id in group_ids:
        try:
            chat = await context.bot.get_chat(group_id)
            group_name = chat.title
            unique_users.append(f"=======================")
            unique_users.append(f"Группа: {group_name}")
            count = 1
            administrators = await context.bot.get_chat_administrators(group_id)
            for admin in administrators:
                user = admin.user
                user_id = user.id
                username = user.username
                fullname = f"{user.first_name} {user.last_name or ''}".strip()
                unique_users.append(f"{count}. ID: {user_id}, Имя пользователя:{username}, Полное имя:{fullname}")
                count += 1
        except Exception as e:
            unique_users.append(f'Не удалось получить информацию о группе с ID {group_id}: {e}')
    return "\n".join(unique_users)


# функция для получения информации о зарегистрированных пользователей
async def get_users_list() -> str:
    unique_users = ["Список всех зарегистрированных пользователей:"]
    try:
        with open(filenameUsersIds, "r") as file:
            user_ids = [line.strip() for line in file]  # Считываем все user_id в список

            # Форматируем каждую запись для вывода
            count = 1
            for user_entry in user_ids:
                # Предполагаем, что user_entry имеет формат: "user_id"_"@username"_"full_name"
                parts = user_entry.split('_')
                if len(parts) == 3:
                    user_id = parts[0].strip('"')
                    username = parts[1].strip('"')[1:]  # Убираем '@'
                    full_name = parts[2].strip('"')
                    unique_users.append(f'{count}. ID: {user_id}, Имя пользователя: @{username}, Полное имя: {full_name}')
                    count += 1

    except FileNotFoundError:
        unique_users.append(f'Не удалось получить информацию о пользователях из файла {filenameUsersIds}')

    # Возвращаем результат как строку
    return "\n".join(unique_users)


# функция проверки пользователя, админ ли он любой группы
async def check_admin(context: ContextTypes.DEFAULT_TYPE, user_id) -> bool:
    group_ids = load_group_ids()
    for group_id in group_ids:
        try:
            administrators = await context.bot.get_chat_administrators(group_id)
            for admin in administrators:
                if user_id == admin.user.id:
                    return True
        except Exception as e:
            print(f"Ошибка при получении администраторов для группы {group_id}: {e}")
    return False
