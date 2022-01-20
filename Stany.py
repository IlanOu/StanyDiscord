import discord
from discord.ext import commands
from discord.utils import get

Prefix = "."


bot = commands.Bot(command_prefix=Prefix)
bot.remove_command('help')


#INFORMER QUE LE BOT EST CONNECTE_________________________________________________________________________________
@bot.event
async def on_ready():
    print(f"{bot.user.display_name} est connecté au serveur.")


    for guild in bot.guilds:
        for channel in guild.text_channels:
            Bots_Channel : discord.TextChannel = guild.rules_channel

    await Bots_Channel.send(content=f"{bot.user.mention} est connecté au serveur.")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{Prefix}help"))



#SOUHAITER LA BIENVENUE AUX NOUVEAUX______________________________________________________________________________
@bot.event
async def on_member_join(member):
    print("Bienvenue !")
    for guild in bot.guilds:
        for channel in guild.text_channels:
            Bots_Channel : discord.TextChannel = guild.system_channel

    await Bots_Channel.send(content=f"Bienvenue sur le serveur {member.display.mention} !")





#REACTION ROLE______________________________________________________________________________
@bot.event
async def on_reaction_add(reaction, user):
    for guild in bot.guilds:
        for channel in guild.text_channels:
            Bots_Channel : discord.TextChannel = guild.system_channel

    await Bots_Channel.send(content=f"Bienvenue sur le serveur {user.mention} !")

    if user.name != bot.user.display_name:
        channel = reaction.message.channel
        await reaction.message.channel.send(content=f"{user.name} a réagit !")





#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘#
#_ _ _ _ _ _ _ _ _ _ _ _ C O M M A N D E S _ _ _ _ _ _ _ _ _ _ _ _#
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘#




#AJOUTER UNE REACTION A UNE COMMANDE PRECISE______________________________________________________________________
@bot.command(name='yey', description="Commande de test.")
async def react(ctx):
	emoji = '😁'
	await ctx.message.add_reaction(emoji)
	emoji = '😎'
	await ctx.message.add_reaction(emoji)

@react.error
async def print_error(ctx, error):
	await ctx.message.channel.send(content=error)



#SUPPRIMER UN CERTAIN NOMBRES DE MESSAGES_________________________________________________________________________
@bot.command(name='del', description=f"Supprime le nombre de message idiqué : \n*{Prefix}del (nombre de messages).*")
@commands.has_permissions(manage_messages=True)
async def delete(ctx, number_of_messages: int):

	messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

	for each_message in messages:
		await each_message.delete()

@delete.error
async def print_error(ctx, error):
	await ctx.message.channel.send(content=error)



@bot.command(name='invites', description="Affiche le nombre d'invitations que vous avez fait.")
async def invites(ctx):

    totalInvites = 0
    for i in await ctx.message.guild.invites():
        if i.inviter == ctx.message.author:
            totalInvites += i.uses
    await ctx.message.channel.send(f"Vous avez invité {totalInvites} membre{'' if totalInvites == 1 else 's'} sur le serveur !")

@invites.error
async def print_error(ctx, error):
	await ctx.message.channel.send(content=error)





@bot.command(name='ping', description=f"Affiche la latence du bot.")
async def ping(ctx):
    await ctx.message.channel.send(content="Pong")
    await ctx.message.channel.send(content=f"{round(bot.latency, 1)}")





@bot.command(name='embed', description=f"Crée un embed personnalisé sous la forme : \n*{Prefix}embed \"Titre\" \"Description\" \"R G B\"*.")
@commands.has_permissions(administrator=True)
async def embed(ctx, title, description, colour):
    embed = discord.Embed(title = title, description = description, colour= discord.Colour.from_rgb(int(str(colour).split(" ")[0]), int(str(colour).split(" ")[1]), int(str(colour).split(" ")[2])))
    messages = await ctx.channel.history(limit=1).flatten()
    await messages[0].delete()
    EnvoiEmbed = await ctx.message.channel.send(embed=embed)

@embed.error
async def print_error(ctx, error):
	await ctx.message.channel.send(content=error)





@bot.command(name="help", description="Affiche ce message.")
async def help(ctx):
    helptext = ""

    for command in bot.commands:
        helptext+=f"{command} : {command.description}\n\n"
    #helptext+="`"
    embed = discord.Embed(title = "__Page d'aide__", description = f"**Prefix : \" {Prefix} \"**\n\n**Commandes :**\n\n\n" + helptext, colour= 0xffffff)
    EnvoiEmbed = await ctx.message.channel.send(embed=embed)
    #await ctx.send(helptext)









bot.run("OTMzMDMwMzIzNzQ5NTM5ODUy.YebmNA.fq4V0Kqs4cAtYI_f6vSxdEO-Ybs")
