from microsoftbotframework import MsBot
from tasks import *
import os

print os.environ

bot = MsBot(port=int(os.environ['PORT']))
bot.add_process(activity_handler)
bot.run()
