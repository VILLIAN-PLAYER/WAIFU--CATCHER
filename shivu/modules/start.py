import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler
from telegram.ext import MessageHandler

# Constants
PHOTO_URL = ["https://telegra.ph/file/40832edc299ed8950319d.jpg"]
SUPPORT_CHAT = "FallenXDeveloper"
UPDATE_CHAT = "FallenXDeveloper"
BOT_USERNAME = "Keqing_WaifuBot"
GROUP_ID = "-1002103727164"

# Function to handle the start command
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    # Check if user data exists
    if user_data is None:
        # Insert user data in collection if not found
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})

        # Notify group about new user
        await context.bot.send_message(chat_id=GROUP_ID, text=f"New user Started The Bot..\nUser: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    
    # Update user data if details changed
    else:
        if user_data['first_name'] != first_name or user_data['username'] != username:
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})
    
    # Send welcome message based on chat type
    if update.effective_chat.type == "private":
        caption = "🎐 ʜᴇʏ ᴛʜᴇʀᴇ...! 
              
◎ ─━──━─❖─━──━─ ◎
⍟ ɪ ᴀᴍ ᴄᴀᴛᴄʜ ʏᴏᴜʀ ᴡᴀɪғᴜ ʙᴏᴛ,
ɪ sᴘᴀᴡɴ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs, ᴀɴᴅ ʟᴇᴛ ᴜsᴇʀs ᴄᴏʟʟᴇᴄᴛ ᴛʜᴇᴍ.
⍟ sᴏ ᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.
◎ ─━──━─❖─━──━─ ◎

ʜɪᴛ help ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ."
    else:
        caption = "🎐 ʜᴇʏ ᴛʜᴇʀᴇ...! 
              
◎ ─━──━─❖─━──━─ ◎
⍟ ɪ ᴀᴍ ᴄᴀᴛᴄʜ ʏᴏᴜʀ ᴡᴀɪғᴜ ʙᴏᴛ,
ɪ sᴘᴀᴡɴ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs, ᴀɴᴅ ʟᴇᴛ ᴜsᴇʀs ᴄᴏʟʟᴇᴄᴛ ᴛʜᴇᴍ.
⍟ sᴏ ᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.
◎ ─━──━─❖─━──━─ ◎

ʜɪᴛ help ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ."
    
    keyboard = [
        [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
        [InlineKeyboardButton("SUPPORT", url=f'https://t.me/{SUPPORT_CHAT}'),
         InlineKeyboardButton("UPDATES", url=f'https://t.me/{UPDATE_CHAT}')],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    photo_url = random.choice(PHOTO_URL)
    
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

# Function to handle button interactions
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == 'help':
        # Handle button action
        pass
    elif query.data == 'back':
        # Handle button action
        pass

# Initialize the bot
updater = Updater("7191385539:AAHwhpupUBixxB7wehd5PR2NWaUawVz9l3A", use_context=True)
dispatcher = updater.dispatcher

# Add handlers
dispatcher.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', pass_update_queue=True, pass_job_queue=True, pass_user_data=True))
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()
updater.idle()