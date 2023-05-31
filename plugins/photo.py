from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🇧🇷🇮🇬🇭🇹", callback_data="bright"),
                        InlineKeyboardButton(text="🇲🇮🇽🇪🇩", callback_data="mix"),
                        InlineKeyboardButton(text="🇧 & 🇼", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="🇨🇮🇷🇨🇱🇪", callback_data="circle"),
                        InlineKeyboardButton(text="🇧🇱🇺🇷", callback_data="blur"),
                        InlineKeyboardButton(text="🇧🇴🇷🇩🇪🇷", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="🇸🇹🇮🇨🇰🇪🇷", callback_data="stick"),
                        InlineKeyboardButton(text="🇷🇴🇹🇦🇹🇪", callback_data="rotate"),
                        InlineKeyboardButton(text="🇨🇴🇳🇹🇷🇦🇸🇹", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="🇸🇪🇵🇮🇦", callback_data="sepia"),
                        InlineKeyboardButton(text="🇵🇪🇳🇨🇮🇱", callback_data="pencil"),
                        InlineKeyboardButton(text="🇨🇦🇷🇹🇴🇴🇳", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="🇮🇳🇻🇪🇷🇹", callback_data="inverted"),
                        InlineKeyboardButton(text="🇬🇱🇮🇹🇨🇭", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="🇷🇪🇲🇴🇻🇪 🇧🇬", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="🇨🇱🇴🇨🇪", callback_data="close_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text(f"{e} \nSomething went wrong!", quote=True)
            except Exception:
                return
