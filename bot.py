import os
from pyrogram import Client, filters
import shutil
from os import system as cmd
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6280972722:AAG3GrropPJhZvfjljtgppKeeXpfpBVZG4Y"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت الرفع لأرشيف  , فقط أرسل الملف هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.document | filters.photo | filters.audio | filters.video | filters.voice)
def _telegram_file(client, message):
  
  user_id = message.from_user.id 
  sent_message = message.reply_text('جار االرفع\n\n', quote=True)
  file = message
  file_path = message.download(file_name="./downloads/")


@bot.on_message(filters.command('upld') & filters.private)
def command2(bot,message):
  cmd("rclone copy ./downloads/ 'karim':'tasmeem155151sx' --progress ")
  shutil.rmtree('./downloads/')
bot.run()
