import telebot
from datetime import datetime as dt

key = "" #here you can type your token api
bot = telebot.TeleBot(key)

@bot.message_handler(commands = ["Abrir"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Vou verificar se você tem a senha")

    with open("BD.txt", "r") as arquivo:
        teste = arquivo.readlines()

    aut = False
    for linha in teste:
        linha = linha[:-1]
        if str(mensagem.from_user.id) == linha:
            aut = True

    if aut:
        data = dt.now()
        #here is recommended to manipulate the "data" using the day, month or something like that

        bot.send_message(mensagem.chat.id, data)
    else:
        bot.send_message(mensagem.chat.id, "Nao abre")

@bot.message_handler(commands = ["Mandar"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! O SharKey manda outro <3")

def verificar(mensagem):
    return True

@bot.message_handler(func = verificar)
def responder(mensagem):
    texto = """
    Olá, eu sou o SharKey, Bot da Tranca da Focus, clique em um item
     /Abrir a porta
     /Mandar o abraço pro SharKey
    """
    bot.send_message(mensagem.chat.id, texto)

bot.polling ()