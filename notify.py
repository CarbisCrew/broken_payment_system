class Notify:
    def __init__(self, message: str) -> None:
        self.__message__ = message
    
    def sms_send(self):
        print(f"{self.__message__}")
