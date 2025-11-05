import os

# Your bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7917897990:AAFj1hn2JWJ5pvKNUrbL9sDaKmqug0dlcO8")

# MongoDB (you can use SRV URL here)
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://teddugovardhan544_db_user:WVjIA96jQ31net0j@cluster0.kwkkleo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Your old database and collection
DB_NAME = os.environ.get("DB_NAME", "filestore")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "users")

# Admin Telegram ID (only admin can broadcast)
ADMIN_ID = int(os.environ.get("ADMIN_ID", "5654093580"))
