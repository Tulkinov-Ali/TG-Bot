from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from .buttons import inline  # keyboard
from .valyutas import multi_lang_values, Cceis
import requests as re


def valyuta(ccy):
    res = re.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/").json()
    for i in res:
        if i['Ccy'].lower() == ccy.lower():
            return i
    return None


def start(update: Update, context):
    user = update.message.from_user
    update.message.reply_html(f'Hello <b>{user.first_name}</b> Welcome to Real Time World Currency Checker',
                              reply_markup=inline())


log = {
    'page': 1
}

all_items = len(multi_lang_values)
page_items = 9
if all_items % page_items != 0:
    max_page = (all_items // page_items) + 1
else:
    max_page = all_items // page_items


# def msg_handler(update: Update, context):
#     msg = update.message.text
#     natija = valyuta(msg)
#
#     if msg == '<<Prev':
#         if log['page'] == 1:
#             update.message.reply_html('You are in the first page!')
#         else:
#             log['page'] = log['page'] - 1
#             update.message.reply_html('Previous page', reply_markup=keyboard('Currency', page=log['page']))
#
#     elif msg == 'Next>>':
#         if log['page'] == max_page:
#             update.message.reply_html('You are on the last page!')
#         else:
#             log['page'] = log['page'] + 1
#             update.message.reply_html('Next page', reply_markup=keyboard('Currency', page=log['page']))
#     elif natija:
#         update.message.reply_text(
#             f"Name: {natija['CcyNm_UZ']}\nShort: {natija['Ccy']}\nRate:{natija['Rate']}\nDate:{natija['Date']}")
#     else:
#         update.message.reply_html(f'You have entered wrong Currency!!!')


def inline_msg(update: Update, context):
    query = update.callback_query
    all_data = query.data
    sp_data = all_data.split('_')
    data = sp_data[0]
    lang = 'uz' if len(sp_data) == 1 else sp_data[1]
    if data in Cceis:
        try:
            query.message.edit_text(f'{data}', reply_markup=inline('val', page=log['page'], lang=lang))
            inline_natija = valyuta(data)
            query.message.reply_text(
                f"Name: {inline_natija['CcyNm_UZ']}\nShort: {inline_natija['Ccy']}\nRate:{inline_natija['Rate']}\nDate:{inline_natija['Date']}")
        except:
            pass
        return 0

    elif data == 'ru':
        query.message.edit_text('Добро пожаловать, вы выбрали Русский язык', reply_markup=inline('val', lang='ru'))
        # query.message.reply_text('Выберите валюту.', reply_markup=inline('val', lang='ru'))

    elif data == 'uz':
        query.message.edit_text('Xush kelibsiz, siz Uzbek tilini tanladingiz', reply_markup=inline('val', lang='uz'))
        # query.message.reply_text('Valyutani tanlang.', reply_markup=inline('val', lang='uz'))

    elif data == 'en':
        query.message.edit_text('Welcome, you have chosen English language', reply_markup=inline('val', lang='en'))
        # query.message.reply_text('Select the Currency', reply_markup=inline('val', lang='en'))

    elif data == 'valyutas':
        query.message.edit_text('bla bla bla', reply_markup=inline('val', lang=lang))

    elif data == 'prev':
        if log['page'] == 1:
            query.answer("You are in the first Page")
        else:
            log['page'] = log['page'] - 1
            query.message.edit_text('Previous page', reply_markup=inline('val', page=log['page'], lang=lang))

    elif data == 'next':
        if log['page'] == max_page:
            query.answer("You are in the Last Page")
        else:
            log['page'] = log['page'] + 1
            query.message.edit_text('Next page', reply_markup=inline('val', page=log['page'], lang=lang))
