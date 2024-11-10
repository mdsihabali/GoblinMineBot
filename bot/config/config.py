from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [3600, 7200]
    START_DELAY: list[int] = [5, 25]
    AUTO_MINING: bool = True
    AUTO_BUY_MINE: bool = True
    AUTO_UPGRADE: bool = True
    UPGRADE_MINE: bool = True
    UPGRADE_MINERS: bool = True
    UPGRADE_INVENTORY: bool = True
    UPGRADE_CART: bool = True
    MAX_CART_LEVEL: int = 3
    EXPEDITIONS: bool = False
    CUSTOM_EXPEDITION_COST: int = 10000
    MIN_EXP_DURATION: int = 360
    JOIN_TG_CHANNELS: bool = False
    REF_ID: str = '7253650410'


settings = Settings()
