"""`/ping`

Action
    send_message
        Send message -> then edit with delay between interaction and response
"""
# MUST HAVE
import os
from data import Ids
from sty import ef, fg, rs
from src.logger import logger

import discord
from discord import app_commands
from discord.ext import commands

# OTHER
from datetime import datetime, timedelta


"""
Cog class
"""
class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
        logger(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {}'.format(command_name))

    # Command decorator
    @app_commands.command(name="ping", description="Renvoi le délai de Quantum entre les messages et réponses")

    # Command definition
    async def ping(self, interaction: discord.Interaction):
        if not interaction.channel_id in Ids.bot_channels: # Check if bot in right channel
            return

        # Core command code
        first = datetime.now().timestamp()
        await interaction.response.send_message(":hourglass: Loading...")
        second = datetime.now().timestamp()
        third = interaction.created_at.timestamp()#replace(tzinfo=None)# + timedelta(hours=1)
        delay = round((second - first)*1000,2)
        delay2 = round((third - first)*1000,1)
        await interaction.edit_original_response(content="Discord Bot ⇒ `{}ms`\nDiscord Websocket ⇒ `{}ms`".format(delay2, delay))


"""
Cog class
"""
async def setup(bot):
    await bot.add_cog(Ping(bot), guilds=[discord.Object(id=Ids.guild_main)])