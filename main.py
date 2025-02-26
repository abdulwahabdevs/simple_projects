import pygame
from pygame.font import Font
from pygame.time import Clock
import random
import sys


class DodgySquare:
    def __init__(self):
        # Pygame
        pygame.init()

        # Screen
        self.screen_width, self.screen_height = 600, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Dodgy Square by Abdulwahab')

        # Colours
        self.WHITE: tuple = (255, 255, 255)
        self.BLACK: tuple = (0, 0, 0)
        self.RED: tuple = (255, 0, 0)
        self.GREEN: tuple = (0, 255, 0)
        self.BLUE: tuple = (0, 0, 255)
        self.YELLOW: tuple = (255, 255, 0)
        self.LIGHTBLUE: tuple = (0, 255, 255)

        # Font
        self.default_font: str = pygame.font.get_default_font()
        self.font: Font = pygame.font.Font(self.default_font, 26)

        # Player
        self.player_size: int = 30
        self.player_pos: list[int] = [0, 0]

        # Enemies
        self.enemy_size: int = 50
        self.enemy_pos: list[int] = []
        self.enemy_list = []
        self.enemy_speed: float  = 3 # low = slow, high = fast
        self.enemy_frequency: int = 20 # low > lots of enemies, high > few enemies

        # Clock
        self.clock: Clock = pygame.time.Clock()

        # Game data
        self.game_over: bool = False
        self.score: int = 0
        self.frame_count: int = 0
        self.score_record: int = 0

    def create_enemy(self):
        """ Creates a new enemy at a random position """

        enemy_pos: list[int] = [random.randint(0, self.screen_width - self.enemy_size), -self.enemy_size]
        self.enemy_list.append(enemy_pos)

    # Function to update enemy positions
    def update_enemy_position(self):
        """Check whether it is time to create a new enemy and then does so"""

        if self.frame_count % self.enemy_frequency == 0:
            self.create_enemy()

        # Give each enemy an id
        for idx, enemy_pos in enumerate(self.enemy_list):
            if -self.enemy_size <= enemy_pos[1] < self.screen_height:
                enemy_pos[1] += self.enemy_speed
            else:
                # when the enemy passed the line
                self.enemy_list.pop(idx)
                self.score += 1
                self.enemy_speed += 0.1

                # Increase the difficulty each 15 points
                if self.enemy_frequency > 10:
                    if self.score % 15 == 0:
                        self.enemy_frequency -= 2

    def detect_collision(self, player_pos: list[int], enemy_pos: list[int]) -> bool:
        """Collision detection logic for checking if squares are intercepting"""

        px, py = player_pos
        ex, ey = enemy_pos

        if (px <= ex < (px + self.player_size)) or (ex <= px < (ex + self.enemy_size)):
            if (py <= ey < (py + self.player_size)) or (ey <= py < (ey + self.enemy_size)):
                return True
        return False

    # Game over text
    def show_game_over(self):
        """ Display game-over and restart text"""

        # Create the text
        game_over_text = self.font.render('GAME OVER', True, self.WHITE)
        restart_text = self.font.render('Press "r" to restart', True, self.WHITE)

        # Make sure the text is centered
        text_width, text_height = game_over_text.get_size()
        restart_width, restart_height = restart_text.get_size()
        coordinates: tuple = (self.screen_width // 2 - text_width // 2, self.screen_height // 2 - text_height // 2)
        restart_coord: tuple = (self.screen_width // 2 - text_width // 2 -30, (self.screen_height // 2 + 30)- text_height // 2)
        self.screen.blit(game_over_text, coordinates)
        self.screen.blit(restart_text, restart_coord)


    # Function to replay the game
    def replay_game(self):
        """ Reset everything to its initial state"""

        # reset enemies
        self.enemy_list = []
        self.enemy_speed: float = 3
        self.enemy_frequency: int = 20

        # reset game stats
        self.game_over: bool = False
        self.score: int = 0
        self.frame_count: int = 0

    def draw_character(self, color: tuple, position: list[int], size: int):
        """Draws rectangle on the screen"""

        pygame.draw.rect(self.screen, color, (position[0], position[1], size, size))


    # Main game loop
    def run(self):
        """Run the game"""

        pygame.mouse.set_visible(False)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle key events
                if event.type == pygame.KEYDOWN:
                    if self.game_over and event.key == pygame.K_r:
                        self.replay_game()

                # get mouse current position
                mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

                # update the player position to follow the mouse
                self.player_pos[0] = mouse_pos[0] - self.player_size // 2
                self.player_pos[1] = mouse_pos[1] - self.player_size // 2

                # make sure the player stays on the screen
                self.player_pos[0] = max(0, min(self.player_pos[0], self.screen_width - self.player_size))
                self.player_pos[1] = max(0, min(self.player_pos[1], self.screen_height - self.player_size))

            if not self.game_over:
                self.update_enemy_position()

                # check for collisions
                for enemy_pos in self.enemy_list:
                    if self.detect_collision(self.player_pos, enemy_pos):
                        self.game_over = True
                        break

                # reset everything for the next frame
                self.screen.fill(self.BLACK)

                # draw the player
                self.draw_character(self.WHITE, self.player_pos, self.player_size)

                # draw the enemy
                for enemy_pos in self.enemy_list:
                    if self.score > 100:
                        self.draw_character(self.BLUE, enemy_pos, self.enemy_size)
                    else:
                        self.draw_character(self.GREEN, enemy_pos, self.enemy_size)

                # display the score
                score_text = self.font.render(f'Score: {self.score}', True, self.YELLOW)
                self.screen.blit(score_text, [10, 35])

                # display the record
                score_record_text = self.font.render(f'Record: {self.score_record}', True, self.YELLOW)
                self.screen.blit(score_record_text, [10, 10])

                # Increment the frame count
                self.frame_count += 1
            else:
                if self.score_record < self.score:
                    self.score_record = self.score
                self.show_game_over()

            pygame.display.update()
            self.clock.tick(60)

    def main_menu(self):
        """Main menu"""

        pygame.mouse.set_visible(True)
        while True:
            self.screen.fill(self.LIGHTBLUE)
            main_menu_text = self.font.render('Main Menu', True, self.BLACK)
            self.screen.blit(main_menu_text, [230, 100])

            mx, my = pygame.mouse.get_pos()

            # Creating buttons
            play_button = pygame.Rect(200, 160, 200, 50)
            exit_button = pygame.Rect(200, 240, 200, 50)

            # Handling buttons
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(mx, my):
                        self.run()

                    if exit_button.collidepoint(mx, my):
                        pygame.quit()
                        sys.exit()

            # drawing buttons
            pygame.draw.rect(self.screen, (255, 0, 0), play_button)
            pygame.draw.rect(self.screen, (255, 0, 0), exit_button)

            # writing on buttons
            play_text = self.font.render('Play', True, (255, 255, 255))
            self.screen.blit(play_text, [270, 175])
            exit_text = self.font.render('Exit', True, (255, 255, 255))
            self.screen.blit(exit_text, [270, 255])


            pygame.display.update()
            self.clock.tick(60)





if __name__ == '__main__':
    game = DodgySquare()
    game.main_menu()




