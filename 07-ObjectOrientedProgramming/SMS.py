from dc9 import Message
class SMS(Message):
    def __init__(self,sender,receiver,topic,message=' '):
        super().__init__(message)
        self.sender=sender
        self.receiver=receiver
        self.topic=topic
    def send(self):
        return f'''
                    Wysyłanie SMS...
                    Od: {self.sender}
                    Do: {self.receiver}
                    Temat: {self.topic}
                    Treść: {m1.message}'''
    
a1=SMS('Me','You','Hi')
print(a1.send())