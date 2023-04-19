import telebot
import os
from datetime import datetime as dt

bot = telebot.TeleBot(os.environ.get("TOKEN"))

@bot.message_handler(commands=["Abrir"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Vou verificar se você tem a senha")

    with open("BD.txt", "r") as dataBaseTXT:
        dataBase = dataBaseTXT.readlines()

    autorized = False
    for line in dataBase:
        if str(mensagem.from_user.id) == line[:-1]:
            autorized = True

    if autorized:
        password = dt.now()
        bot.send_message(mensagem.chat.id, password)
    else:
        bot.send_message(mensagem.chat.id, "Nao abre")


@bot.message_handler(commands=["Mandar"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! O SharKey manda outro <3")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    text = """
    Olá, eu sou o SharKey, Bot da Tranca da Focus, clique em um item
     /Abrir a porta
     /Mandar o abraço pro SharKey
    """
    bot.send_message(mensagem.chat.id, text)


bot.polling()
