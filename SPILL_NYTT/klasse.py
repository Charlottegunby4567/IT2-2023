import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.Clock()
        self.is_running = True
        self.troll = Troll(400, 300)
        self.foods = [Food(random.randint(0, 780), random.randint(0, 580)) for _ in range(3)]
        self.obstacles = []
        self.score = 0
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 36)

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.troll.move('UP')
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.troll.move('DOWN')
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    self.troll.move('LEFT')
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.troll.move('RIGHT')

    def update(self):
        for food in self.foods:
            if self.troll.rect.colliderect(food.rect):
                self.score += 1
                self.troll.speed += 1
                self.obstacles.append(Obstacle(food.rect.x, food.rect.y))
                self.foods.remove(food)
                while True:
                    new_food = Food(random.randint(0, 780), random.randint(0, 580))
                    if all(not new_food.rect.colliderect(x.rect) for x in self.foods + self.obstacles + [self.troll]):
                        self.foods.append(new_food)
                        break

    def draw(self):
        self.screen.fill
