from base_function import *
from kick import qkick_command, kick_command
from invite import invite_command, invite_button_handler

# Основная функция для запуска бота
def main() -> None:
    print("start")
    application = Application.builder().token(bot_token).build()
    application.add_handler(CommandHandler("start", start), group=1)
    application.add_handler(CallbackQueryHandler(button), group=1)

    application.add_handler(CommandHandler("help", help_command), group=2)
    #application.add_handler(CommandHandler("command_chat", command_chat_command), group=2)
    application.add_handler(CommandHandler("command", command_command), group=2)
    application.add_handler(CommandHandler("group", group_command), group=2)
    application.add_handler(CommandHandler("admin", admin_command), group=2)
    application.add_handler(CommandHandler("users_list", get_users_list_command), group=2)

    application.add_handler(CommandHandler("qkick", qkick_command), group=2)
    application.add_handler(CommandHandler("kick", kick_command), group=2)
    application.add_handler(CommandHandler("invite", invite_command), group=5)
    application.add_handler(CallbackQueryHandler(invite_button_handler), group=5)

    application.add_handler(CommandHandler("add_group", add_group_command), group=2)
    application.add_handler(CommandHandler("remove_group", remove_group_command), group=2)

    #application.add_handler(CommandHandler("invite_chat", invite_chat_command), group=3)
    #application.add_handler(CallbackQueryHandler(invite_chat_button_handler), group=3)
    #application.add_handler(CommandHandler("kick_chat", kick_chat_command), group=2)
    #application.add_handler(CommandHandler("qkick_chat", qkick_chat_command), group=2)

    application.run_polling()

if __name__ == '__main__':
    main()
