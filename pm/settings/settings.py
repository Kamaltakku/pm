from pydantic import BaseSettings


class Settings(BaseSettings):
    user: str
    db_type: str = 'sqlite'
    db_name: str
    db_password: str
    port: int

    class Config:
        env_file: str = "settings.cfg"
