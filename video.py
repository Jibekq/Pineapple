# @bot.message_handler(content_types=['video'])
# def video(message):
#     fileID = message.video[-1].file_id
#     video_name = message.json['video']['video_name']
#     file_info = bot.get_file(fileID)
#     downloaded_file = bot.download_file(file_info.file_path)

#     with open(video_name, "wb") as new_folder:
#         file_content = bot.download_file(file_info.file_path)
#         new_folder.write(downloaded_file)
#     bot.reply_to(message, f"I saved the video :D")

# @bot.message_handler(content_types=['document'])
# def get_file(message):
#     file_name = message.document.file_name
#     file_info = bot.get_file(message.document.file_id)
#     with open(file_name, "wb") as f:
#         file_content = bot.download_file(file_info.file_path)
#         f.write(file_content)
#     bot.reply_to(message, f"OK. Сохранил {file_name}")


# @bot.message_handler(content_types=['video'])      
# def send_text(message):
    
#     file_info = bot.get_file(file_id)
#     downloaded_file = bot.download_file(file_info.file_path)
#     src = 'files/' + file_info.file_path
#     with open(src, 'wb') as new_file:
#         new_file.write(downloaded_file)
#         bot.reply_to(message, f"I saved the video :D")


