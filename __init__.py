# Общие тексты для команд
HELP_TEXT = (
    "Список доступных команд:\n"
    "/start - Начать взаимодействие с ботом\n"
    "/help - Показать это сообщение\n"
    "/command_chat - Получить список команд бота в группах\n"
    "/command - Получить список команд бота в этом приватном диалоге\n"
    "/group - Получить информацию о доступных группах\n"
    "/admin - Получить информацию об администраторах всех групп\n"
    "/users_list - Получить список всех авторизованных пользователей\n"
    "/add_group <chat_id> - добавить группу\n"
    "/remove_group <chat_id> - удалить группы\n"
)

HELP_USER_TEXT = (
    "Список доступных команд:\n"
    "/start - Начать взаимодействие с ботом\n"
    "/help - Показать это сообщение\n"
)

HELP_GROUP_TEXT = (
    "Что бы получить ID доступных групп:\n"
    "1. Убедитесь что у вас есть телефон с номером к которому привязан чат-бот\n"
    "2. Обратитесь к программисту который может вручную получить список всех ID\n"
    "3. Для этого ему потребуется доступ к вашему телефону и коду авторизации, который прийдет на него\n"
    "P.s. Другого способа нет!\n"
)

#COMMAND_TEXT = (
#    "Список доступных команд для выполнения в группе:\n"
#    "/kick_chat - ответ на сообщении пользователя, которого нужно удалить из группы\n"
#    "/qkick_chat - ответ на сообщении пользователя, которого нужно удалить из всех групп\n"
#    "/invite_chat -  ответ на сообщении пользователя, которого отправить приглашение на вступление в группы\n"
#)

COMMAND_BOT_TEXT = (
    "Список доступных команд для выполнения в приватном диалоге:\n"
    "/kick <user_id> <chat_id> -  удалить пользователя с id = <user_id>, из группы c id = <chat_id>\n"
    "/qkick <user_id> - удалить пользователя с id = <user_id>,, из всех групп\n"
    "/invite <user_id> - отправить пользователю приглашение на вступление в группы\n"
    "/add_group <chat_id> - добавить группу\n"
    "/remove_group <chat_id> - удалить группы\n"
)

bot_token = ''

#admin_api_id = int('')
#admin_api_hash = ''
#admin_phone = ''

filenameUsersIds = 'user_ids.txt'
filenameGroupIds = 'group_ids.txt'

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
