from bot.config import Config
from colorama import Fore
import bot.main as bot

if __name__ == '__main__':
    try:
        bot.start_bot(Config.TOKEN)

    except Exception as e:
        print(f'[{Fore.RED}ERROR{Fore.RESET}] {e}')
