from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood('😊', polarity)
    elif polarity <= hostile_threshold:
        return Mood('😠', polarity)
    else:
        return Mood('😑', polarity)


def run_bot():
    print('Enter some text to get a sentiment response!(exit to quit)')
    while True:
        user_input: str = input('You: ')
        # to check whether user wants to quit
        if user_input.lower() == 'exit':
            break
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')

if __name__ == '__main__':
    run_bot()
