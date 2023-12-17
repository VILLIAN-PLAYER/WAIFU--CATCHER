import os
from dotenv import load_dotenv

env = load_dotenv("config.env")

if env:
    OWNER_ID = os.environ.get("OWNER_ID")
    sudo_users = list(map(int, os.environ.get("sudo_users", "").split()))
    GROUP_ID = os.environ.get("GROUP_ID")
    TOKEN = os.environ.get("TOKEN")
    mongo_url = os.environ.get("MONGODB_URL")
    if os.environ.get("PHOTO_URL") != None:
        PHOTO_URL = os.environ.get("PHOTO_URL") 
    else:
        PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT")
    UPDATE_CHAT = os.environ.get("UPDATE_CHAT")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    CHARA_CHANNEL_ID = os.environ.get("CHARA_CHANNEL_ID")
    api_id = os.environ.get("api_id")
    api_hash = os.environ.get("api_hash")
else:
    OWNER_ID = 5443243540
    sudo_users = ["5715764478", "5690711835", "6765826972"]
    GROUP_ID = -1001931513350
    TOKEN = "6970532785:AAHt-X1qhAhTpN2R942BrX44Koa9a1ilWaU"
    mongo_url = "mongodb+srv://HaremDB:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "The_Catch_Squad"
    UPDATE_CHAT = "botupdatex"
    BOT_USERNAME = "CatchEmWaifuBot"
    CHARA_CHANNEL_ID = -1002064277119
    api_id = 28122413
    api_hash = "750432c8e1b221f91fd2c93a92710093"