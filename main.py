
# Create a Monkey that increases a number
# Show number increasing on screen
# use Input to buy more of that monkey.

# imports
import pygame
from vars import (
   FPS,
   BGCOLOR,
   tick_counter,
   cash
)
from textlines import text_lines
import textlines


# set up pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


class Monkey:
    def __init__(self, prestige, tier, price, amount=0, last_tick=0):
        self.prestige = prestige
        self.tier = tier
        self.price = price
        self.amount = amount
        self.last_tick = last_tick
        self.name = f"monkey_{prestige}_{tier}"
        self.head = f"{self.name}_head"
        self.buy = f"{self.name}_buy"


monkey_1_1 = Monkey(1,  1,  1e1,    30)
monkey_1_2 = Monkey(1,  2,  1e3,)
monkey_1_3 = Monkey(1,  3,  1e6,)
monkey_1_4 = Monkey(1,  4,  1e9,)
monkey_1_5 = Monkey(1,  5,  1e12,)

# print(f"monkey amount 1.1 = {monkey_1_1.amount}")

def text_out(line):
    screen.blit(
        pygame.font.Font(None, line.font_size)
        .render(line.output, True, line.color),
        line.position)
    return


while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BGCOLOR)

    for line in text_lines:
        text_out(line.get_class())

    # interaction by player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        # check money and buy delay of 10 ticks
        if (cash > monkey_1_1.price and
            tick_counter - 10 > monkey_1_1.last_tick):

            monkey_1_1.amount += 1
            textlines.Monkey1_1_head.set_output(monkey_1_1.amount)

            cash = round(cash - monkey_1_1.price, 2)
            textlines.Cash.set_output(cash)

            monkey_1_1.price = round(pow(monkey_1_1.price, 1.03), 2)
            textlines.Monkey1_1_buy.set_output(monkey_1_1.price)
            monkey_1_1.last_tick = tick_counter

    if keys[pygame.K_2]:
        # check money and buy delay of 10 ticks
        if (cash > monkey_1_2.price and
            tick_counter - 10 > monkey_1_2.last_tick):

            monkey_1_2.amount += 1
            textlines.Monkey1_2_head.set_output(monkey_1_2.amount)

            cash = round(cash - monkey_1_2.price, 2)
            textlines.Cash.set_output(cash)

            monkey_1_2.price = round(pow(monkey_1_2.price, 1.03), 2)
            textlines.Monkey1_2_buy.set_output(monkey_1_2.price)
            monkey_1_2.last_tick = tick_counter

    # calc next tick
    if tick_counter % 15 == 0:
        monkey_1_1.amount = round(monkey_1_1.amount + monkey_1_2.amount, 0)
        textlines.Monkey1_1_head.set_output(monkey_1_1.amount)
    if tick_counter % 10 == 0:
        cash = round(cash + monkey_1_1.amount, 2)
        textlines.Cash.set_output(cash)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to fps
    clock.tick(FPS)
    tick_counter += 1

# print(textlines.Cash.get_class().output)
pygame.quit()
