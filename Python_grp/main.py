import pygame
from game1 import gameLoop
from game2 import board
from game3 import game

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH = 800
HEIGHT = 600
MENU_FONT = pygame.font.Font(None, 36)

# Main Menu
def main_menu(screen):
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text(screen, "Select a Game:", (WIDTH // 2, HEIGHT // 4))
        draw_text(screen, "1. Dodge Ball", (WIDTH // 2, HEIGHT // 2 - 50))
        draw_text(screen, "2. Pong", (WIDTH // 2, HEIGHT // 2))
        draw_text(screen, "3. Space Invader", (WIDTH // 2, HEIGHT // 2 + 50)) 

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    gameLoop()
                elif event.key == pygame.K_2:
                    board()
                elif event.key == pygame.K_3:
                    game()

    pygame.quit()

# Function to draw text on the screen
def draw_text(screen, text, pos):
    text_surface = MENU_FONT.render(text, True, (255, 255, 255))
    rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, rect)

# Main Function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mini-Game Collection")

    main_menu(screen)

main()
