
class Config:
    task_class = 'pipeline.Pipeline'
    task_config = {
       'kafka_consumer_config': {
           'bootstrap.servers': '127.0.0.1:9092',
           'enable.auto.commit': False,
           'auto.offset.reset': 'earliest',
           'group.id': 'app_my_pipeline_group'
       },
       'kafka_producer_config': {
           'bootstrap.servers': '127.0.0.1:9092',
       },
       'kafka_topics': ['app_my_pipeline_topic'],
       'schema_registry_url': '127.0.0.1:8081'
    }

    def get_task_class(self):
        return self.task_class

    def get_task_confg(self):
        return self.task_config
