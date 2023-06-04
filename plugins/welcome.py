import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from info import WELCOM_TEXT, BYE_TEXT

@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=WELCOM_TEXT)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=BYE_TEXT)
