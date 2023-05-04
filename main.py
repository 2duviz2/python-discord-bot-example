import discord
from bot_logic import gen_pass
import random
from settings import settings
import time


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

tempnumber = 0

prefix = str(settings["default-prefix"])

encurso = False


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
    global encurso
    global msg
    global prefix
    global health
    global enemyhealth
    if message.author == client.user:
        return
    

    #COMANDOS
    if message.content.startswith(prefix+'hola'):
        await message.channel.send("TETAS ALERT! <:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879><:shockface:1101812286366158879>")

    elif message.content.startswith(prefix+'adios'):
        await message.channel.send("<:miguel:1101485771350872104>")

    elif message.content.startswith(prefix+'genpass '):
        tempnumber =   message.content.replace(prefix+"genpass ", "")
        if tempnumber.isnumeric() == False or int(tempnumber) > 1000:
            await message.channel.send("Eso es un numero muy grande o no escribiste un numero <:shockface:1101812286366158879>!")
        else:
            await message.channel.send(gen_pass(int(tempnumber)))

    elif message.content.startswith(prefix+'random '):
        tempnumber =   message.content.replace(prefix+"random ", "")
        if tempnumber.isnumeric() == False or int(tempnumber) > 10000:
            await message.channel.send("Eso es un numero muy grande o no escribiste un numero <:shockface:1101812286366158879>!")
        else:
            await message.channel.send(random.randint(0, int(tempnumber)))

    elif message.content.startswith(prefix+'rpg'):
        if encurso == True:
            await message.channel.send("Hay una partida en curso <:shockface:1101812286366158879>")

        if encurso == False:
            encurso = True
            health = 200
            enemyhealth = 300
            
            msg = await message.channel.send("Que quieres hacer? Tienes "+str(health)+"HP y el enemigo tiene "+str(enemyhealth)+"HP.")
            await msg.add_reaction('⚔️')
            await msg.add_reaction('🌮')

    elif message.content.startswith(prefix+'meme'):
        rand = random.randint(1,7)
        if rand == 1:
            await message.channel.send(file=discord.File(r'C:\Users\javie\Pictures\B9ZEaPLN_400x400.jpg'))
        if rand == 2:
            await message.channel.send(file=discord.File(r'C:\Users\javie\Pictures\buho.png'))
        if rand == 3:
            await message.channel.send(file=discord.File(r'C:\Users\javie\Pictures\mujer gamer.png'))
        if rand == 4:
            await message.channel.send(file=discord.File(r'C:\Users\javie\Pictures\ssstwitter.com_1679246036930.mp4'))
        if rand == 5:
            await message.channel.send(file=discord.File(r'C:\Users\javie\Pictures\ssstwitter.com_1679425493692.mp4'))
        if rand == 6:
            await message.channel.send(file=discord.File(r'C:\Users\javie\Pictures\YOUTUBER PROMEDIO.jpeg'))
        if rand == 7:
            await message.channel.send(file=discord.File(r'C:\Users\javie\Pictures\ohio.pjpg.jpg'))

    elif message.content.startswith(prefix+'help'):
        helpmsg = "**Parece que necesitas ayuda**\n\n**-hola** * te saludo *\n\n**-adios** * bye bye *\n\n**-genpass (numero)** * genera una contraseña con el numero de caracteres que escribiste *\n\n**-random (numero)** * genera un numero del 0 a tu numero *\n\n**-rpg** * minijuego, solo puede jugar 1 a la vez pero todos pueden interactuar *\n\n**-meme** * meme random *\n\n**AVISO: ESTE BOT PUEDE CONTENER RACISMO, MACHISMO O REFERENCIAS SEXUALES!!!**"
        helpmsg = helpmsg.replace("-", str(prefix))
        await message.channel.send(helpmsg)


    #COMANDOS ADMIN
    elif message.content.startswith(prefix+'ahelp') and str(message.author) == "Duviz 2#2937":
        helpmsg = "**AAyuda (Ayuda de admin)**\n\n**-ahelp**\n\n**-prefixset (prefix)**"
        helpmsg = helpmsg.replace("-", str(prefix))
        await message.channel.send(helpmsg)

    elif message.content.startswith(prefix+'prefixset ') and str(message.author) == "Duviz 2#2937":
        tempnumber = message.content.replace(prefix+"prefixset ", "")
        prefix = str(tempnumber)
        await message.channel.send("El prefix ahora es " + str(prefix))
        await client.change_presence(activity=discord.Game(name=prefix+"help para ayuda!"))

    elif message.content.startswith(prefix+'prefixset ') and str(message.author) == "Duviz 2#2937":
        tempnumber = message.content.replace(prefix+"prefixset ", "")
        prefix = str(tempnumber)
        await message.channel.send("El prefix ahora es " + str(prefix))
        await client.change_presence(activity=discord.Game(name=prefix+"help para ayuda!"))
    #MODERACION AUTO
    msg_content = message.content.lower()

    #curseWord = ['fck', 'fuck', 'tta', 'tt4', 't3t4', 't3ta', 'tet4', 'tetas', 'puto', 'gordo', 'g0r', 'd0', 'puta', 'pute', 'put0', 'put4', 'pto', 'pta', 'pte', 'cojones','cojon', 'c0j', 'coj0', 'j0n', 'joder', 'joe', 'jod3', 'j0', '3r' 'j03', 'jo3', 'j0e', 'jod', 'j0d' ]
    #
    # delete curse word if match with the list
    #if any(word in msg_content for word in curseWord):
    #    await message.reply('No puedes decir eso <:miguel:1101485771350872104>!')
    #    await message.delete()


    # else:
        # await message.channel.send(message.content)

