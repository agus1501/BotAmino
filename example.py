from BotAmino import BotAmino

print("wait...")
client = BotAmino("anamdap@hotmail.com", "agus1501ytt")


@client.command("hola")
def hola(data):
    data.subClient.send_message(data.chatId, message="Hola!!")

@client.command("chau")
def chau(data):
    data.subClient.send_message(data.chatId, message="Chau!!")

@client.command("feo")
def feo(data):
    data.subClient.send_message(data.chatId, message="Tonto")    

client.launch()
print("Listo")
