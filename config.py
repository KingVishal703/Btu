import os

# Your bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6335646151:AAF22GWMVxarTI7lTuSRTBwsRA1IvwHrQXw")

# MongoDB (you can use SRV URL here)
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://mrsam:mrsam1212@cluster0.br8a94z.mongodb.net/?retryWrites=true&w=majority"
)

# Your old database and collection
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "Telegram_files")

# Admin Telegram ID (only admin can broadcast)
ADMIN_ID = int(os.environ.get("ADMIN_ID", "5654093580"))
