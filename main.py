from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pymongo import MongoClient
import asyncio
from config import BOT_TOKEN, MONGO_URL, DB_NAME, COLLECTION_NAME, ADMIN_ID

# ================= MongoDB =================
client = MongoClient(MONGO_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Broadcast Bot is Active!\n"
        "Use /broadcast <msg> or reply to a media with /broadcast."
    )

# ================= USERS =================
async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Only admin can use this command!")
        return

    total_users = collection.count_documents({})
    await update.message.reply_text(f"👥 Total Users in Bot: {total_users}")

# ================= BROADCAST =================
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Broadcast text or replied media to all users."""
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Only admin can broadcast!")
        return

    reply = update.message.reply_to_message
    text_msg = " ".join(context.args)

    msg_type = None
    caption = None
    file_id = None

    if reply:
        if reply.photo:
            msg_type = "photo"
            file_id = reply.photo[-1].file_id
            caption = reply.caption or text_msg
        elif reply.video:
            msg_type = "video"
            file_id = reply.video.file_id
            caption = reply.caption or text_msg
        elif reply.document:
            msg_type = "document"
            file_id = reply.document.file_id
            caption = reply.caption or text_msg
        elif reply.text:
            msg_type = "text"
            caption = reply.text
        else:
            await update.message.reply_text("❌ Unsupported media type!")
            return
    else:
        if not text_msg:
            await update.message.reply_text(
                "⚠️ Usage:\n/broadcast <message>\nOr reply to a media and type /broadcast"
            )
            return
        msg_type = "text"
        caption = text_msg

    users_list = list(collection.find({}))
    total = len(users_list)
    sent = 0
    failed = 0

    await update.message.reply_text(f"📢 Broadcasting to {total} users...")

    for user in users_list:
        user_id = user.get("user_id") or user.get("_id")
        if not user_id:
            continue
        try:
            if msg_type == "text":
                await context.bot.send_message(chat_id=user_id, text=caption)
            elif msg_type == "photo":
                await context.bot.send_photo(chat_id=user_id, photo=file_id, caption=caption)
            elif msg_type == "video":
                await context.bot.send_video(chat_id=user_id, video=file_id, caption=caption)
            elif msg_type == "document":
                await context.bot.send_document(chat_id=user_id, document=file_id, caption=caption)

            sent += 1
            await asyncio.sleep(0.2)

        except Exception:
            failed += 1
            await asyncio.sleep(0.1)

    await update.message.reply_text(
        f"✅ Done!\n📤 Sent: {sent}\n❌ Failed: {failed}\n👥 Total: {total}"
    )

# ================= MAIN =================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("users", users))  # 👈 ADDED

    app.run_polling()

if __name__ == "__main__":
    main()
