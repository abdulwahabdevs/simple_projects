from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    phrases: list[str] = ['Welcome to this page!','You look good today!', 'The weather seems nice!']
    return {
        'phrase': choice(phrases),
        'date': datetime.now()
    }

@app.route('/api/random')
def random():
    number_input = request.args.get('number', type=int)
    text_input = request.args.get('text', type=str, default='default_text')

    if isinstance(number_input, int):
        return {
            'number': number_input,
            'random': randint(0, number_input),
            'text': text_input,
            'date': datetime.now()
        }
    else:
        return {'Error': 'Please enter valid number.'}
if __name__ == '__main__':
    app.run(debug=True)
