import pygame
import random

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 10
SQUARE_SIZE = WINDOW_WIDTH // GRID_SIZE
FPS = 30

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Snakes and Ladders positions
SNakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake and Ladder Game")
clock = pygame.time.Clock()

class Player:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.position = 0

    def move(self, roll):
        new_position = self.position + roll
        if new_position > 100:
            return False  # Cannot move
        # Move to new position
        self.position = new_position
        return True

    def check_snakes_ladders(self):
        if self.position in SNakes:
            self.position = SNakes[self.position]
        elif self.position in LADDERS:
            self.position = LADDERS[self.position]

def draw_board(players):
    # Draw the board
    screen.fill(WHITE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(j * SQUARE_SIZE, (GRID_SIZE - 1 - i) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, GREEN if (i + j) % 2 == 0 else RED, rect, 1)
            if i * GRID_SIZE + j < 100:
                font = pygame.font.Font(None, 36)
                text = font.render(str(i * GRID_SIZE + j + 1), True, WHITE)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    # Draw players
    for player in players:
        x = (player.position - 1) % GRID_SIZE
        y = GRID_SIZE - 1 - (player.position - 1) // GRID_SIZE
        pygame.draw.circle(screen, player.color, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 4)

    pygame.display.flip()

def main():
    # Game setup
    players = [Player(BLUE, "Player 1"), Player(RED, "Player 2")]
    current_player_index = 0
    running = True

    while running:
        clock.tick(FPS)
        draw_board(players)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                roll = random.randint(1, 6)
                print(f"{players[current_player_index].name} rolled a {roll}.")

                if players[current_player_index].move(roll):
                    players[current_player_index].check_snakes_ladders()
                    if players[current_player_index].position == 100:
                        print(f"{players[current_player_index].name} wins!")
                        running = False

                # Switch players
                current_player_index = (current_player_index + 1) % len(players)

    pygame.quit()

if __name__ == "__main__":
    main()
