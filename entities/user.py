class User:
    def __init__(self, uuid: str, name: str, email: str, token: str):
        self.uuid = uuid
        self.name = name
        self.email = email
        self.token = token