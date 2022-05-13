
USER_ENTITY_SCHEMA = """
    {
        "namespace": "confluent.io.schama.avro",
        "name": "User",
        "type": "record",
        "fields": [
            {
                "name": "uuid",
                "type": "string"
            },
            {
                "name": "name", 
                "type": "string"
            },
            {
                "name": "email", 
                "type": "string"
            },
            {
                "name": "token", 
                "type": "string"
            }
        ]
    }
"""

USER_VALIDATION_SCHEMA = """
   {
        "namespace": "confluent.io.schama.avro",
        "name": "UserValidation",
        "type": "record",
        "fields": [
            {
                "name": "user_uuid",
                "type": "string"
            },
            {
                "name": "status", 
                "type": "string"
            },
        ]
    }

"""