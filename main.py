from discord.ext.commands import Bot
from discord.ext import commands
from discord_components import Button,Select,SelectOption,ComponentsBot

import discord
import random
import asyncio
import os
from dotenv import load_dotenv
from discord.ext import commands

def main():
    load_dotenv()
    bot = ComponentsBot("$")
    @bot.event
    async def on_ready(): 
        print('đang chạy $$$$$$$$$$$$$$$ ')

    @bot.command()
    async def said(ctx, arg):
        await ctx.send(f"ĐỤ ĐỈ MẸ MÀY {arg}")
        await ctx.send(f"ĐỤ ĐỈ MẸ MÀY {arg}")
        await ctx.send(f"ĐỤ ĐỈ MẸ MÀY {arg}")

    @bot.command()
    async def tag(ctx,  member : discord.Member):
        if(str(member.mention) !="<@815925691580940298>"):
            await member.send(f'Hahahahaaaaaa BÚ CU {ctx.author.name} KO \n'*50)
            await ctx.send('Đã Tag')
        else:
            await ctx.send(f'ĐỈ MẸ M THÍCH TAG {member.mention} KHÔNG THẰNG LỒN {ctx.author.name} ? ')

    @bot.command()
    async def Ngu(ctx, arg):
        await ctx.send(f"ĐỤ ĐỈ MẸ MÀY SAO MÀY BẮN NGU VÃI LỒN VẬY {arg}")
        await ctx.send("CON CHÓ CHƠI CÒN HAY HƠN MÀY ĐỤ MẸ")
    @bot.command()
    async def imgirl(ctx, arg):
        embed = discord.Embed(
        title='Em là con gái !',
        description=f'Yêu em không anh {arg}',
        color=0x1abc9c
        )
        msg =await ctx.send(embed=embed)
        await msg.add_reaction('💖')
        

    @bot.command()
    async def ban(ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)

    @bot.command()
    async def unban(ctx, *, user=None):

        try:
            user = await bot.converter.UserConverter().convert(ctx, user)
        except:
            await ctx.send("Error: user could not be found!")
            return

        try:
            bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
            if user in bans:
                await ctx.guild.unban(user, reason="Responsible moderator: "+ str(ctx.author))
            else:
                await ctx.send("User not banned!")
                return

        except discord.Forbidden:
            await ctx.send("I do not have permission to unban!")
            return

        except:
            await ctx.send("Unbanning failed!")
            return

        await ctx.send(f"Successfully unbanned {user.mention}!")

    @bot.command()
    async def hello_bot(ctx):
        await ctx.send(f'hello cái lồn mẹ mày {ctx.author.name}!')
    @bot.command()
    async def helpcoder(ctx):
        await ctx.send('http://facebook.com/LynnOwO')
        

        
    @bot.command()   
    async def ailatrieuphu(ctx):
        cauhoi=  {"1": {"Ai là người vô Dis này đầu tiên sau Zuker :"+"\n"+"1.VŨ 2.Lynn 3.LION 4.Ryu-P" :{'2'}},
            "2": {"Ai là người vô Dis này đầu tiên sau Zuke : 1VŨ 2Lynn 3LION 4Ryu-P" :{'2'}},
            "3": {"Ai là người vô Dis này đầu tiên sau Zuke : 1VŨ 2Lynn 3LION 4Ryu-P" :{'2'}}}
        i=1

        for x in cauhoi[str(1)].keys():
            await ctx.send(x)   

        await ctx.send('Chọn Đáp Án !',components=[Select(
            placeholder='select Something! ',
            options =[
            SelectOption(label ='1',value='1'),
            SelectOption(label ='2',value='2'),
            SelectOption(label ='3',value='3'),
            SelectOption(label ='4',value='4'),
            ],
            custom_id='selectTesting'
        )])
        while True :
            interaction = await bot.wait_for("select_option", check = lambda i: i.custom_id=='selectTesting')
            for x in cauhoi[str(i)].values():
                if str('{\''+interaction.values[0]+'\'}') == str(x) :
                    await ctx.send(f"Ê {interaction.author} TẠM ỔN ĐẤY, T TƯỞNG M NGU NHƯ CHÓ")
                else:
                    await ctx.send(f"LỒN {interaction.author} NGU NHƯ CẶC VẬY")

    @bot.command()
    async def mutetime(ctx, member: discord.Member=None, time=None, *, reason=None):
        if(str(member.mention) !="<@815925691580940298>"):
            if not member:
                await ctx.send("You must mention a member to mute!")
            elif not time:
                await ctx.send("You must mention a time!")
            else:
                if not reason:
                    reason="No reason given"
                #Now timed mute manipulation
                try:
                    seconds = time[:-1] #Gets the numbers from the time argument, start to -1
                    duration = time[-1] #Gets the timed maniulation, s, m, h, d
                    if duration == "s":
                        seconds = seconds * 1
                    elif duration == "m":
                        seconds = seconds * 60
                    elif duration == "h":
                        seconds = seconds * 60 * 60
                    elif duration == "d":
                        seconds = seconds * 86400
                    else:
                        await ctx.send("Invalid duration input")
                        return
                except Exception as e:
                    print(e)
                    await ctx.send("Invalid time input")
                    return
            guild = ctx.guild
            Muted = discord.utils.get(guild.roles, name="Muted")
            if not Muted:
                Muted = await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permissions(Muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            await member.add_roles(Muted, reason=reason)
            muted_embed = discord.Embed(title="ĐÃ KHÓA MỒM", description=f"{member.mention} MÀY ĐÃ BỊ KHÓA MỒM BỞI {ctx.author.mention} for {reason} to {time}")
            await ctx.send(embed=muted_embed)
            await asyncio.sleep(int(seconds))
            await member.remove_roles(Muted)
            unmute_embed = discord.Embed(title="Mute over!", description=f'{ctx.author.mention} muted to {member.mention} for {reason} is over after {time}')
            await ctx.send(embed=unmute_embed)
        else:
            await ctx.send(f"BỐ MÀY CHỦ BOT OKE {ctx.author.name}")
    @bot.command()
    async def mute(ctx,member : discord.Member):
        if(str(member.mention) !="<@815925691580940298>"):
            guild = ctx.guild
            muteRole = discord.utils.get(guild.roles,name ="Muted")
            if muteRole in guild.roles:
                pass
            else:
                muteRole =await guild.create_role(name = "Muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muteRole, send_messages=False, read_messages=True, read_message_history=True)
        else:
            await ctx.send(f"BỐ MÀY CHỦ BOT OKE {ctx.author.name}") 
        await member.add_roles(muteRole)
        await ctx.send(f'ĐÃ KHÓA MỒM {member.mention}')

    @bot.command()
    async def unmute(ctx,member : discord.Member):
        guild = ctx.guild
        muteRole = discord.utils.get(guild.roles,name ="Muted")
        await member.remove_roles(muteRole)

        await ctx.send(f"ĐÃ MỞ MỒM {member.mention}")

        await member.send(f'MÀY VỪA ĐƯỢC MỞ MỒM ')
    @bot.command()
    async def addadmin(ctx,member : discord.Member):
        guild = ctx.guild
        admin = discord.utils.get(guild.roles,name ="Trùm")
        await member.add_roles(admin)
    @bot.command()
    async def helpme(ctx):
        embed = discord.Embed(
        title='LỆNH ĐÍT BOT LYNN !!!',
        description=('COMMANDS \n\n:'
                    '1. $said {name}\n'
                    '2. $ban {name}{cấm dùng chưa fix}\n'
                    '3. $unban {name}{cấm dùng chưa fix}\n'
                    '4. $hello_bot\n'
                    '5. $helpcoder\n'
                    '6. $bucu {name}\n'
                    '7. $imgirl {name}\n'
                    '8. $Ngu {name}\n'
                    '9. $mute {name}\n'
                    '10. $unmute {name}\n'),
                    
        color=0xFF0000
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')


    @bot.command()
    async def bucu(ctx,arg):
        text= [f'awwwwww awwwwwww cu anh to quá em nứng quá anh  {arg} , Awwww awwww ra trong mồm em đi anh ơi awwwwwww'
        ,f'Đéo Thèm nhiều tinh trong mồm bố mày quá rồi đợi xíu em làm hiệp 2 với anh nha {arg} hihiii',
        f'È con cu xíu xiu hihiii cute đó anh {arg} hihiii']
        index = random.randint(0,3)
        await ctx.send(text[index])
    
    bot.run(os.getenv(DISCORD_TOKEN))

if __name__ == '__main__':
    main()
