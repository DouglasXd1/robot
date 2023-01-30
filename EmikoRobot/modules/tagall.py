import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator

from EmikoRobot import telethn as client

spam_chats = []


@client.on(events.NewMessage(pattern="^/tagall|@all|/all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("__ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅᴀᴘᴀᴛ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅᴀʟᴀᴍ ɢʀᴜᴘ ᴅᴀɴ sᴀʟᴜʀᴀɴ 🍭__")

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(
            event.chat_id,
            event.sender_id
        ))
    except UserNotParticipantError:
        is_admin = False
    else:
        if (
                isinstance(
                    partici_.participant,
                    (
                            ChannelParticipantAdmin,
                            ChannelParticipantCreator
                    )
                )
        ):
            is_admin = True
    if not is_admin:
        return await event.reply("__ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ʏᴀɴɢ ʙɪsᴀ ᴍᴇɴʏᴇʙᴜᴛᴋᴀɴ sᴇᴍᴜᴀɴʏᴀ🍭__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.reply("__ʙᴇʀɪᴋᴀɴ sᴀʏᴀ sᴇʙᴜᴀʜ ᴋᴀᴛᴀ🍭__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴʏᴇʙᴜᴛᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ᴜɴᴛᴜᴋ ᴘᴇsᴀɴ ʟᴀᴍᴀ🍭 (ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪᴋɪʀɪᴍ sᴇʙᴇʟᴜᴍ sᴀʏᴀ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜᴘ)__")
    else:
        return await event.reply("__ʙᴀʟᴀs ᴘᴇsᴀɴ ᴀᴛᴀᴜ ʙᴇʀɪ sᴀʏᴀ ʙᴇʙᴇʀᴀᴘᴀ ᴛᴇᴋs ᴜɴᴛᴜᴋ ᴍᴇɴʏᴇʙᴜᴛᴋᴀɴ ᴏʀᴀɴɢ ʟᴀɪɴ🍭__")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ''
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"🍭 [{usr.first_name}](tg://user?id={usr.id})\n"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ''
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/stop$"))
async def cancel_spam(event):
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(
            event.chat_id,
            event.sender_id
        ))
    except UserNotParticipantError:
        is_admin = False
    else:
        if (
                isinstance(
                    partici_.participant,
                    (
                            ChannelParticipantAdmin,
                            ChannelParticipantCreator
                    )
                )
        ):
            is_admin = True
    if not is_admin:
        return await event.reply("__ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ🍭__")
    if not event.chat_id in spam_chats:
        return await event.reply("__ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘʀᴏsᴇs ʏᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ 🍭__")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__ʙᴇʀʜᴇɴᴛɪ ᴍᴇɴʏᴇʙᴜᴛᴋᴀɴ 🍭__")


__mod_name__ = "ᴛᴀɢ ᴀʟʟ 🍭"
__help__ = """
──「 Mention all func 」──

Douglas Can Be a Mention Bot for your group.

Only admins can tag all.  here is a list of commands

❂ /tagall or @all (reply to message or add another message) To mention all members in your group, without exception.
❂ /stop for canceling the mention-all.
"""
