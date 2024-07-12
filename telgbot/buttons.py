from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from .valyutas import multi_lang_values


# def keyboard(type=None, page=1):
#     btn = []
#     if type == 'Currency':
#         limit = 9
#         offset = (page - 1) * limit
#         status = True
#         for i in range(offset + 1, page * limit, 3):
#             try:
#                 btn.append([
#                     KeyboardButton(vals[i - 1]['Ccy']),
#                     KeyboardButton(vals[i]['Ccy']),
#                     KeyboardButton(vals[i + 1]['Ccy'])
#                 ])
#             except:
#                 status = False
#
#         if status is False and len(vals) % 2:
#             btn.append([KeyboardButton(vals[-1]['Ccy'])])
#
#         btn.append([
#             KeyboardButton("<<Prev"),
#             KeyboardButton("Next>>"),
#         ])
#
#     return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def inline(type=None, page=1, lang='uz'):
    btn = []
    lang = lang.upper()
    if type == 'val':
        limit = 9
        offset = (page - 1) * limit
        status = True
        for i in range(offset + 1, page * limit, 3):
            try:
                btn.append([
                    InlineKeyboardButton(multi_lang_values[i - 1][f'CcyNm_{lang}'],
                                         callback_data=f"{multi_lang_values[i - 1]['Ccy']}_{lang}"),
                    InlineKeyboardButton(multi_lang_values[i][f'CcyNm_{lang}'],
                                         callback_data=f"{multi_lang_values[i]['Ccy']}_{lang}"),
                    InlineKeyboardButton(multi_lang_values[i + 1][f'CcyNm_{lang}'],
                                         callback_data=f"{multi_lang_values[i + 1]['Ccy']}_{lang}")
                ])
            except:
                status = False

        if status is False and len(multi_lang_values) % 3 == 1:
            btn.append([InlineKeyboardButton(multi_lang_values[-1][f'CcyNm_{lang}'],
                                             callback_data=f"{multi_lang_values[-1]['Ccy']}_{lang}")])
        if status is False and len(multi_lang_values) % 3 == 2:
            btn.append([InlineKeyboardButton(multi_lang_values[-1][f'CcyNm_{lang}'],
                                             callback_data=f"{multi_lang_values[-1]['Ccy']}_{lang}")])
            btn.append([InlineKeyboardButton(multi_lang_values[-2][f'CcyNm_{lang}'],
                                             callback_data=f"{multi_lang_values[-2]['Ccy']}_{lang}")])

        btn.append([
            InlineKeyboardButton("<<Prev", callback_data=f'prev_{lang}'),
            InlineKeyboardButton("Next>>", callback_data=f'next_{lang}'),
        ])

    else:
        btn = [
            [
                InlineKeyboardButton("🇺🇿uz", callback_data="uz"),
                InlineKeyboardButton("🇷🇺ru", callback_data="ru"),
                InlineKeyboardButton("🇺🇸en", callback_data="en"),
            ]
        ]

    return InlineKeyboardMarkup(btn)
