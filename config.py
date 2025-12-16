import os

# Your bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6417803923:AAFi4-J-ov9R-R4xKDkQJXFk9IjKy_5uLJI")

# MongoDB (you can use SRV URL here)
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://simoya4228:JQU2RGSyGXUqMcS0@cluster0.0qtubmi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Your old database and collection
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "Telegram_files")

# Admin Telegram ID (only admin can broadcast)
ADMIN_ID = int(os.environ.get("ADMIN_ID", "5654093580"))
