from colorama import Fore


def print_error(message: str):
    print("[" + Fore.RED + "ERROR" + Fore.RESET + "] " + message)


def print_warn(message: str):
    print("[" + Fore.YELLOW + "WARN" + Fore.RESET + "] " + message)


def print_success(message: str):
    print("[" + Fore.GREEN + "SUCCESS" + Fore.RESET + "] " + message)


def print_info(message: str):
    print("[" + Fore.CYAN + "INFO" + Fore.RESET + "] " + message)
