from microsoftbotframework import MsBot
from tasks import *
import os

bot = MsBot(port=int(os.environ['PORT']))
bot.add_process(science)
bot.run()
