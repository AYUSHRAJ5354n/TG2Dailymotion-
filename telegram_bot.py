import logging
from telegram import Update, File
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Replace with your actual bot token
BOT_TOKEN = 'your_bot_token'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context):
    await update.message.reply_text('Hello! Send me a file and I will upload it to Dailymotion.')

async def handle_file(update: Update, context):
    file: File = await update.message.document.get_file()
    file_path = f"downloads/{update.message.document.file_name}"
    await file.download(file_path)
    await update.message.reply_text('File received! Now uploading to Dailymotion...')
    
    response = upload_to_dailymotion(file_path)
    if response.get('url'):
        await update.message.reply_text(f'File uploaded! Watch it here: {response.get("url")}')
    else:
        await update.message.reply_text('Failed to upload file to Dailymotion.')

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_file))

    application.run_polling()

if __name__ == '__main__':
    main()
