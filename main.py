import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")


@bot.group()
async def afk(ctx):
    pass


@afk.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("Kamu harus berada di voice channel.")
        return

    channel = ctx.author.voice.channel
    vc = await channel.connect()
    await vc.guild.change_voice_state(channel=channel, self_mute=True, self_deaf=True)
    await ctx.send(f"Bergabung ke **{channel.name}** dan diam di sini 24/7.")


@afk.command()
async def leave(ctx):
    if ctx.voice_client is None:
        await ctx.send("Bot tidak sedang di voice channel.")
        return

    await ctx.voice_client.disconnect()
    await ctx.send("Bot keluar dari voice channel.")


bot.run(TOKEN)
