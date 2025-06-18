from telegram.ext import (
    Updater,
    MessageHandler,
    CallbackContext,
    Filters,
    CommandHandler,
    CallbackQueryHandler,
)
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

token = "8016350842:AAEvU0fcRkhyo9qzKCBCZwIwIBWE3KUKeW4"

updater = Updater(token=token)


def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat_id

    bot = context.bot

    keyboard1 = InlineKeyboardButton("dislike 👎 0", callback_data="1dislike,0,0")
    keyboard2 = InlineKeyboardButton("like 👍 0", callback_data="1like,0,0")
    reply_markup = InlineKeyboardMarkup(
        [
            [keyboard1, keyboard2],
        ]
    )

    bot.send_message(
        chat_id=chat_id,
        text="Hello @" + update.message.chat.username,
        reply_markup=reply_markup,
    )


def query(update: Update, context: CallbackContext):
    if update.callback_query:
        button = update.callback_query.data
        parts = button.split(",")
        action = parts[0]
        count_dislike = int(parts[1])
        count_like = int(parts[2])

        if "dislike" in button:
            count_dislike += 1
        else:
            count_like += 1
        keyboard1 = InlineKeyboardButton(
            f"dislike 👎 {count_dislike}",
            callback_data=f"1dislike,{count_dislike},{count_like}",
        )
        keyboard2 = InlineKeyboardButton(
            f"like 👍 {count_like}", callback_data=f"1like,{count_dislike},{count_like}"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [keyboard1, keyboard2],
            ]
        )
        # Example: answer the callback query to avoid Telegram client loading icon
        update.callback_query.edit_message_reply_markup(reply_markup=reply_markup)


dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler(command="start", callback=start))
dispatcher.add_handler(CallbackQueryHandler(callback=query, pattern="1"))


updater.start_polling()
updater.idle()