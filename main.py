import telebot
from telebot import types
from requests import get, RequestException

bot = telebot.TeleBot('token', threaded=False)


class Pics(object):
    def __init__(self):
        self.html = None
        self.url = None

    def get_html(self):
        try:
            response = get(self.url)
            response.raise_for_status()
            return response.text
        except (RequestException, ValueError):
            return False

    def get_waifu_nsfw(self):
        self.url = 'https://api.waifu.pics/nsfw/waifu'
        self.html = self.get_html()
        return str(self.get_html()[8:-3])

    def get_neko_nsfw(self):
        self.url = 'https://api.waifu.pics/nsfw/neko'
        self.html = self.get_html()
        return str(self.get_html()[8:-3])

    def get_blowjob_nsfw(self):
        self.url = 'https://api.waifu.pics/nsfw/blowjob'
        self.html = self.get_html()
        return str(self.get_html()[8:-3])

    def get_trap_nsfw(self):
        self.url = 'https://api.waifu.pics/nsfw/trap'
        self.html = self.get_html()
        return str(self.get_html()[8:-3])

    def get_waifu_sfw(self):
        self.url = 'https://api.waifu.pics/sfw/waifu'
        self.html = self.get_html()
        return str(self.get_html()[8:-3])

    def get_neko_sfw(self):
        self.url = 'https://api.waifu.pics/sfw/neko'
        self.html = self.get_html()
        return str(self.get_html()[8:-3])

    def get_awoo_sfw(self):
        self.url = 'https://api.waifu.pics/sfw/awoo'
        self.html = self.get_html()
        return str(self.get_html()[8:-3])


pics = Pics()


@bot.message_handler(commands=['start'])
def process_start_command(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb_anime = types.KeyboardButton('♿ Anime crap')

    keyboard.row(kb_anime)

    bot.send_message(message.chat.id, 'What d\'you want?'.format(message.from_user), reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def process_help_command(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb_anime = types.KeyboardButton('♿ Anime crap')

    keyboard.row(kb_anime)

    bot.send_message(message.chat.id,
                     'What can I do? Hmm, let me think... Maybe you\'ll pay attention to the keyboard below and find '
                     'out for yourself?'.format(message.from_user), reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.chat.type == 'private':
        if message.text == '♿ Anime crap':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

            kb_sfw = types.KeyboardButton('📌 SFW')
            kb_nsfw = types.KeyboardButton('🔞 NSFW')
            kb_back = types.KeyboardButton('🔙 Back')

            keyboard.row(kb_sfw, kb_nsfw)
            keyboard.row(kb_back)

            bot.send_message(message.chat.id, 'dude...'.format(message.from_user), reply_markup=keyboard)

        elif message.text == '🔞 NSFW':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

            kb_waifu_nsfw = types.KeyboardButton('👀 Nothing special')
            kb_neko_nsfw = types.KeyboardButton('🐈 Neko')
            kb_blowjob_nsfw = types.KeyboardButton('👄 BJ')
            kb_trap_nsfw = types.KeyboardButton('🤡 Pls no..')
            kb_back = types.KeyboardButton('🔙 Back')

            keyboard.row(kb_waifu_nsfw, kb_neko_nsfw)
            keyboard.row(kb_blowjob_nsfw, kb_trap_nsfw)
            keyboard.row(kb_back)

            bot.send_video(message.chat.id,
                           'https://c.tenor.com/GBdIH5sL4XQAAAAM/the-rock-rock.gif'.format(message.from_user),
                           reply_markup=keyboard, reply_to_message_id=message.message_id)

        elif message.text == '👀 Nothing special':
            try:
                bot.send_photo(message.chat.id, get(pics.get_waifu_nsfw()).content,
                               reply_to_message_id=message.message_id)
            except Exception as e:
                bot.send_message(message.chat.id, 'Try again', reply_to_message_id=message.message_id)
                print('Photo sending error: ', e)

        elif message.text == '🐈 Neko':
            try:
                bot.send_photo(message.chat.id, get(pics.get_neko_nsfw()).content,
                               reply_to_message_id=message.message_id)
            except Exception as e:
                bot.send_message(message.chat.id, 'Try again', reply_to_message_id=message.message_id)
                print('Photo sending error: ', e)

        elif message.text == '👄 BJ':
            try:
                bot.send_video(message.chat.id, get(pics.get_blowjob_nsfw()).content,
                               reply_to_message_id=message.message_id)
            except Exception as e:
                bot.send_message(message.chat.id, 'Try again', reply_to_message_id=message.message_id)
                print('Photo sending error: ', e)

        elif message.text == '🤡 Pls no..':
            try:
                bot.send_photo(message.chat.id, get(pics.get_trap_nsfw()).content,
                               reply_to_message_id=message.message_id)
            except Exception as e:
                bot.send_message(message.chat.id, 'Try again', reply_to_message_id=message.message_id)
                print('Photo sending error: ', e)

        elif message.text == '📌 SFW':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

            kb_waifu_sfw = types.KeyboardButton('🚺 Adam\'s Rib')
            kb_neko_sfw = types.KeyboardButton('🐱 Neko')
            kb_awoo_sfw = types.KeyboardButton('🐺 Wolves')
            kb_back = types.KeyboardButton('🔙 Back')

            keyboard.row(kb_waifu_sfw, kb_neko_sfw, kb_awoo_sfw)
            keyboard.row(kb_back)

            bot.send_video(message.chat.id,
                           'https://c.tenor.com/X24lJCALrgEAAAAM/rock-nodding.gif'.format(message.from_user),
                           reply_markup=keyboard, reply_to_message_id=message.message_id)

        elif message.text == '🚺 Adam\'s Rib':
            try:
                bot.send_photo(message.chat.id, get(pics.get_waifu_sfw()).content,
                               reply_to_message_id=message.message_id)
            except Exception as e:
                bot.send_message(message.chat.id, 'Try again', reply_to_message_id=message.message_id)
                print('Photo sending error: ', e)

        elif message.text == '🐱 Neko':
            try:
                bot.send_photo(message.chat.id, get(pics.get_neko_sfw()).content,
                               reply_to_message_id=message.message_id)
            except Exception as e:
                bot.send_message(message.chat.id, 'Try again', reply_to_message_id=message.message_id)
                print('Photo sending error: ', e)

        elif message.text == '🐺 Wolves':
            try:
                bot.send_photo(message.chat.id, get(pics.get_awoo_sfw()).content,
                               reply_to_message_id=message.message_id)
            except Exception as e:
                bot.send_message(message.chat.id, 'Try again', reply_to_message_id=message.message_id)
                print('Photo sending error: ', e)

        elif message.text == '🔙 Back':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

            kb_anime = types.KeyboardButton('♿ Anime crap')

            keyboard.row(kb_anime)

            bot.send_message(message.chat.id, 'What d\'you want?'.format(message.from_user), reply_markup=keyboard)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print('Bot error:', e)
