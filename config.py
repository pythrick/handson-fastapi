from pydantic.env_settings import read_env_file


class Settings:
    class Config:
        env_file = ".env"
        env_prefix = "PYDANTIC_"

    def __init__(self):
        envs = read_env_file(self.Config.env_file)
        for k, v in envs.items():
            if k.upper().startswith(self.Config.env_prefix):
                setattr(self, k.upper().replace(self.Config.env_prefix, ""), v)


settings = Settings()
