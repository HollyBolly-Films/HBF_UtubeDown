from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/hollybolly_films"),
        InlineKeyboardButton("Support 😊", url="https://t.me/hbf_supportbot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nI Can Upload Video/Mp3 File in Telegram using youtube Link\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
