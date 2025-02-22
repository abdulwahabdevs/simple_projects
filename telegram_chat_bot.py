from typing import Final
from xml.dom.pulldom import ErrorHandler

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater

# Constants
TOKEN: Final[str] = '...'
BOT_USERNAME: Final[str] = '...'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! Nice to meet you. Let\'s chat')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('How can I help you?')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This a set command')

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'Wassup man! How u doin\'?'
    if 'how are you' in processed:
        return 'Fantastic'
    if 'what can you do' in processed:
        return 'I can talk to you like right now'
    if 'can you think' in processed:
        return 'Not yet. I am not fully developed'
    # else:
    return 'I don\'t understand'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Log
    print(f'{update.message.chat.id} in {message_type}: "{text}"')

    # check if bot is mention
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return

    response: str = handle_response(text)

    # Reply
    print('Bot: ' + response)
    await update.message.reply_text(response)

async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update "{update}" caused error "{context.error}"')


def main():
    print('Starting up the bot...')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # errors
    app.add_error_handler(handle_error)

    # Polling
    print('Polling...')
    app.run_polling(poll_interval=5)


if __name__ == '__main__':
    main()






