import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات خود را اینجا قرار دهید
TOKEN = "7678926810:AAHjGHU-RXCvSCW-W_1l4ExzoR7tGjRAvJo"

# لینک‌ها و آیدی کانال‌ها
CHANNEL_1 = "https://t.me/kllllkllllll"
CHANNEL_2 = "https://t.me/fudcffyiyfygjjff"
CHANNEL_3 = "https://t.me/ftutgurfutuufududuftut"
LINK_4 = "https://www.downloadha.com/game/alan-wake-2/"
CHANNEL_IDS = ["@kllllkllllll", "@fudcffyiyfygjjff", "@ftutgurfutuufududuftut"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("سلام! برای دیدن لینک‌ها، 'نمایش لینک' رو بفرست.")

async def show_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    bot = context.bot

    # بررسی عضویت
    is_member_all = True
    for channel_id in CHANNEL_IDS:
        try:
            member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                is_member_all = False
                break  # اگر در یک کانال عضو نبود، حلقه رو می‌شکنیم ولی ادامه می‌دیم
        except telegram.error.TelegramError as e:
            is_member_all = False
            await update.message.reply_text(f"خطا در بررسی عضویت در {channel_id}: {str(e)}")
            return

    # نمایش لینک‌ها
    response = (
        "لینک‌ها:\n"
        f"1. {CHANNEL_1}\n"
        f"2. {CHANNEL_2}\n"
        f"3. {CHANNEL_3}\n"
    )
    
    if is_member_all:
        response += f"4. {LINK_4}"
    else:
        response += "برای دیدن لینک چهارم، در سه کانال بالا عضو شوید!"

    await update.message.reply_text(response)

def main() -> None:
    # راه‌اندازی ربات
    app = Application.builder().token(TOKEN).build()

    # ثبت دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Text(["نمایش لینک"]), show_links))

    # شروع ربات
    print("ربات شروع به کار کرد...")
    app.run_polling()

if __name__ == "__main__":
    main()