import configparser

from pydantic import BaseSettings


class Settings(BaseSettings):
    user: str
    db_type: str = 'sqlite'
    db_name: str
    db_password: str
    port: int


def load_settings_from_file(file) -> Settings:
    config = configparser.ConfigParser()
    config.read(file)

    return Settings(
        user=config["Main"]["user"],
        db_name=config["Database"]["database"],
        db_password=config["Database"]["password"],
        port=config["Database"]["port"]
    )
