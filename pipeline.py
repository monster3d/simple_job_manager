import asyncio

from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry.avro import AvroSerializer

from schema import USER_ENTITY_SCHEMA, USER_VALIDATION_SCHEMA
from entities.user import User
from entities.user_validation import UserValidation

from task import Task

class Pipeline(Task):
    kafka_consumer = None
    kafka_producer = None
    
    async def start(self):
        print('{} started'.format(self.__class__.__name__))
        self._init()

        await asyncio.sleep(1)

    def _init(self):
        def dict_to_entity(obj, ctx):
            return User(
                uuid=obj['uuid'],
                name=obj['name'], 
                email=obj['email'],
                token=obj['token']
            )

        def entity_to_dict(entity, ctx):
            return dict(
                user_uuid=entity.user_uuid,
                status=entity.status
            )

        schema_registry = SchemaRegistryClient({'url': self.config['schema_registry_url']})
        
        avro_deserializer = AvroDeserializer(schema_registry, USER_ENTITY_SCHEMA, dict_to_entity)
        avro_deserializer_settings = {
            'key.deserializer': StringDeserializer('utf_8'),
            'value.deserializer': avro_deserializer,
        }

        consumer_config = self.config['kafka_consumer_config']
        consumer_config.update(avro_deserializer_settings)

        self.kafka_consumer =  DeserializingConsumer(consumer_config)

        avro_serializer = AvroSerializer(schema_registry, USER_VALIDATION_SCHEMA, entity_to_dict)
        avro_serializer_settings = {
            'key.serializer':  StringSerializer('utf_8'),
            'value.serializer': avro_serializer,
        }

        producer_config = self.config['kafka_producer_config']
        producer_config.update(avro_serializer_settings)

        self.kafka_producer = SerializingProducer(producer_config)
    





