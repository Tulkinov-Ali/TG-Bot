from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# start komandasiga javob beruvchi funksiya
def start(update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=f"👋🏻 Assalomu alaykum {user.first_name}\n Bu bot orqali dostingizni topishingiz mumkin.\n Dostingizni usernameni yuboring:")


# salom habariga javob beruvchi funksiya
def reply_to_salom(update, context):
    # Foydalanuvchi habar matnini olish
    user_message = update.message.text

    # Assuming 'update' is an object passed to the function
    if "@nrx_xusan" in user_message:
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text="👨‍💼️ Turi: foydalanuvchi\n 🆔 Foydalanuvchi ID: 5613062658 \n 🔗 Havola: https://t.me/nrx_xusan \n👤 Ism: XusanDev07 \n Guruhlar [2]:\n @djangouzb Uz Django Developers Community \n @itpark_livechat IT Park Livechat"
        )

    if "@Joha_JST" in user_message:
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text="👨‍💼️ Turi: foydalanuvchi\n 🆔 Foydalanuvchi ID: 1475094695 \n 🔗 Havola: https://t.me/Joha_JST \n👤 Ism: Javohir Guruhlar [3]:\n @python_uz Python 🐍 \n@botlarhaqida Botlar Haqida \n @python_uz_offtopic Python🇺🇿 offtopic group"
        )

    if "@Avazbek_alone" in user_message:
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text="👨‍💼️ Turi: foydalanuvchi\n 🆔 Foydalanuvchi ID: 919323624 \n 🔗 Havola: https://t.me/Avazbek_alone \n 👤 Ism: Avazbek \n Guruhlar [2]: \n @haqiqatchiblogeruz BLOGER va Qonun 🇺🇿 \n @appleuz_chat 🍏Apple.Uzb 🛍Интернет-Магазин 🛍"
        )


def main():
    # Bot tokenini quyidagi o'zgartiring
    updater = Updater("6842218151:AAGnd_y7ZuEwAc4W0ivdviM2y7wjRPMnHw8", use_context=True)

    # start komandasiga javob beruvchi handler qo'shamiz
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # salom habariga javob beruvchi handler qo'shamiz
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_salom))

    # Botni ishga tushiramiz
    updater.start_polling()

    # Dastur to'xtatilganda botni to'xtatamiz
    updater.idle()


if __name__ == '__main__':
    main()
