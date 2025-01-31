import random
import sys

# create class for our project
class RPS:
    def __init__(self):
        print("Welcome to the Rock Paper Scissors Mini Game!")

        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list = list(self.moves.keys())
        self.stats: dict = {
        'tie_counter': 0,
        'user_wins_counter': 0,
        'ai_wins_counter': 0
        }

    def play_game(self):
        user_move = input("Rock, paper, or scissors?: ").lower() # in order to avoid mistyping

        # making sure user wants to play or exit
        if user_move.lower() == 'exit':
            print(f"Overall results -> "
                  f"tie: {self.stats['tie_counter']}, "
                  f"win: {self.stats['user_wins_counter']}, "
                  f"loss: {self.stats['ai_wins_counter']}")
            print("Thanks for playing!")
            sys.exit()

        # to check if the move is valid
        if user_move not in self.valid_moves:
            print("Invalid move. Please try again.")
            return self.play_game()

        ai_move = random.choice(self.valid_moves)

        self.display(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display(self, user_move: str, ai_move: str):
        print('----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')


    def check_moves(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('It\'s a draw!')
            self.stats['tie_counter'] += 1
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
            self.stats['user_wins_counter'] += 1
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
            self.stats['user_wins_counter'] += 1
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
            self.stats['user_wins_counter'] += 1
        else:
            print('AI wins! Fatality')
            self.stats['ai_wins_counter'] += 1



if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()