from difflib import get_close_matches
import json

def get_best_matches(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]


def get_response(message: str, knowledge: dict) -> str:
    best_matches: str | None = get_best_matches(message, knowledge)

    if answer:= knowledge.get(best_matches):
        return answer
    else:
        return 'hmm. I don\'t get it. Could you rephrase it?'

def load_knowledge(file: str) -> dict:
    with open(file, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    test_knowledge = load_knowledge('knowledge.json')
    test_response = get_response('by e', knowledge=test_knowledge)
    print(test_response)

