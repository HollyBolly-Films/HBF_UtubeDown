from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) \nJust Send a Youtube Url and see the magic "
    await message.reply_text(helptxt)
