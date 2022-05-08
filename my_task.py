from task import Task

class MyTask(Task):
    async def start(self):
        print('{}:{} started'.format(self.config['name'], __class__.__name__))
        