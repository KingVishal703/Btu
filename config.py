import os

# Your bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7648577586:AAG10G2khDJyFiQtwhVT7fyhjjo_AX8jFeI")

# MongoDB (you can use SRV URL here)
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://sankarbio8098:sankar@cluster0.5gfezqj.mongodb.net/?retryWrites=true&w=majority"
)

# Your old database and collection
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "Telegram_files")

# Admin Telegram ID (only admin can broadcast)
ADMIN_ID = int(os.environ.get("ADMIN_ID", "5654093580"))
