from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class GoHomeMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        self.readBoolean()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24101, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 17750

    def getMessageVersion(self):
        return self.messageVersion