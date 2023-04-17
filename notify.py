class Notify:
    def __init__(self, message: str) -> None:
        self.__message__ = message
    
    def message_send(self):
        print(f"{self.__message__}")
