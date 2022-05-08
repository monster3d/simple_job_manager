import asyncio
import importlib

from pipeline import Pipeline
from config import Config

class Job:    
    def __init__(self, config: Config):
        self.config = config

    async def run(self):
        task_module = importlib.import_module(self._get_task_module_name())
        task_class = self._get_task_class_name()
        task_config = self.config.get_task_confg()
        task = getattr(task_module, task_class)(task_config)

        await task.start()

    def _get_task_module_name(self):
        return self.config.get_task_class().split('.')[:-1][0]
    
    def _get_task_class_name(self):
        return self.config.get_task_class().split('.')[-1:][0]
