import os
from dotenv import load_dotenv

env = load_dotenv("config.env")

if env:
    OWNER_ID = os.environ.get("1813373023")
    sudo_users = list(map(int, os.environ.get("1813373023", "").split()))
    GROUP_ID = os.environ.get("-1002103727164")
    TOKEN = os.environ.get("7191385539:AAHwhpupUBixxB7wehd5PR2NWaUawVz9l3A")
    mongo_url = os.environ.get("mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
    if os.environ.get("https://telegra.ph/file/a0a18f4619fed4b45ea01.jpg") != None:
        PHOTO_URL = os.environ.get("https://telegra.ph/file/a0a18f4619fed4b45ea01.jpg") 
    else:
        PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = os.environ.get("FallenXDeveloper")
    UPDATE_CHAT = os.environ.get("FallenXDeveloper")
    BOT_USERNAME = os.environ.get("Keqing_WaifuBot")
    CHARA_CHANNEL_ID = os.environ.get("-1002074617147")
    api_id = os.environ.get("21846639")
    api_hash = os.environ.get("2cebc99bd8378b5237b31ea8e7496d79")
else:
    OWNER_ID = 1813373023
    sudo_users = ["1813373023"]
    GROUP_ID = -1002103727164
    mongo_url = "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority"    
    TOKEN = "7191385539:AAHwhpupUBixxB7wehd5PR2NWaUawVz9l3A"
    PHOTO_URL = ["https://telegra.ph/file/a0a18f4619fed4b45ea01.jpg", "https://telegra.ph/file/a0a18f4619fed4b45ea01.jpg"]
    SUPPORT_CHAT = "FallenXDeveloper"
    UPDATE_CHAT = "FallenXDeveloper"
    BOT_USERNAME = "Keqing_WaifuBot"
    CHARA_CHANNEL_ID = -1002074617147
    api_id = 21846639
    api_hash = "2cebc99bd8378b5237b31ea8e7496d79"
