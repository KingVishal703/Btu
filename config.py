import os

# Your bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8575350149:AAHSlhzLLRuP0Rk8NvmSdHnFqXz3pbZpKKg")

# MongoDB (you can use SRV URL here)
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://bosstgbots_db_user:DiRFdWd2U9kHoP4j@cluster0.g6p3m4j.mongodb.net/?appName=Cluster0"
)

# Your old database and collection
DB_NAME = os.environ.get("DB_NAME", "techvjbotz")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "techvjbotz")

# Admin Telegram ID (only admin can broadcast)
ADMIN_ID = int(os.environ.get("ADMIN_ID", "5654093580"))
