import discord
from discord.ext import commands
import random
import json


class commandoP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Prefixos operacionais.")

    @commands.command()
    async def pergunte(self, ctx, * , questao):
        with open("C:\Git\Bot\Bot2\cogs\quack\call.txt","r") as f:
            respostas_random = f.readlines()
            resposta = random.choice(respostas_random)
        
            await ctx.send(resposta)
    @commands.command()
    async def ping(self,ctx):
        bot_latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong {bot_latency} ms.")
        
    @commands.command()
    async def agarrar(self,ctx):
        await ctx.send(f"puxei alguem pra outro chat")
        
    @commands.command()
    async def bigtal(self,ctx):
        with open("Bot\Bot2\cogs\quack\gigtal.txt","r") as f:
            respostas_random = f.readlines()
            resposta = random.choice(respostas_random)
            await ctx.send(resposta)
    @commands.command()
    async def heylle(self,ctx):
        await ctx.send(f"A pedido de Heylle, a sato foi convocada, pra quê eu n sei")
    @commands.command()
    async def xedo(self,ctx):
        await ctx.send(f"Coé <@482324660525072415>, faz o curso")
    @commands.command()
    async def decker(self,ctx):
        await ctx.send(f"para o <@646571634185994251> \n https://cdn.discordapp.com/attachments/1272065177197477969/1273042710701277235/Engineer_TF2_sings_Out_of_Touch.mp4?ex=66c272ea&is=66c1216a&hm=ac3814e3d408fd8798f58e6c4d6c87519b37b33297740bd344815fb8131e8b43&")
    @commands.command()
    async def quack(self,ctx):
        with open("Bot\Bot2\cogs\quack\pato.txt","r") as f:
            respostas_random = f.readlines()
            resposta = random.choice(respostas_random)
            await ctx.send(resposta)
            
            

        
async def setup(bot):
    await bot.add_cog(commandoP(bot))