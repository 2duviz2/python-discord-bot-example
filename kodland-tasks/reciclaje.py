import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
    await bot.change_presence(activity=discord.Game(">help para ayuda!"))

@bot.command()
async def help(ctx):
    await ctx.send("comandos!\n**>help**\n**>donar**\n**>consejo**\n**>articulo**")
    
@bot.command()
async def consejo(ctx):
    consejos = [
        'Recuerda apagar las luces cuando no las necesites para ahorrar energía.',
        'Utiliza transporte público o comparte coche para reducir la contaminación del aire.',
        'Evita el uso de plásticos de un solo uso y opta por alternativas reutilizables.',
        'Planta árboles en tu comunidad para ayudar a combatir el cambio climático.',
        'Reduce tu consumo de agua cerrando el grifo mientras te cepillas los dientes o lavas los platos.',
        'Recicla tus residuos correctamente para minimizar el impacto ambiental.',
        'Compra productos locales y de temporada para reducir la huella de carbono del transporte.',
        'Ahorra papel imprimiendo solo cuando sea necesario y utiliza papel reciclado.',
        'Participa en actividades de limpieza comunitaria para mantener el medio ambiente limpio.',
        'Informa a otras personas sobre la importancia de cuidar el medio ambiente y cómo pueden contribuir.'
    ]
    consejo_aleatorio = random.choice(consejos)
    await ctx.send(consejo_aleatorio)
    
@bot.command()
async def donar(ctx):
    await ctx.send("https://teamseas.org")

@bot.command()
async def articulo(ctx):
    sitios_web = [
        'https://www.elagoradiario.com/desarrollo-sostenible/economia-circular/residuos-plasticos-triplicaran-2060-ocde/',
        'https://www.ecolatras.es/blog/reciclaje/como-reciclar-todo-en-casa',
        'https://elpais.com/clima-y-medio-ambiente/2023-05-16/reutilizacion-impuestos-y-freno-a-los-envases-de-un-solo-uso-la-propuesta-de-la-onu-para-reducir-un-80-la-contaminacion-por-plastico-para-2040.html'
    ]
    sitio_web_aleatorio = random.choice(sitios_web)
    await ctx.send(sitio_web_aleatorio)

bot.run('token mega secreto')
