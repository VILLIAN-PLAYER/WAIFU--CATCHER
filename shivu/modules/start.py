import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, Updater

PHOTO_URL = ["https://telegra.ph/file/40832edc299ed8950319d.jpg"]
BOT_USERNAME = "Keqing_WaifuBot"

def start(update: Update, context: CallbackContext):
    caption = "🎐 **ʜᴇʏ ᴛʜᴇʀᴇ...!**\n\n"
    caption += "**⍟ ɪ ᴀᴍ ᴄᴀᴛᴄʜ ʏᴏᴜʀ ᴡᴀɪғᴜ ʙᴏᴛ,**\n"
    caption += "ɪ sᴘᴀᴡɴ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs, ᴀɴᴅ ʟᴇᴛ ᴜsᴇʀs ᴄᴏʟʟᴇᴄᴛ ᴛʜᴇᴍ.\n\n"
    caption += "⍟ sᴏ ᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.\n\n"
    caption += "ʜɪᴛ /help ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ."

    keyboard = [
        [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    photo_url = random.choice(PHOTO_URL)
    
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='Markdown')

dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
