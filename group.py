from __init__ import *

# Общая функция для получения информации о группах
async def get_group_info(context: ContextTypes.DEFAULT_TYPE) -> str:
    group_ids = load_group_ids()
    group_info = ["Список групп:"]
    count = 1
    for group_id in group_ids:
        try:
            chat = await context.bot.get_chat(group_id)
            group_name = chat.title
            group_id = chat.id
            member_count = await context.bot.get_chat_member_count(group_id)
            group_info.append(f'{count}. ID:{group_id}, Группа: {group_name}, Кол-во пользователей: {member_count}')
            count += 1
        except Exception as e:
            group_info.append(f'Не удалось получить информацию о группе с ID {group_id}: {e} - Пожалуйста, удалите группу, чтобы избежать возможных ошибок в будущем.')
    return "\n".join(group_info)

def load_group_ids() -> list:
    try:
        with open(filenameGroupIds, "r") as file:
            group_ids = [line.strip() for line in file]  # Считываем все group_id в список
            print("Загруженные group_ids:", group_ids)
            return group_ids
    except FileNotFoundError:
        print(f"Файл {filenameGroupIds} не найден. Глобальная переменная group_ids будет пустой.")
        return []

def save_group_ids(group_ids: list) -> None:
    """Сохранить ID групп в файл."""
    with open(filenameGroupIds, 'w+') as file:
        for group_id in group_ids:
            file.write(f"{group_id}\n")

async def add_group(context: ContextTypes.DEFAULT_TYPE) -> str:
    group_ids = load_group_ids()

    if context.args:
        group_id = context.args[0]
        print(group_id)
        if group_id not in group_ids:
            print(group_ids)
            group_ids.append(group_id)
            print(group_ids)
            save_group_ids(group_ids)
            print('tyt')
            return f'Группа с ID {group_id} добавлена.'
        else:
            return f'Группа с ID {group_id} уже существует.'
    else:
        return 'Используйте: /add_group <chat_id>'


async def remove_group(context: ContextTypes.DEFAULT_TYPE) -> str:
    group_ids = load_group_ids()

    if context.args:
        group_id = context.args[0]
        if group_id in group_ids:
            group_ids.remove(group_id)
            save_group_ids(group_ids)
            return f'Группа с ID {group_id} удалена.'
        else:
            return f'Группа с ID {group_id} не найдена.'
    else:
        return 'Используйте: /remove_group <chat_id>'

'''
import string
import random
def generate_random_string(length=20):
    letters = string.ascii_letters  # Включает как строчные, так и заглавные буквы
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

#обновить список доступных групп вручную
async def get_group_list() -> None:
    # Создаем клиент
    st = generate_random_string()
    print(st)
    client = TelegramClient(st, admin_api_id, admin_api_hash)
    await client.start(phone=admin_phone)

    # Если требуется ввести код, запрашиваем его у пользователя
    if not await client.is_user_authorized():
        code = input("Please enter the code you received: ")
        await client.sign_in(phone=admin_phone, code=code)

    async with client:
        group_ids = []
        async for dialog in client.iter_dialogs():
            # Проверяем, является ли чат группой
            if dialog.is_group:
                print(f"Название группы: {dialog.name}, ID: {dialog.id}")
                group_ids.append(dialog.id)

        # Записываем обновленный список group_ids обратно в файл
        with open(filenameGroupIds, "w") as file:
            for gid in group_ids:
                file.write(f"{gid}\n")  # Записываем каждую запись на новой строке
'''
