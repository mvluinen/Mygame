
# Create a Monkey that increases a number
# Show number increasing on screen
# use Input to buy more of that monkey.

# imports
import pygame

# init
START_CASH = 10
START_MONKEY_1_1 = 1
START_MONKEY_1_2 = 0

START_MONKEY_1_1_PRICE = 10
START_MONKEY_1_2_PRICE = 1000

# start new save
cash = START_CASH
monkey_1_1 = START_MONKEY_1_1
monkey_1_1_price = START_MONKEY_1_1_PRICE

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

# texts
texts = {
    'cash': {'text': f"Current Cash: ${cash}",
             'position': (800, 10),
             'font_size': 64},
    'monkey1_1': {'text': f"Tier 1_1 monkeys: {monkey_1_1}",
                  'position': (100, 100),
                  'font_size': 64},
    'monkey1_1_buy': {'text': f"Press 1 to buy: ${monkey_1_1_price}",
                      'position': (100, 150),
                      'font_size': 32}
        }


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

    for line in texts:
        text_out(line)

    # interaction by player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        if cash > monkey_1_1_price:
            monkey_1_1 += 1
            cash = round(cash - monkey_1_1_price, 2)
            monkey_1_1_price = round(monkey_1_1_price * 1.1, 2)

    # calc next tick

    if tick % 30 == 0:
        cash = round(cash + monkey_1_1, 2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to fps
    clock.tick(FPS)
    tick += 1

pygame.quit()

# while cash < 10:
#     os.system('clear')
#     print(f"# Tier 1 monkey: {monkey_1_1}")
#     print(f"total Cash: {cash}")
#     cash = cash + monkey_1_1
#     time.sleep(0.5)
