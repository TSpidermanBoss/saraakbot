import wikipedia
from telegram import Update, Bot
from telegram.ext import run_async, Filters
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

def wiki(bot: Bot, update: Update):
        query = str(update.effective_message.text[6:])
        result = '**Wiki:**\n' + query + '\n\n**Results:**\n' + str(wikipedia.summary(query))
        update.effective_message.reply_markdown(result)

__help__ = """
 ➡️ /wiki: To get Some Information.
 """
__mod_name__ = "Wikipedia"

WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki)
dispatcher.add_handler(WIKI_HANDLER)
