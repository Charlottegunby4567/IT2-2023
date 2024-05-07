import pygame
import random


pygame.init()


BREDDE, HØYDE = 800, 600
VINDU = pygame.display.set_mode((BREDDE, HØYDE))
pygame.display.set_caption("Pong")


HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRÅ = (128, 128, 128)


SPILLER_BREDDE, SPILLER_HØYDE = 10, 100
SPILLER_FART = 5


BALL_STØRRELSE = 15
BALL_FART_X = 5
BALL_FART_Y = 5


HINDRE_BREDDE, HINDRE_HØYDE = 20, 100
HINDRE_POSISJON_X = BREDDE // 2 - HINDRE_BREDDE //2
HINDRE_POSISJON_Y = [HØYDE // 4 - HINDRE_HØYDE //2, HØYDE // 2 - HINDRE_HØYDE // 2, 3 * HØYDE // 4 - HINDRE_HØYDE // 2]


spiller1 = pygame.Rect(50, HØYDE // 2 - SPILLER_HØYDE // 2, SPILLER_BREDDE, SPILLER_HØYDE)
spiller2 = pygame.Rect(BREDDE - 50 - SPILLER_BREDDE, HØYDE // 2 - SPILLER_HØYDE // 2, SPILLER_BREDDE, SPILLER_HØYDE)


ball = pygame.Rect(BREDDE // 2 - BALL_STØRRELSE // 2, HØYDE // 2 - BALL_STØRRELSE // 2, BALL_STØRRELSE, BALL_STØRRELSE)
ball_fart_x = BALL_FART_X * random.choice ((1, -1))
ball_fart_y = BALL_FART_Y * random.choice ((1, -1))


hindre = [pygame.Rect(HINDRE_POSISJON_X, HINDRE_POSISJON_Y[0], HINDRE_BREDDE, HINDRE_BREDDE),
        pygame.Rect(HINDRE_POSISJON_X, HINDRE_POSISJON_Y[1], HINDRE_BREDDE, HINDRE_HØYDE),
        pygame.Rect(HINDRE_POSISJON_X, HINDRE_POSISJON_Y[2], HINDRE_BREDDE, HINDRE_HØYDE)]


poeng_spiller1 = 0
poeng_spiller2 = 0
font = pygame.font.Font(None, 50)


def tegn_vindu(spiller1, spiller2, ball, hindre, poeng_spiller1, poeng_spiller2):
    VINDU.fill(SVART)
    pygame.draw.rect(VINDU, HVIT, spiller1)
    pygame.draw.rect(VINDU, HVIT, spiller2)
    pygame.draw.rect(VINDU, HVIT, ball)


    for hindre_rect in hindre:
        pygame.draw.rect(VINDU, GRÅ, hindre_rect)



    poeng_tekst = font.render (f"{poeng_spiller1} {poeng_spiller2}", True, HVIT)
    VINDU.blit(poeng_tekst, (BREDDE // 2 - poeng_tekst.get_width() // 2, 20))


    pygame.display.update()


def håndter_input(spiller):
    keys = pygame.key.get_pressed()
    if keys [pygame.K_w]:
        spiller.y -= SPILLER_FART
    if keys [pygame.K_s]:
        spiller.y += SPILLER_FART


def spill():
    global ball_fart_x, ball_fart_y, poeng_spiller1, poeng_spiller2

    klokke = pygame.time.Clock()
    kjør = True

    while kjør:
        klokke.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kjør = False

        håndter_input(spiller1)
        håndter_input(spiller2)


        ball.x += ball_fart_x
        ball.y += ball_fart_y
        

        if ball.colliderect(spiller1) or ball.colliderect (spiller2):
            ball_fart_x *= -1


        for hindre_rect in hindre:
            if ball.colliderect(hindre_rect):
                ball_fart_x *= -1


        if ball.y <= 0 or ball.y >= HØYDE - BALL_STØRRELSE:
            ball_fart_y *= -1


        if ball.x <= 0:
            poeng_spiller2 += 1
            ball.x = BREDDE // 2 - BALL_STØRRELSE // 2
            ball.y = HØYDE // 2 - BALL_STØRRELSE // 2
            ball_fart_x = BALL_FART_X * random.choice ((1, -1))
            ball_fart_y = BALL_FART_Y * random.choice ((1, -1))
        elif ball.x >= BREDDE - BALL_STØRRELSE:
            poeng_spiller1 += 1
            ball.x = BREDDE // 2- BALL_STØRRELSE // 2
            ball.y = HØYDE // 2 - BALL_STØRRELSE // 2
            ball_fart_x = BALL_FART_X * random.choice ((1, -1))
            ball_fart_y = BALL_FART_Y * random.choice ((1, -1))

        tegn_vindu(spiller1, spiller2, ball, hindre, poeng_spiller1, poeng_spiller2)

    pygame.quit()

if __name__ == "__main__":
    spill()