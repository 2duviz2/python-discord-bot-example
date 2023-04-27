import discord
from bot_logic import gen_pass
import random
from settings import settings

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

tempnumber = 0

prefix = str(settings["default-prefix"])


@client.event
async def on_ready():
    global prefix
    print(f'Hemos iniciado sesión como {client.user}')
    # Setting `Playing ` status
    await client.change_presence(activity=discord.Game(name=prefix+"help para ayuda!"))

    # Setting `Streaming ` status
    #await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

    # Setting `Listening ` status
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

    # Setting `Watching ` status
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

@client.event
async def on_message(message):
    global prefix
    if message.author == client.user:
        return
    
    if message.content.startswith(prefix+'hola'):
        await message.channel.send("Hola!")

    elif message.content.startswith(prefix+'adios'):
        await message.channel.send(":moyai:")

    elif message.content.startswith(prefix+'genpass '):
        tempnumber =   message.content.replace(prefix+"genpass ", "")
        if tempnumber.isnumeric() == False or int(tempnumber) > 1000:
            await message.channel.send("Eso es un numero muy grande o no escribiste un numero!")
        else:
            await message.channel.send(gen_pass(int(tempnumber)))

    elif message.content.startswith(prefix+'random '):
        tempnumber =   message.content.replace(prefix+"random ", "")
        if tempnumber.isnumeric() == False or int(tempnumber) > 1000:
            await message.channel.send("Eso es un numero muy grande o no escribiste un numero!")
        else:
            await message.channel.send(random.randint(0, int(tempnumber)))

    elif message.content.startswith(prefix+'help'):
        await message.channel.send("**Parece que necesitas ayuda**\n**-hola** * te saludo *\n**-adios** * bye bye *\n**-genpass (numero)** * genera una contraseña con el numero de caracteres que escribiste *\n**-random (numero)** * genera un numero del 0 a tu numero *")

    elif message.content.startswith(prefix+'ahelp') and str(message.author) == "Usuario#0000":
        await message.channel.send("**AAyuda**\n**-prefixset (prefix)**")

    elif message.content.startswith(prefix+'prefixset ') and str(message.author) == "Usuario#0000":
        tempnumber = message.content.replace(prefix+"prefixset ", "")
        prefix = str(tempnumber)
        await message.channel.send("El prefix ahora es " + str(prefix))
        await client.change_presence(activity=discord.Game(name=prefix+"help para ayuda!"))



    # else:
        # await message.channel.send(message.content)

client.run(settings["token"])
