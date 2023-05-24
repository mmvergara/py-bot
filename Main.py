import Bot
import dotenv
import os

dotenv.load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")

if __name__ == '__main__':
    Bot.run_discord_bot(TOKEN)