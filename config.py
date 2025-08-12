from typing import Self
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel, field_validator
from enum import Enum

BASE_DIR = Path(__file__).resolve().parent


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath

    @field_validator("image_png_file", mode="before")
    def resolve_relative(cls, v):
        return BASE_DIR / Path(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )
    app_url: HttpUrl
    headless: bool = False
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    @classmethod
    def initialize_settings(cls) -> Self:
        videos_dir = DirectoryPath(BASE_DIR / "videos")
        tracing_dir = DirectoryPath(BASE_DIR / "tracing")
        browser_state_file = FilePath(BASE_DIR / "browser-state.json")

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(videos_dir=videos_dir,
                        tracing_dir=tracing_dir,
                        browser_state_file=browser_state_file)

    def get_base_url(self) -> str:
        return f"{self.app_url}/"


settings = Settings.initialize_settings()
