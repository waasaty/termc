# LIBS
from colorama import Fore, Style, init
import getpass
from datetime import datetime
import sys

init(autoreset=True)    

# COLORS
termc_C_PRIMARY = Fore.CYAN
termc_C_MUTED = Fore.LIGHTBLACK_EX
termc_C_OK = Fore.GREEN
termc_C_ERR = Fore.RED
termc_C_WARN = Fore.YELLOW
termc_C_DBG = Fore.MAGENTA

# VARIABLES
termc_pc_username = getpass.getuser()
termc_program_name = "termc"

# CONFIG
class termcConfig:
    @staticmethod
    def program_name(name: str) -> None:
        global termc_program_name
        termc_program_name = name

    @staticmethod
    def preset(name: str = "default"):
        global termc_C_PRIMARY, termc_C_MUTED, termc_C_OK, termc_C_ERR, termc_C_WARN, termc_C_DBG
        if name == "default":
            termc_C_PRIMARY = Fore.CYAN
            termc_C_MUTED = Fore.LIGHTBLACK_EX
            termc_C_OK = Fore.GREEN
            termc_C_ERR = Fore.RED
            termc_C_WARN = Fore.YELLOW
            termc_C_DBG = Fore.MAGENTA
        elif name == "ocean":
            termc_C_PRIMARY = Fore.BLUE
            termc_C_MUTED = Fore.LIGHTBLACK_EX
            termc_C_OK = Fore.LIGHTGREEN_EX
            termc_C_ERR = Fore.LIGHTRED_EX
            termc_C_WARN = Fore.LIGHTYELLOW_EX
            termc_C_DBG = Fore.LIGHTCYAN_EX
        elif name == "sunset":
            termc_C_PRIMARY = Fore.LIGHTRED_EX
            termc_C_MUTED = Fore.LIGHTBLACK_EX
            termc_C_OK = Fore.LIGHTGREEN_EX
            termc_C_ERR = Fore.RED
            termc_C_WARN = Fore.LIGHTYELLOW_EX
            termc_C_DBG = Fore.LIGHTMAGENTA_EX
        elif name == "mono":
            termc_C_PRIMARY = Fore.WHITE
            termc_C_MUTED = Fore.LIGHTBLACK_EX
            termc_C_OK = Fore.WHITE
            termc_C_ERR = Fore.LIGHTWHITE_EX
            termc_C_WARN = Fore.LIGHTBLACK_EX
            termc_C_DBG = Fore.LIGHTBLACK_EX
        else:
            print("Available presets: default, mono, ocean, sunset")


### FUNCTIONS
# -------------------------
# inputs
# -------------------------

def prompt_header() -> None:
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(
        f'{termc_C_PRIMARY}╭─{Style.RESET_ALL} '
        f'{Style.BRIGHT}{termc_pc_username}{Style.RESET_ALL}'
        f'{termc_C_MUTED}@{Style.RESET_ALL}'
        f'{termc_C_PRIMARY}{Style.BRIGHT}{termc_program_name}{Style.RESET_ALL}'
        f' {termc_C_MUTED}[{timestamp}]{Style.RESET_ALL}'
    )


def prompt_mid(message: str) -> str:
    return input(f'{termc_C_PRIMARY}├─❯{Style.RESET_ALL} {message}: ')


def prompt_bot(message: str) -> str:
    return input(f'{termc_C_PRIMARY}╰─❯{Style.RESET_ALL} {message}: ')


# -------------------------
# prints
# -------------------------

def info(message: str) -> None:
    print(f'{termc_C_PRIMARY}[i]{Style.RESET_ALL} {message}')


def error(message: str) -> None:
    print(f'{termc_C_ERR}[✗]{Style.RESET_ALL} {message}')


def success(message: str) -> None:
    print(f'{termc_C_OK}[✓]{Style.RESET_ALL} {message}')


def warn(message: str) -> None:
    print(f'{termc_C_WARN}[!]{Style.RESET_ALL} {message}')


def dbg(message: str) -> None:
    print(f'{termc_C_DBG}[~]{Style.RESET_ALL} {message}')


def option(number: int, message: str) -> str:
    return f'{termc_C_PRIMARY}[{Style.BRIGHT}{number}{Style.NORMAL}]{Style.RESET_ALL} {message}'


def banner(text: str, color: str = None) -> None:
    if color is None:
        color = termc_C_PRIMARY
    lines = text.splitlines()
    width = max(len(line) for line in lines) + 2
    print(f'{color}╭{"─" * width}╮')
    for line in lines:
        print(f'{color}│ {Style.RESET_ALL}{line.ljust(width - 1)}{color}│')
    print(f'{color}╰{"─" * width}╯{Style.RESET_ALL}')


def separator(length: int = 50, color: str = None) -> None:
    if color is None:
        color = termc_C_MUTED
    print(f'{color}{"─" * length}{Style.RESET_ALL}')


def header() -> None:
    banner(f"{termc_program_name}", color=termc_C_PRIMARY)
    print()

def menu(title: str, options: list[str]) -> None:
    numbered = [f"{i}. {option}" for i, option in enumerate(options, start=1)]
    width = max(len(title), max(len(o) for o in numbered)) + 2

    print(f'{termc_C_PRIMARY}╭{"─" * width}╮{Style.RESET_ALL}')
    print(f'{termc_C_PRIMARY}│{Style.RESET_ALL} {Style.BRIGHT}{title.ljust(width - 1)}{termc_C_PRIMARY}│{Style.RESET_ALL}')
    print(f'{termc_C_PRIMARY}├{"─" * width}┤{Style.RESET_ALL}')

    for line in numbered:
        print(f'{termc_C_PRIMARY}│{Style.RESET_ALL} {line.ljust(width - 1)}{termc_C_PRIMARY}│{Style.RESET_ALL}')

    print(f'{termc_C_PRIMARY}╰{"─" * width}╯{Style.RESET_ALL}')

def progress_bar(current: int, total: int, width: int = 30) -> None:
    filled = int(width * current / total)
    bar = "█" * filled + "░" * (width - filled)
    pct = int(100 * current / total)
    sys.stdout.write(f'\r{termc_C_PRIMARY}[{bar}] {pct}%{Style.RESET_ALL}')
    sys.stdout.flush()
    if current == total:
        print()