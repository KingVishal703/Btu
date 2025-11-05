# Broadcast-OldUsers-Bot

A simple Telegram bot to broadcast text, photo, video, or document to all users from your old MongoDB database.

### 🌐 Environment Variables
- `BOT_TOKEN` — Your Telegram bot token
- `MONGO_URL` — Your MongoDB connection string
- `DB_NAME` — Your database name
- `COLLECTION_NAME` — Your user collection name
- `ADMIN_ID` — Your Telegram ID

### ⚙️ Commands
- `/start` — Check if bot is active
- `/broadcast <message>` — Send text message to all users
- Reply to any media with `/broadcast` — Send that media to all users

### 🚀 Deploy
1. Fork this repo  
2. Add environment variables in **Koyeb** or **Render**  
3. Deploy directly — no config changes needed!
