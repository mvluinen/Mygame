
# Create a Monkey that increases a number
# Show number increasing on screen
# use Input to buy more of that monkey.

# imports
import pygame

# init
START_CASH = 10
START_MONKEY_1_1 = 30
START_MONKEY_1_1_PRICE = 10

START_MONKEY_1_2 = 0
START_MONKEY_1_2_PRICE = 1000

# start new save
cash = START_CASH
monkey_1_1 = START_MONKEY_1_1
monkey_1_1_price = START_MONKEY_1_1_PRICE
monkey_1_1_last_tick = 0
monkey_1_2 = START_MONKEY_1_2
monkey_1_2_price = START_MONKEY_1_2_PRICE
monkey_1_2_last_tick = 0

# set up pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# constants
FPS = 30
TEXT_COLOR = "#FFFF00"
BGCOLOR = "#001f24"
FONT_1 = pygame.font.Font(None, 64)
FONT_2 = pygame.font.Font(None, 32)

# vars
tick = 1




def text_out(text_line):
    text = texts[text_line]['text']
    position = texts[text_line]['position']
    font_size = texts[text_line]['font_size']
    output = (pygame.font.Font(None, font_size)
              .render(text, True, TEXT_COLOR)
              )
    screen.blit(output, position)
    return


while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BGCOLOR)

    texts = {
        'cash': {'text': f"Cash: ${cash}",
                 'position': (750, 10),
                 'font_size': 64},
        'monkey1_1': {'text': f"Tier 1_1 monkeys: {monkey_1_1}",
                      'position': (100, 100),
                      'font_size': 64},
        'monkey1_1_buy': {'text': f"Press 1 to buy: ${monkey_1_1_price}",
                          'position': (100, 150),
                          'font_size': 32},
        'monkey1_2': {'text': f"Tier 1_2 monkeys: {monkey_1_2}",
                      'position': (100, 250),
                      'font_size': 64},
        'monkey1_2_buy': {'text': f"Press 2 to buy: ${monkey_1_2_price}",
                          'position': (100, 300),
                          'font_size': 32},
            }

    for line in texts:
        text_out(line)

    # interaction by player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        # check money and buy delay of 10 ticks
        if cash > monkey_1_1_price and tick - 10 > monkey_1_1_last_tick:
            monkey_1_1 += 1
            cash = round(cash - monkey_1_1_price, 2)
            monkey_1_1_price = round(pow(monkey_1_1_price, 1.03), 2)
            monkey_1_1_last_tick = tick

    if keys[pygame.K_2]:
        if cash > monkey_1_2_price and tick - 10 > monkey_1_2_last_tick:
            monkey_1_2 += 1
            cash = round(cash - monkey_1_2_price, 2)
            monkey_1_2_price = round(pow(monkey_1_2_price, 1.03), 2)
            monkey_1_2_last_tick = tick

    # calc next tick
    if tick % 15 == 0:
        monkey_1_1 = round(monkey_1_1 + monkey_1_2, 0)
    if tick % 10 == 0:
        cash = round(cash + monkey_1_1, 2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to fps
    clock.tick(FPS)
    tick += 1

pygame.quit()