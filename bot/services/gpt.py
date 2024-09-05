def gpt(message: str) -> str:
    try:
        from duckduckgo_search import DDGS
        results = DDGS().chat(message, model='claude-3-haiku')
        return results

    except Exception as e:
        from colorama.ansi import Fore
        print(f'[{Fore.RED}ERROR{Fore.RESET}]: {e}')
        return str(e)
