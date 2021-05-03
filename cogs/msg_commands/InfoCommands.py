from discord.ext.commands import Cog
from discord.ext.commands import command, check

import datetime
from datetime import timezone
import checks
import help_messages

class InfoCommands(Cog, name='General Info Commands'):

    def __init__(self, bot):
        self.bot = bot

    @command(name="utc", description=help_messages.utc_help_msg)
    @check(checks.check_allowed_channel)
    async def utc_time_command(self, ctx):
        await ctx.channel.send(datetime.now(timezone.utc))

    @command(name="rules", description=help_messages.rules_help_msg)
    @check(checks.check_allowed_channel)
    async def rules_command(self, ctx):
        await ctx.channel.send('<#825137784112807946>')

    @command(name="website", aliases=["site"], description=help_messages.website_help_msg)
    @check(checks.check_allowed_channel)
    async def website_command(self, ctx):
        await ctx.channel.send('https://www.osrsbotdetector.com/')

    @command(name="beta", description=help_messages.beta_help_msg)
    @check(checks.check_allowed_channel)
    async def beta_command(self, ctx):
        await ctx.channel.send('https://github.com/Bot-detector/bot-detector/wiki/Running-the-Development-Version-From-Source')

    @command(name="patreon", description=help_messages.patreon_help_msg)
    @check(checks.check_allowed_channel)
    async def patreon_command(self, ctx):
        await ctx.channel.send('https://www.patreon.com/bot_detector')

    @command(name="github", description=help_messages.github_help_msg)
    @check(checks.check_allowed_channel)
    async def github_command(self, ctx, repo):
        repos = {
            "core": "https://github.com/Bot-detector/Bot-Detector-Core-Files",
            "plugin": "https://github.com/Bot-detector/bot-detector",
            "discord": "https://github.com/Bot-detector/bot-detector-discord-bot",
            "website": "https://github.com/Bot-detector/Bot-Detector-Web"
        }

        not_found_text = f"{repo} isn't a valid GitHub repository name. Try 'Core' or 'Plugin'."

        repo_url = repos.get(repo.lower(), not_found_text)

        await ctx.channel.send(repo_url)


    @command(name="invite", description=help_messages.invite_help_msg)
    @check(checks.check_allowed_channel)
    async def invite_command(self, ctx):
        await ctx.channel.send('https://discord.com/invite/JCAGpcjbfP')


    @command(name="issues", aliases=["issue"], description=help_messages.issues_help_msg)
    @check(checks.check_allowed_channel)
    async def issues_command(self, ctx):
        await ctx.channel.send('<#822851862016950282>')


def setup(bot):
    bot.add_cog(InfoCommands(bot))