@client.event
async def on_reaction_add(reaction, user):
    global msg
    global health
    global enemyhealth
    if reaction.count == 1:
        return
    if health <= 0 or enemyhealth <= 0:
        return
    #Channel = client.get_channel(YOUR_CHANNEL_ID)
    #if reaction.message.channel.id != Channel.id:
    #    return
    if reaction.emoji == "⚔️" and reaction.message == msg:
      #Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
      #await user.add_roles(Role)
      #await msg.edit(content="Ok aya voy")
        quitavida = random.randint(1,8)
        muere = random.randint(1, 3)
        enemyhealth -= quitavida
        global encurso
        health -= muere
        await msg.channel.send("Golpeaste al enemigo... Le quitaste "+str(quitavida)+" de vida")
        if enemyhealth <= 0:
            await msg.channel.send("EL ENEMIGO MURIO!!!")
            msg = ""
            encurso = False
            return
        await msg.channel.send("El enemigo ataco... Perdiste "+str(muere)+" de vida")
        if health <= 0:
            await msg.channel.send("MORISTE!!!")
            msg = ""
            encurso = False
            return
        msg = await msg.channel.send("Que quieres hacer? Tienes "+str(health)+"HP y el enemigo tiene "+str(enemyhealth)+"HP.")
        await msg.add_reaction('⚔️')
        await msg.add_reaction('🌮')
    if reaction.emoji == "🌮" and reaction.message == msg:
      #Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
      #await user.add_roles(Role)
      #await msg.edit(content="Ok aya voy")
        curar = random.randint(0, 8)
        muere = random.randint(2, 3)
        health += curar
        health -= muere
        await msg.channel.send("Te curaste... Te curaste "+str(curar)+" de vida")
        await msg.channel.send("El enemigo ataco... Perdiste "+str(muere)+" de vida")
        if health <= 0:
            await msg.channel.send("MORISTE!!!")
            #await reaction.clear()
            msg = ""
            encurso = False
            return
        msg = await msg.channel.send("Que quieres hacer? Tienes "+str(health)+"HP y el enemigo tiene "+str(enemyhealth)+"HP.")
        await msg.add_reaction('⚔️')
        await msg.add_reaction('🌮')
      

client.run(settings["token"])
