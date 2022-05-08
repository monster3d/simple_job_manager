from config import Config

class Task:
    def __init__(self, config: Config):
        self.config = config

    async def start(self):
        raise NotImplementedError