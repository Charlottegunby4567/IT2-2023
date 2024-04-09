import pygame
import sys
import random

# Initialiserer Pygame
pygame.init()

# Definerer konstanter
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 60

# Initialiserer poeng og liv
score = 0
lives = 3

# Lager vinduet
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gjett bildet!")

# Laster inn bildet
image = pygame.image.load("bilde.jpg")
image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Definerer riktige svar
correct_answers = ["honning"]

# Funksjon for å vise deler av bildet
def show_partial_image():
    x = (SCREEN_WIDTH - image.get_width()) / 2
    y = (SCREEN_HEIGHT - image.get_height()) / 2
    screen.blit(image, (x, y))

# Funksjon for å tegne poeng
def draw_score():
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, RED)
    screen.blit(text, (10, 10))

# Funksjon for å tegne gjetteboksen
def draw_guess_box():
    font = pygame.font.Font(None, 36)
    text = font.render("Gjett ordet:", True, BLACK)
    screen.blit(text, (10, SCREEN_HEIGHT - 50))
    pygame.draw.rect(screen, WHITE, (150, SCREEN_HEIGHT - 70, 300, 30), 2)

# Funksjon for å sjekke svaret
def check_answer(answer):
    global score, lives
    if answer.lower() in correct_answers:
        score += 1
    else:
        lives -= 1

# Funksjon for å starte spillet
def start_game():
    global score, lives
    score = 0
    lives = 3
    main()

# Funksjon for hovedspill-loopen
def main():
    clock = pygame.time.Clock()
    game_started = False

    running = True
    while running:
        screen.fill(WHITE)
        
        if not game_started:
            draw_score()
        
        else:
            show_partial_image()
            draw_score()
            draw_guess_box()

        pygame.display.flip()

        # Sjekker hendelser
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if not game_started and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50, 300, 100)
                if button_rect.collidepoint(mouse_pos):
                    game_started = True

            if game_started and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    check_answer(current_guess)
                    # Tilbakestiller gjetteboksen etter at svaret er sjekket
                    current_guess = ""

                elif event.key == pygame.K_BACKSPACE:
                    # Sletter siste tegn fra gjettet ord hvis BACKSPACE trykkes
                    current_guess = current_guess[:-1]

                else:
                    # Legger til trykte tegn til gjettet ord
                    current_guess += event.unicode

        clock.tick(FPS)

if __name__ == "__main__":
    main()


