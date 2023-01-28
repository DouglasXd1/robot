# Copyright (c) 2022 Shiinobu Project

from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from EmikoRobot import pbot as Client
from EmikoRobot import (
    OWNER_ID as owner,
    SUPPORT_CHAT as log,
)
from EmikoRobot.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command("lapor"))
@capture_err
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username} / `{msg.chat.id}`")
    else:
        chat_username = (f"ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ / `{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    thumb = "https://telegra.ph/file/46f9ca36ad49d0223c269.jpg"
    
    bug_report = f"""
**#BUG : ** **[ꝛʌᴢᴏʀ](https://t.me/rzrgnshn)**
**ᴅᴀʀɪ ᴘᴇɴɢɢᴜɴᴀ : ** **{mention}**
**ɪᴅ ᴘᴇɴɢɢᴜɴᴀ : ** **{user_id}**
**ɢʀᴏᴜᴘ : ** **{chat_username}**
**ʟᴀᴘᴏʀᴀɴ ᴋᴇsᴀʟᴀʜᴀɴ : ** **{bugs}**
**ᴡᴀᴋᴛᴜ ʟᴀᴘᴏʀᴀɴ : ** **{datetimes}**"""

    
    if msg.chat.type == "private":
        await msg.reply_text("❎ <b>ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ ʜᴀɴʏᴀ ʙᴇʀɢᴜɴᴀ ᴅɪ sᴜᴘᴇʀ ɢʀᴏᴜᴘ.</b>")
        return

    if user_id == owner:
        if bugs:
            await msg.reply_text(
                f"❎ <b>ᴀᴘᴀ ʏᴀɴɢ ʜᴀʀᴜs ᴅɪ ʟᴀᴘᴏʀᴋᴀɴ? ᴅᴀsᴀʀ ᴘᴇᴍɪʟɪᴋ ʙᴏᴅᴏʜ !!</b>",
            )
            return
        else:
            await msg.reply_text(
                f"❎ <b>ᴘᴇᴍɪʟɪᴋ ʙᴏᴅᴏʜ</b>",
            )
    elif user_id != owner:
        if bugs:
            await msg.reply_text(
                f"<b>ʟᴀᴘᴏʀᴀɴ ᴋᴇsᴀʟᴀʜᴀɴ : {bugs}</b>\n\n"
                "✅ <b>ʟᴀᴘᴏʀᴀɴ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪ ʟᴀᴘᴏʀᴋᴀɴ ᴋᴇ ᴘᴇᴍɪʟɪᴋ ʙᴏᴛ ɪɴɪ</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴛᴜᴛᴜᴘ", callback_data=f"close_reply")
                        ]
                    ]
                )
            )
            await Client.send_photo(
                log,
                photo=thumb,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ʟɪʜᴀᴛ ʟᴀᴘᴏʀᴀɴ", url=f"{msg.link}")
                        ],
                        [
                            InlineKeyboardButton(
                                "ᴛᴜᴛᴜᴘ", callback_data=f"close_send_photo")
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"❎ <b>ᴀᴘᴀ ʏᴀɴɢ ᴅɪ ʟᴀᴘᴏʀᴋᴀɴ?</b>",
            )
        
    

@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(Client, CallbackQuery):
    await CallbackQuery.message.delete()


__mod_name__ = "Bug"
