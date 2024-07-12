from django.core.management import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from django.conf import settings

from telgbot.views import start, inline_msg


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(settings.TOKEN)
        print("bot server is running", updater.bot.username)
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(inline_msg))

        updater.start_polling()
        updater.idle()
