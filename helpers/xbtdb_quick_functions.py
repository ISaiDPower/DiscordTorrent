import mysql.connector.cursor
import mysql.connector

import helpers.sql_predefined_tables
from helpers.console_print import *
from helpers.misc_functions import suicide


def check_exists(table_name: str, xbt_cursor: mysql.connector.cursor.MySQLCursorAbstract):
    xbt_cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return xbt_cursor.fetchone() is not None


def check_and_create(table_name: str, xbt_cursor: mysql.connector.cursor.MySQLCursorAbstract):
    if not check_exists(table_name, xbt_cursor):
        print_warn(f"The '{table_name}' table is not present in the database, creating it now...")
        try:
            xbt_cursor.execute(helpers.sql_predefined_tables.get_table(table_name))
        except mysql.connector.Error:
            print_error(F"Could not create the {table_name} table, killing myself...")
            suicide()
        print_success(f"The table was created successfully! ({table_name})", )
    else:
        print_info(f"{table_name} is present in the database")


def get_table_size(table_name: str, xbt_cursor: mysql.connector.cursor.MySQLCursorAbstract) -> int:
    xbt_cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    num_rows: int = int(xbt_cursor.fetchone()[0])
    return num_rows
