class ProtocolHandler:
    def __init__(self, protocol:str, key: str, command: str) -> None:
        self.protocol = protocol
        self.key = key
        self.command = command