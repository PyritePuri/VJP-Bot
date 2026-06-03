import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ContextTypes
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("BOT_TOKEN")

MANIFESTO = """
📜 *Vinod Janata Party — Official Manifesto*

🎯 *Pillar 1: Maximum Vibes*
We promise to increase national vibes by 420%.

🍜 *Pillar 2: Free Maggi for All*
Every citizen deserves a hot bowl of Maggi, funded by the government.

😴 *Pillar 3: Nap Rights*
A mandatory 2-hour afternoon nap for all working citizens.

📱 *Pillar 4: Wi-Fi is a Human Right*
5G in every jungle, chai stall, and jugaad vehicle.

🐄 *Pillar 5: Cows Get Voting Rights*
They've always had opinions. It's time they were heard.

*Vote VJP — Sab ka Vinod, Sab ka Vikas!* 🇮🇳
"""

SLOGANS = [
    "🔊 Vinod hi Vikas hai!",
    "🔊 Ek baar mauka do, hum kuch nahi karenge!",
    "🔊 VJP: Promises made, promises... whatever.",
    "🔊 Abki baar, Vinod Sarkar!",
    "🔊 Na khaunga, na khaane dunga... actually, thoda kha lenge.",
]

slogan_index = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📜 Read Manifesto", callback_data="manifesto")],
        [InlineKeyboardButton("🔊 Party Slogan", callback_data="slogan")],
        [InlineKeyboardButton("🗳️ Join the Party", callback_data="join")],
        [InlineKeyboardButton("📊 Our Achievements", callback_data="achievements")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🇮🇳 *Welcome to the Vinod Janata Party!*\n\n"
        "_The only party that's honest about being a party_ 🎉\n\n"
        "What would you like to know?",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global slogan_index
    query = update.callback_query
    await query.answer()

    if query.data == "manifesto":
        await query.message.reply_text(MANIFESTO, parse_mode="Markdown")

    elif query.data == "slogan":
        slogan = SLOGANS[slogan_index % len(SLOGANS)]
        slogan_index += 1
        await query.message.reply_text(slogan)

    elif query.data == "join":
        await query.message.reply_text(
            "🎊 *Congratulations! You've joined VJP!*\n\n"
            "Your membership benefits:\n"
            "✅ Bragging rights\n"
            "✅ A imaginary party card\n"
            "✅ Zero responsibilities\n"
            "✅ Access to our vibes\n\n"
            "_Note: VJP is a parody party. No actual politics involved._ 😄",
            parse_mode="Markdown"
        )

    elif query.data == "achievements":
        await query.message.reply_text(
            "📊 *VJP's Glorious Achievements*\n\n"
            "• Successfully did nothing: ✅\n"
            "• Promised everything: ✅\n"
            "• Delivered vibes: ✅\n"
            "• Won zero elections: ✅ (as planned)\n"
            "• Made people laugh: ✅✅✅\n\n"
            "_Sab moh maya hai._ 🙏",
            parse_mode="Markdown"
        )

async def slogan_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global slogan_index
    slogan = SLOGANS[slogan_index % len(SLOGANS)]
    slogan_index += 1
    await update.message.reply_text(slogan)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("slogan", slogan_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("VJP Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
