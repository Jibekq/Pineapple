import telebot
import os
import requests
import uuid
import eyed3
from types import GenericAlias

token = "1916204899:AAEQs7q9ChpXFKorT6wkvhscmxVmjISIQDk"

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hey")

@bot.message_handler(content_types=["text"]) 
def text(message): 
    bot.send_message(message.chat.id, 'Hello') 

# @bot.message_handler(content_types=['photo'])
# def photo(message):
#     save_url = '/Users/User/project/pineapple/images'
#     fileID = message.photo[-1].file_id
#     file_info = bot.get_file(fileID)
#     image_name = str(uuid.uuid4())+'.jpg'
#     downloaded_file = bot.download_file(file_info.file_path)

#     with open(save_url+image_name, 'wb') as new_file:
#         new_file.write(downloaded_file)
#     bot.reply_to(message, f"Saved")

@bot.message_handler(content_types=['video'])
def video(message):
    fileID = message.video.file_id
    file_info = bot.get_file(fileID)
    video_name = str(uuid.uuid4())+'.mp4'
    downloaded_file = bot.download_file(file_info.file_path)

    with open(video_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, f"Saved")


# @bot.message_handler(content_types=['audio'])
# def video(message):
    
#     fileID = message.audio.file_id
#     file_info = bot.get_file(fileID)
#     audio_name = str(uuid.uuid4())+'.mp3'
#     downloaded_file = bot.download_file(file_info.file_path)

#     with open(audio_name, 'wb') as new_file:
#         new_file.write(downloaded_file)
#     bot.reply_to(message, f"Saved")



bot.polling()