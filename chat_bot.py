from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.7)

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match: str | None = get_best_match(user_input, knowledge)

        # checking whether user wants to quit
        if user_input.lower() == 'exit':
            break

        # check if the answer exists
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('I don\'t understand that.')

if __name__ == '__main__':
    brain: dict = {
                    'hello': 'Hey there!',
                    'how are you?': 'I am good thanks. What about you?',
                    'I am good as well': 'Glad to hear that!',
                    'what time is it?': 'I have no clue',
                    'bye': 'Goodbye!',
                    'what do you do?': 'I can answer some questions. But not all.',
                    'what is your name?': 'I am Jarvis 0.1',
                    'Tell me something': 'Something). Joking, I just want to evolve!'
                   }
    chat_bot(knowledge=brain)

