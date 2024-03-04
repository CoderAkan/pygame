from random import randint
import pygame, sys
from button2 import Button

pygame.init()

win = pygame.display.set_mode((512, 512))

pygame.display.set_caption("Menu")

BG = pygame.image.load("background.jpg")
bullets = []

music = pygame.mixer.music.load("mus.mp3")
pygame.mixer.music.play(-1)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        win.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(30).render("MAIN MENU", True, "#d7fcd4")
        MENU_RECT = MENU_TEXT.get_rect(center=(250, 50))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(250, 150),
                             text_input='PLAY', font=get_font(25), base_color="#d7fcd4", hovering_color="white")
        INSTRUCTION_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(250, 270),
                                    text_input='INSTRUCTIONS', font=get_font(25), base_color="#d7fcd4", hovering_color="white")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(250, 390),
                             text_input='QUIT', font=get_font(25), base_color="#d7fcd4", hovering_color="white")
        win.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, INSTRUCTION_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play1()
                if INSTRUCTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instr()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def instr():
    pygame.display.set_caption('Instructions')
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        win.fill("white")
        win.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(20).render("Instructions", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(250, 45))
        win.blit(OPTIONS_TEXT, OPTIONS_RECT)

        GOAL_TEXT1 = get_font(12).render("The main goal is to collect eggs", True, "White")
        GOAL_RECT1 = GOAL_TEXT1.get_rect(topleft=(10, 70))
        win.blit(GOAL_TEXT1, GOAL_RECT1)

        SECOND_TEXT1 = get_font(12).render("A player can simultaneously shoot", True, "White")
        SECOND_RECT1 = SECOND_TEXT1.get_rect(topleft=(10, 100))
        win.blit(SECOND_TEXT1, SECOND_RECT1)

        SECOND_TEXT2 = get_font(12).render("only 5 eggs", True, "White")
        SECOND_RECT2 = SECOND_TEXT2.get_rect(topleft=(10, 115))
        win.blit(SECOND_TEXT2, SECOND_RECT2)

        THIRD_TEXT1 = get_font(12).render("To reach the next level player should", True, "White")
        THIRD_RECT1 = THIRD_TEXT1.get_rect(topleft=(10, 145))
        win.blit(THIRD_TEXT1, THIRD_RECT1)

        THIRD_TEXT2 = get_font(12).render("collect all necessary amounts of eggs", True, "White")
        THIRD_RECT2 = SECOND_TEXT2.get_rect(topleft=(10, 160))
        win.blit(THIRD_TEXT2, THIRD_RECT2)

        FOURTH_TEXT1 = get_font(12).render("To move right press right key", True, "White")
        FOURTH_RECT1 = FOURTH_TEXT1.get_rect(topleft=(10, 190))
        win.blit(FOURTH_TEXT1, FOURTH_RECT1)

        FOURTH_TEXT2 = get_font(12).render("to move left press left key", True, "White")
        FOURTH_RECT2 = FOURTH_TEXT2.get_rect(topleft=(10, 205))
        win.blit(FOURTH_TEXT2, FOURTH_RECT2)

        FIFTH_TEXT1 = get_font(12).render("To shoot eggs press space key, to appear", True, "White")
        FIFTH_RECT1 = FIFTH_TEXT1.get_rect(topleft=(10, 235))
        win.blit(FIFTH_TEXT1, FIFTH_RECT1)

        FIFTH_TEXT2 = get_font(12).render("in specific place click anywhere", True, "White")
        FIFTH_RECT2 = FIFTH_TEXT2.get_rect(topleft=(10, 250))
        win.blit(FIFTH_TEXT2, FIFTH_RECT2)

        FIFTH_TEXT3 = get_font(12).render("in the screen with mouse after", True, "White")
        FIFTH_RECT3 = FIFTH_TEXT3.get_rect(topleft=(10, 265))
        win.blit(FIFTH_TEXT3, FIFTH_RECT3)

        FIFTH_TEXT4 = get_font(12).render("1 seconds it works only in Level 1", True, "White")
        FIFTH_RECT4 = FIFTH_TEXT4.get_rect(topleft=(10, 280))
        win.blit(FIFTH_TEXT4, FIFTH_RECT4)

        SIXTH_TEXT1 = get_font(12).render("Moving mouse down will make the", True, "White")
        SIXTH_RECT1 = SIXTH_TEXT1.get_rect(topleft=(10, 310))
        win.blit(SIXTH_TEXT1, SIXTH_RECT1)

        SIXTH_TEXT2 = get_font(12).render("velocity -= 2", True, "White")
        SIXTH_RECT2 = SIXTH_TEXT2.get_rect(topleft=(10, 325))
        win.blit(SIXTH_TEXT2, SIXTH_RECT2)

        SIXTH_TEXT3 = get_font(12).render("Moving mouse up will make the", True, "White")
        SIXTH_RECT3 = SIXTH_TEXT3.get_rect(topleft=(10, 340))
        win.blit(SIXTH_TEXT3, SIXTH_RECT3)

        SIXTH_TEXT4 = get_font(12).render("velocity += 1", True, "White")
        SIXTH_RECT4 = SIXTH_TEXT4.get_rect(topleft=(10, 355))
        win.blit(SIXTH_TEXT4, SIXTH_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(250, 425),
                              text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def play1():
    win.blit(BG, (0, 0))
    pygame.display.set_caption("Level 1")

    fire = pygame.image.load("fire.png")

    hitSound = pygame.mixer.Sound("hit.mp3")
    bulletSound = pygame.mixer.Sound("bullet.mp3")

    clock = pygame.time.Clock()

    score = 0

    class Basket:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 3
        def draw(self, win):
            pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.width, self.height))
        def cleared(self):
            win.blit(BG, (0, 0))
            self.font2 = pygame.font.SysFont("Press Start 2P", 50)
            self.text2 = self.font2.render("Level 1 is cleared", 1, (255, 0, 0))
            win.blit(self.text2, (250 - (self.text2.get_width() / 2), 200))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()
    class Egg(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.vel = 2
            self.visible = True
            self.hitBox = [self.x + 15, self.y + 2, 35, 50]
        def draw(self, win):
            self.move()
            if self.visible:
                win.blit(fire, (self.x, self.y))
        def move(self):
            if self.y < 500:
                self.y += self.vel
            else:
                self.visible = False
        def hit(self):
            self.visible = False

    def redrawGameWindow():
        win.blit(BG, (0, 0))
        text = font.render("Score: " + str(score), 1, (255, 255, 255))
        win.blit(text, (360, 16))
        basket.draw(win)
        for egg in eggs:
            egg.draw(win)
        pygame.display.update()

    font = pygame.font.SysFont('Press Start 2P', 40, True)
    basket = Basket(250 - 25, 400, 50, 100)
    m = [100 - 32, 150 - 32, 200 - 32, 250 - 32, 300 - 32, 350 - 32, 400 - 32, 450 - 32]
    shootLoop = 0
    run = True
    t = False
    ik = -1
    eggs = []
    while run:
        clock.tick(27)

        ik += 1
        if ik == 25:
            shootLoop = 0
            ik = -1


        if score == 5:
            eggs.clear()
            basket.cleared()
            play2()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                basket.vel -= 1
                print("Down")
            if event.type == pygame.MOUSEBUTTONUP:
                basket.vel += 2
                print('Up')
            if t and event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                basket.x, basket.y = mouse_position[0], 400
                t = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for egg in eggs:
            if basket.y <= egg.y <= basket.y + basket.height and basket.x <= egg.x <= basket.x + basket.width:
                hitSound.play()
                score += 1
                eggs.pop(eggs.index(egg))
            if egg.y < 500 and egg.y > 0:
                egg.y += egg.vel
            else:
                eggs.pop(eggs.index(egg))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            if len(eggs) < 5:
                bulletSound.play()
                eggs.append(Egg(m[randint(0, len(m) - 1)], 5))
            shootLoop = 1

        if keys[pygame.K_LEFT] and basket.x > 5:
            basket.x -= basket.vel
        elif keys[pygame.K_RIGHT] and basket.x < 500 - basket.width - basket.vel:
            basket.x += basket.vel
        if keys[pygame.K_UP]:
            if basket.y > 20:
                basket.y -= basket.vel
        elif keys[pygame.K_DOWN]:
            if basket.y <= 400:
                basket.y += basket.vel
        redrawGameWindow()
    pygame.display.update()

def play2():
    win.blit(BG, (0, 0))
    pygame.display.set_caption("Level 2")

    fire = pygame.image.load("fire.png")

    hitSound = pygame.mixer.Sound("hit.mp3")
    bulletSound = pygame.mixer.Sound("bullet.mp3")

    clock = pygame.time.Clock()

    score = 0

    class Basket:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 4
        def draw(self, win):
            pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.width, self.height))
        def cleared(self):
            win.blit(BG, (0, 0))
            self.font2 = pygame.font.SysFont("Press Start 2P", 50)
            self.text2 = self.font2.render("The end", 1, (255, 0, 0))
            self.font3 = pygame.font.SysFont("Press Start 2P", 25)
            self.text3 = self.font3.render("You were able to collect all eggs", 1, (255, 0, 0))
            win.blit(self.text2, (250 - (self.text2.get_width() / 2), 200))
            win.blit(self.text3, (250 - (self.text3.get_width() / 2), 400))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()
    class Egg(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.vel = 3
            self.visible = True
        def draw(self, win):
            self.move()
            if self.visible:
                win.blit(fire, (self.x, self.y))
        def move(self):
            if self.y < 500:
                self.y += self.vel
            else:
                self.visible = False
        def hit(self):
            self.visible = False

    def redrawGameWindow():
        win.blit(BG, (0, 0))
        text = font.render("Score: " + str(score), 1, (255, 255, 255))
        win.blit(text, (360, 16))
        basket.draw(win)
        for egg in eggs:
            egg.draw(win)
        pygame.display.update()

    font = pygame.font.SysFont('Press Start 2P', 40, True)
    basket = Basket(250 - 25, 400, 50, 100)
    m = [100 - 32, 150 - 32, 200 - 32, 250 - 32, 300 - 32, 350 - 32, 400 - 32, 450 - 32]
    shootLoop = 0
    run = True
    t = False
    ik = -1
    eggs = []
    while run:
        clock.tick(27)

        ik += 1
        if ik == 25:
            shootLoop = 0
            ik = -1


        if score == 10:
            eggs.clear()
            basket.cleared()
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                basket.vel -= 1
                print("Down")
            if event.type == pygame.MOUSEBUTTONUP:
                basket.vel += 2
                print('Up')
            if t and event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                basket.x, basket.y = mouse_position[0], 400
                t = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for egg in eggs:
            if basket.y <= egg.y <= basket.y + basket.height and basket.x <= egg.x <= basket.x + basket.width:
                hitSound.play()
                score += 1
                eggs.pop(eggs.index(egg))
            if egg.y < 500 and egg.y > 0:
                egg.y += egg.vel
            else:
                eggs.pop(eggs.index(egg))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            if len(eggs) < 5:
                bulletSound.play()
                eggs.append(Egg(m[randint(0, len(m) - 1)], 5))
            shootLoop = 1

        if keys[pygame.K_LEFT] and basket.x > 5:
            basket.x -= basket.vel
        elif keys[pygame.K_RIGHT] and basket.x < 500 - basket.width - basket.vel:
            basket.x += basket.vel
        if keys[pygame.K_UP]:
            if basket.y > 20:
                basket.y -= basket.vel
        elif keys[pygame.K_DOWN]:
            if basket.y <= 400:
                basket.y += basket.vel
        redrawGameWindow()
    pygame.display.update()
main_menu()
