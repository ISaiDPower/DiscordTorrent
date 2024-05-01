import mysql.connector

import bot.main
import helpers.xbtdb_quick_functions
from helpers.console_print import print_warn, print_error, print_success, print_info
from colorama import Fore, init


def suicide():
    print(Fore.RED + "idk what u did, but the script actually commited suicide bro..." + Fore.RESET)
    exit()


USERS = "dt_discord_users"
SETTINGS = "dt_settings"

init(convert=True)

print_info("DiscordTorrent")
print_info("by JPN")
print_info("Fully working XBT BitTorrent tracker running on Discord.")
print_info("Starting the bot...\n")

print_info("Connecting to the database...")

# MYSQL CONFIGURATION !!!!!!!!!!!!!!!! PLEASE EDIT!!!!
xbt_db = mysql.connector.connect(
    host="localhost",  # Your MySQL database address
    user="root",  # Your MySQL username used to connect
    password="",  # The password for the user you have provided
    database="xbt",  # Database where XBT is already installed
)

if not xbt_db.is_connected():
    print_error("The connection could not be established, commiting suicide...")
    suicide()

print_success("The connection was successful!\n")
print_info("Proceeding with verifying tables and possibly creating new ones if not existing...")
print_info("If this is the first run, please ignore any warnings!")

xbt_executor = xbt_db.cursor()

# Check if tables already exists if not create them
helpers.xbtdb_quick_functions.check_and_create(SETTINGS, xbt_executor)  # Settings table
helpers.xbtdb_quick_functions.check_and_create(USERS, xbt_executor)  # Discord users and associated keys
# Leaving it like that for now, since many of the tables are managed by XBT tracker

print()
print_info("Counting tables...")
print_success(f"Loaded {helpers.xbtdb_quick_functions.get_table_size(USERS, xbt_executor)} users.")
print_success(f"Loaded {helpers.xbtdb_quick_functions.get_table_size('xbt_files', xbt_executor)} files.\n")

print_success("Bootstrap complete!")
print_info("Starting the bot...\n")
bot.main.main()
