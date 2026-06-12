# ┌──────────────────────────────────────────────────┐
# │ SysCLI v0.0.1                                    │
# │ Author: waasaty                                  │
# │ Repo:  https://github.com/waasaty/SysCLI         │
# └──────────────────────────────────────────────────┘

# LIBS
from colorama import Fore, Style, init
import getpass
from datetime import datetime

init(autoreset=True)    

# COLORS
SysCLI_C_PRIMARY = Fore.CYAN
SysCLI_C_MUTED = Fore.LIGHTBLACK_EX
SysCLI_C_OK = Fore.GREEN
SysCLI_C_ERR = Fore.RED
SysCLI_C_WARN = Fore.YELLOW
SysCLI_C_DBG = Fore.MAGENTA

# VARIABLES
SysCLI_pc_username = getpass.getuser()
SysCLI_program_name = "SysCLI"

# CONFIG
class Config:
    def program_name(name: str) -> None:
        global SysCLI_program_name
        SysCLI_program_name = name


### FUNCTIONS
# -------------------------
# inputs
# -------------------------

def input_start_header() -> None:
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(
        f'{SysCLI_C_PRIMARY}╭─{Style.RESET_ALL} '
        f'{Style.BRIGHT}{SysCLI_pc_username}{Style.RESET_ALL}'
        f'{SysCLI_C_MUTED}@{Style.RESET_ALL}'
        f'{SysCLI_C_PRIMARY}{Style.BRIGHT}{SysCLI_program_name}{Style.RESET_ALL}'
        f' {SysCLI_C_MUTED}[{timestamp}]{Style.RESET_ALL}'
    )


def input_middle(message: str) -> str:
    return input(f'{SysCLI_C_PRIMARY}├─❯{Style.RESET_ALL} {message}: ')


def input_bottom(message: str) -> str:
    return input(f'{SysCLI_C_PRIMARY}╰─❯{Style.RESET_ALL} {message}: ')


# -------------------------
# prints
# -------------------------

def print_info(message: str) -> None:
    print(f'{SysCLI_C_PRIMARY}[i]{Style.RESET_ALL} {message}')


def print_error(message: str) -> None:
    print(f'{SysCLI_C_ERR}[✗]{Style.RESET_ALL} {message}')


def print_succes(message: str) -> None:
    print(f'{SysCLI_C_OK}[✓]{Style.RESET_ALL} {message}')


def print_warn(message: str) -> None:
    print(f'{SysCLI_C_WARN}[!]{Style.RESET_ALL} {message}')


def print_dbg(message: str) -> None:
    print(f'{SysCLI_C_DBG}[~]{Style.RESET_ALL} {message}')


def print_option(number: int, message: str) -> str:
    return f'{SysCLI_C_PRIMARY}[{Style.BRIGHT}{number}{Style.NORMAL}]{Style.RESET_ALL} {message}'


def print_banner(text: str, color: str = SysCLI_C_PRIMARY) -> None:
    lines = text.splitlines()
    width = max(len(line) for line in lines) + 2
    print(f'{color}╭{"─" * width}╮')
    for line in lines:
        print(f'{color}│ {Style.RESET_ALL}{line.ljust(width - 1)}{color}│')
    print(f'{color}╰{"─" * width}╯{Style.RESET_ALL}')


def print_separator(length: int = 50, color: str = SysCLI_C_MUTED) -> None:
    print(f'{color}{"─" * length}{Style.RESET_ALL}')


def print_header() -> None:
    print_banner(f"{SysCLI_program_name}", color=SysCLI_C_PRIMARY)
    print()

def print_menu(title: str, options: list[str]) -> None:
    numbered = [f"{i}. {option}" for i, option in enumerate(options, start=1)]
    width = max(len(title), max(len(o) for o in numbered)) + 2

    print(f'{SysCLI_C_PRIMARY}╭{"─" * width}╮{Style.RESET_ALL}')
    print(f'{SysCLI_C_PRIMARY}│{Style.RESET_ALL} {Style.BRIGHT}{title.ljust(width - 1)}{SysCLI_C_PRIMARY}│{Style.RESET_ALL}')
    print(f'{SysCLI_C_PRIMARY}├{"─" * width}┤{Style.RESET_ALL}')

    for line in numbered:
        print(f'{SysCLI_C_PRIMARY}│{Style.RESET_ALL} {line.ljust(width - 1)}{SysCLI_C_PRIMARY}│{Style.RESET_ALL}')

    print(f'{SysCLI_C_PRIMARY}╰{"─" * width}╯{Style.RESET_ALL}')