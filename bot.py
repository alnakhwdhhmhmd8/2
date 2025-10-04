from pyrogram import Client, idle
from pyromod import listen

OWNER_ID = int(f"7728230165")
ch = "xvwwvl" 
OWNER_USERNAME = "wwvvwl"
ST = "xvwwvl"
LT = "wwvvwt"
DEVS = []
DEVS.append(OWNER_USERNAME)
DEVS.append(ST)
DEVS.append(LT)
OWNER = "جاك"

bot_token="7936597041:AAGQAHtCckYIMvWwY8NPZN8fv5yws2Q50Xw"
bot_token2="BAFF9UIAjkdInIuF2_fe1IV1HeF_3xgupMZmzmV12BDJc-WF7Mt5ZNs7NcVN1N2FqmnQxZUSGfv15ljyByb1cwObovV4-9SiTwu3WaeU-vh1FzCSW5OuV3flu-Da_4I5tlzY1hh-LR5vR0ninQ5MJuaq-3FcF9aQMR1bBPhZhwklML3Xy6cbV7RCt2CQ02gjwPTBowHu01NZPpNnudpOfI2IKz4OUB2QDizP6ja0Jhdf0VthV-S_effkYQqtp8wxFGSYdssHcQv-8hkjE5QTaolxV8vXKKBiLEHvyPqvlL-130gAECPiIQxLs0WdCht-6hRXpTVQ8EuKQnCDdhOhtAUSebctEgAAAAHMo28VAA"


bot = Client("ITA", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", session_string=bot_token2)    

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(OWNER_USERNAME, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()
