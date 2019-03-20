# -*- coding: utf-8 -*-

import config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text", "document", "audio", "photo", "video", "voice"])
def repeat_all_messages(message):
    if message.audio:
        bot.send_audio(message.chat.id, message.audio.file_id)

    elif message.photo:
        bot.send_photo(message.chat.id, message.photo[0].file_id)

    elif message.text:
        bot.send_message(message.chat.id, message.text)

    elif message.document:
        bot.send_document(message.chat.id, message.document.file_id)

    elif message.video:
        bot.send_video(message.chat.id, message.video.file_id)

    elif message.voice:
        bot.send_voice(message.chat.id, message.voice.file_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
