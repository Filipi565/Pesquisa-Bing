import random

def get_random_quote(word: bytes) -> str:
    items = (b"what is {}", b"{}", b"{} what means", b"{} dictionary means", b"tradu\xe7\xe3o", b"{} wiki", b"wikipedia")

    while True:
        try:
            return random.choice(items).replace(b"{}", word).decode()
        except UnicodeError:
            pass