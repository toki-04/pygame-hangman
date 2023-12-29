import pygame, sys

pygame.init()

WIDTH = 800
HEIGHT = 600

FPS = 60

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock()

run = True

class KeyboardButton:
    def __init__(self, letter, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = pygame.font.Font("./assets/fonts/OMORI_GAME2.ttf", 50)

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, WHITE, self.rect)
            self.letter = self.font.render(letter, True, BLACK)
        else:
            pygame.draw.rect(screen, WHITE, self.rect, 2)
            self.letter = self.font.render(letter, True, WHITE)

        self.letter_rect = self.letter.get_rect(center=(self.rect.center))
        screen.blit(self.letter, self.letter_rect)

    def update(self):
        pass








def draw_keyboard():
    # KEYBOARD LETTERS
    keyboard_top = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
    keyboard_mid = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
    keyboard_bot = ["Z", "X", "C", "V", "B", "N", "M"]

    for index, key in enumerate(keyboard_top):
        btn = KeyboardButton(key, 55+(index*70), HEIGHT-220, 60, 60)
    for index, key in enumerate(keyboard_mid):
        btn = KeyboardButton(key, 100+(index*70), HEIGHT-150, 60, 60)
    for index, key in enumerate(keyboard_bot):
        btn = KeyboardButton(key, 165+(index*70), HEIGHT-80, 60, 60)




def make_text(text, size, color, pos):
    font = pygame.font.Font("./assets/fonts/OMORI_GAME2.ttf", size)
    text = font.render(text, True, color)
    rect = text.get_rect(center=pos)
    screen.blit(text, rect)

key_A = KeyboardButton("A", 10, 10, 50, 50)
while run:
    screen.fill("black")
    draw_keyboard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.update()

