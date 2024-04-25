from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    PYTHONPATH: str

    DB_USER: SecretStr
    DB_PASS: SecretStr
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    SQLADMIN_LOGIN:       SecretStr    
    SQLADMIN_PASSWORD:    SecretStr
    SQLADMIN_SECRET_KEY:  SecretStr

    @property
    def SQLALCHEMY_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER.get_secret_value()}:{self.DB_PASS.get_secret_value()}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

env_config = EnvConfig()
