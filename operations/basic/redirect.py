import webbrowser
import random


def to_official_repository():
    """redirect to official 'refer' github repository
    """
    happy_emojis = [
        "😀", "😃", "😄", "😁", "😊", "🙂", "😆", "😋",
        "🤗", "😍", "🥰", "😎", "🤩", "😺", "😸", "😹",
        "✨", "🎉", "💖", "🌈"
    ]
    webbrowser.open("https://github.com/CoderRony955/refer")
    print(random.choice(happy_emojis))
