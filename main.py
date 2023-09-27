import telebot

API_TOKEN = 'secretinformation' # change this with your api token

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands = ['help', 'start'])
def send_welcome(msg):
    bot.send_message(msg.chat.id, "Ciao, inserisci due numeri separati da una virgola ed io calcolerò il loro modulo, ad esempio inserisci 21, 2 per avere 21 mod 2 = 1")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func = lambda message: True)
def modulo_message(msg):
    print(msg)
    print(msg.text)
    lista = msg.text
    splittato = lista.split(sep = ',')
    splittato[0] = int(splittato[0])
    splittato[1] = int(splittato[1])
    modulo = splittato[0] % splittato[1]
    #print(modulo)
    bot.reply_to(msg, modulo)


bot.polling()
