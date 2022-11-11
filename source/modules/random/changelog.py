'''
IMPORTS
'''

import discord
from discord import app_commands
from discord.ext import commands

import os 
from sty import fg, ef, rs # Colors https://sty.mewo.dev

from source.printC import F
from source.ids import ids

import source.changelog.file1 as shortcut # Change HERE

module_name = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
command_name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]


'''
CLASS
'''

class Changelog(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(F(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {} / {}'.format(module_name,command_name)))

		
	### CUSTOMIZATION START HERE

	@app_commands.command(name="changelog",\
	description="Post le changelog de la dernière version de Quantum")
	@app_commands.checks.has_any_role(ids.role_admin)
	async def changelog(self, interaction: discord.Interaction):
		if interaction.channel_id in ids.bot_channels:
			channel_changelog = await self.bot.fetch_channel(ids.channel_changelog)
			to_send = shortcut.convert()
			await channel_changelog.send(embed=to_send)
			await interaction.response.send_message(":white_check_mark: __Message envoyé__ **->** <#{}>".format(channel_changelog.id))

	### CUSTOMIZATION START HERE


'''
COG SETUP
'''

async def setup(bot):
	await bot.add_cog(Changelog(bot), guilds=[discord.Object(id=ids.guild_main)])