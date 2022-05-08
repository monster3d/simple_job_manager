
class Config:
    task_class = 'my_task.MyTask'
    task_config = {
        'name': 'Long time task'
    }

    def get_task_class(self):
        return self.task_class

    def get_task_confg(self):
        return self.task_config
