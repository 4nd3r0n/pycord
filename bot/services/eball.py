from translate import Translator
import requests

def eball() -> str:
    try:
        result = requests.get('https://www.eightballapi.com/api?question=&lucky=false')
        if result.status_code == 200:
            trans = Translator(to_lang='es')
            return trans.translate(result.json()['reading'])
        else:
            return 'Not Found'

    except Exception as e:
        from colorama import Fore
        print(f'[{Fore.RED}ERROR{Fore.RESET}] {e}')
        return str(e)
