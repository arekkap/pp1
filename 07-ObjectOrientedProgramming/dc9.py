class Message():
    def __init__(self, message=' '):
        self.message = message
    def set_message(self,message):
        self.message = f'{message.capitalize()}' + ', Soyonara'

m1=Message()
print(m1.message)
m1.set_message('hello mate')
print(m1.message)
