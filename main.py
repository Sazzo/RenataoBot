import discord
from discord.ext import commands
import random

token = 'Njk1NjM5Mzk3OTEwOTcwNTg4.XodSgQ.PpKenVfyUNjZDz847LmAwFcPBK4'

bot = commands.Bot(command_prefix="r!")

@bot.event
async def on_ready():
  print("Logado como", bot.user.name)
  
@bot.command()
async def menu(ctx):
  await ctx.send("Menu:\n\nRenatão: R$23,90\nCoca-Cola: R$7,60\nPepsi: R$7,60 \nGuaraná: R$7,60")

@bot.command()
async def comprar(ctx, arg1):
  items = ["Pepsi", "Coca-Cola", "Guaraná", "Renatão"]
  if not arg1 in items:
    return await ctx.send("Esse item não existe no menu.")
  await ctx.send("Sucesso! Você comprou: {}".format(arg1))

@bot.command()
async def money(ctx):
  await ctx.send("Seu dinheiro atual é: {}".format(money))

@comprar.error
async def comprar_error(ctx, error):
  await ctx.send("Parece que você não informou o que quer comprar.")
bot.run(token)