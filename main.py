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
        a = 1
        cauhoi={
                  "1":{"Tên Đầu Tiên Bác Hồ Là G:"
                      +"\n"+"1.Nguyễn Sinh Cung"
                  +"\n"+"2.Nguyễn Sinh Côn"
                  +"\n"+"3.Nguyễn Tất Thành"
                  +"\n"+"4.Nguyễn Văn Thành"
                    :{'1'}},

                  "2":{"Khi Code Web Code Trên Gì ? :"
                      +"\n"+"1.html"
                  +"\n"+"2.Css"
                  +"\n"+"3.Js"
                  +"\n"+"4.C++" 
                          :{'1'}},

                  "3":{"trong oop muốn kết thừa methord làm sao?"
                      +"\n"+"1.super"
                  +"\n"+"2.extends"
                  +"\n"+"3.Ép kiểu object "
                  +"\n"+"4.Constructor " 
                      :{'1'}},

                  "4":{"Liên Kết Đơn gồm gì ? :"
                      +"\n"+"1.data next"
                  +"\n"+"2.pre data next"
                  +"\n"+"3.data"
                  +"\n"+"4.next pre" 
                          :{'1'}},

                  "5":{"2 số cuối của 100^15 là bao nhiêu :"
                      +"\n"+"1. 00"
                  +"\n"+"2. 20"
                  +"\n"+"3. 40"
                  +"\n"+"4. 60" 
                          :{'1'}},

                  "6":{"Nguyên Hàm của sin(x) :"
                      +"\n"+"1. cos(x)"
                  +"\n"+"2. 1/sin(x)"
                  +"\n"+"3. -1/con(x)"
                  +"\n"+"4.-cot(x)*sin(x)" 
                          :{'4'}},
                "7":{"Nguyên Hàm của Cos(x) :"
                      +"\n"+"1. cos(x)"
                  +"\n"+"2. 1/sin(x)"
                  +"\n"+"3. -1/con(x)"
                  +"\n"+"4.-cot(x)*sin(x)" 
                          :{'4'}},
                "8":{"Địa danh Đắk Tô với những trận đánh nổi tiếng trong kháng chiến chống Mỹ thuộc tỉnh nào của khu vực Tây Nguyên? :"
                    +"\n"+"1.Đắk Lắk"
                    +"\n"+"2.Gia Lai"
                    +"\n"+"3.Kon Tum"
                    +"\n"+"4.Đắk Nông" 
                      :{'3'}},   
                "9":{"Đâu là tên một loại bánh nổi tiếng ở Huế? :"
                      +"\n"+"1.Khoái"
                  +"\n"+"2. Thích"
                  +"\n"+"3. Vui"
                  +"\n"+"4. Sướng" 
                          :{'1'}},		
                "10":{"Bộ phim Chị Dậu được chuyển thể từ tác phẩm nào? :"
                      +"\n"+"1.Người mẹ cầm súng"
                  +"\n"+"2. Tắt đèn"
                  +"\n"+"3.Vợ chồng A Phủ"
                  +"\n"+"4.Tuổi thơ dữ dội" 
                          :{'2'}},
                "11":{"Cho tới thời điểm hiện nay, vườn quốc gia nào của nước ta chưa được công nhận là Vườn Di sản ASEAN? :"
                      +"\n"+"1.Vườn quốc gia Kon Ka Kinh"
                  +"\n"+"2. Vườn quốc gia Chư Mom Ray"
                  +"\n"+"3.Vườn quốc gia Tam Đảo"
                  +"\n"+"4.Vườn quốc gia Bái Tử Long" 
                          :{'3'}},	
                "12":{"Hoa hậu Hòa bình Quốc tế 2017 dự kiến sẽ được tổ chức tại quốc gia nào?:"
                      +"\n"+"1. Thái Lan"
                  +"\n"+"2. Việt Nam"
                  +"\n"+"3. Lào"
                  +"\n"+"4.Campuchia" 
                          :{'2'}},
                "13":{"Hoa hậu Hòa bình Quốc tế 2017 dự kiến sẽ được tổ chức tại quốc gia nào?:"
                      +"\n"+"1. Thái Lan"
                  +"\n"+"2. Việt Nam"
                  +"\n"+"3. Lào"
                  +"\n"+"4.Campuchia" 
                          :{'2'}},
                "14":{"Bệnh gì bác sỹ bó tay?:"
                      +"\n"+"1. chết"
                  +"\n"+"2.đau tim"
                  +"\n"+"3.chết não"
                  +"\n"+"4.gãy tay" 
                          :{'4'}},
                "15":{"Trong harry potter ai đẹp nhất?:"
                      +"\n"+"1.Oliver Wood"
                  +"\n"+"2.Draco Malfoy"
                  +"\n"+"3.Hermione Granger"
                  +"\n"+"4.Luna" 
                          :{'4'}},
                "16":{"Ai là Nhân Vật Lynn ghét nhất?:"
                      +"\n"+"1.James Potter"
                  +"\n"+"2.Draco Malfoy"
                  +"\n"+"3.Tom Riddle"
                  +"\n"+"4.Ron Weasley" 
                          :{'4'}},
                "17":{"Ai Xứng đáng làm nyc của Zuker?:"
                      +"\n"+"1.hermione granger"
                  +"\n"+"2.Draco Malfoy"
                  +"\n"+"3.Tom Riddle"
                  +"\n"+"4.Ron Weasley" 
                          :{'4'}},	
                "18":{"Ai Xứng đáng làm nyc của Zuker?:"
                      +"\n"+"1.hermione granger"
                  +"\n"+"2.Draco Malfoy"
                  +"\n"+"3.Tom Riddle"
                  +"\n"+"4.Ron Weasley" 
                          :{'4'}},
                "19":{"Trong NaruTo Ai đáng Thương nhất?:"
                      +"\n"+"1.madara"
                  +"\n"+"2.obito"
                  +"\n"+"3.naruto"
                  +"\n"+"4.pain" 
                          :{'2'}},
                "20":{"Trong NaruTo Ai đáng Ghét nhất?:"
                      +"\n"+"1.sakura"
                  +"\n"+"2.madara"
                  +"\n"+"3.sasuke"
                  +"\n"+"4.naruto" 
                          :{'1'}},					
              }
        while True:
            i=random.randint(1,20)
            if str(i) not in cauhoi:
                continue
            else:
                await ctx.send('-----câu '+str(a)+'---------')
                for x in cauhoi[str(i)].keys():
                    await ctx.send(x)   

                    await ctx.send('Đáp Án !',components=[Select(
                        placeholder='Chọn ! ',
                        options =[
                        SelectOption(label ='1',value='1'),
                        SelectOption(label ='2',value='2'),
                        SelectOption(label ='3',value='3'),
                        SelectOption(label ='4',value='4'),
                        ],
                        custom_id='selectTesting'
                    )])
                    interaction = await bot.wait_for("select_option", check = lambda i: i.custom_id=='selectTesting')
                    for x in cauhoi[str(i)].values():
                        if str('{\''+interaction.values[0]+'\'}') == str(x) :
                            await ctx.send(f"Ê {interaction.author} GIỎI !!!!")
                            a= a+1
                            del cauhoi[str(i)]
                        else:
                            await ctx.send(f"LỒN {interaction.author} NGU NHƯ CẶC VẬY")
                            await asyncio.sleep(int(2))
                            await ctx.channel.purge(limit=a*4)
                            await ctx.send(f"THẰNG GÀ {interaction.author} TRẢ LỜI ĐC {a-1} Câu !")
                            return
    @bot.command()
    async def dktuoilon(ctx):
        await ctx.send("DK CÓ TUỔI NHƯNG TUỔI LỒN !\n"*55)
    @bot.command()
    async def clear(ctx):
        await ctx.channel.purge(limit=100)    
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
                      '10. $ailatrieuphu\n'
                      '11. $clear\n'
                      '12. $dktuoilon {name}\n'
                      '13. $unmute {name}\n'),

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
    
    bot.run(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    main()
