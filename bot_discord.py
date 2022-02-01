import discord
import datetime
import requests
from discord.ext import commands, tasks

#video2 - requisicoes, pv message https://www.youtube.com/watch?v=YWdchyTqt5I

bot = commands.Bot("!")

@bot.event
async def on_ready():
        current_time.start()
        print(f"Estou Pronto! {bot.user}")

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return;

        if "OS" in message.content:
            await message.channel.send(f"{message.author.name}, Ordem de serviço copiada!")
        await bot.process_commands(message)

@bot.command(name="oi")
async def mandar_oi(ctx):
        name = ctx.author.name

        resposta = "Olá, " + name

        await ctx.send(resposta)



@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y ás %H:%M:%S")

    channel = bot.get_channel(938058406621741066)

    await channel.send("Data atual: " + now)
current_time.start()
bot.run("OTM4MDM1Nzk5MDE3MDA5MTkz.Yfkb6g.998TPyEpKGQ5bbJ8imP0KzSOuaE")