#I used the [:] to make a copy of the list  

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

texts = ["Hello", "How are you", "I'm good"]
sent_texts = []

send_messages(texts[:], sent_texts)

print(texts)
print(sent_texts)