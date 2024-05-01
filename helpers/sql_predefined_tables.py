def get_table(table_name: str):
    if table_name == "dt_settings":
        return dt_settings()
    elif table_name == "dt_discord_users":
        return dt_discord_users()


def dt_settings():
    return """
    CREATE TABLE IF NOT EXISTS dt_settings (
                oid INT AUTO_INCREMENT PRIMARY KEY,
                option_name TINYTEXT NULL,
                option_value BIT NULL
            ) COMMENT='DiscordTorrent Settings Table (feel free to change if you know what you are doing)'
             COLLATE=utf8_bin"""


def dt_discord_users():
    return """
    create table dt_discord_users
(
    uid        int auto_increment,
    discord_id int         not null,
    passkey    varchar(35) not null,
    constraint dt_discord_users_pk
        primary key (uid)
)
    comment 'Discord users and authenticated keys' collate = utf8_bin;
    """
