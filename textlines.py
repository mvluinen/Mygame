from vars import TEXT_COLOR

text_lines = []


class Texts:
    def __init__(self, text, position, font_size, color=TEXT_COLOR, output=""):
        self.text = text
        self.position = position
        self.font_size = font_size
        self.color = color
        self.output = output
        text_lines.append(self)

    def set_output(self, var):
        self.output = self.text + str(var)

    def get_class(self, var=None):
        '''Returns copy of class, optional: with the current value inserted'''
        Tempclass = self
        if var is not None:
            Tempclass.set_output(var)
        return Tempclass


Cash = Texts("Cash: ",
             (750, 10),  # pos X,Y
             64,)  # size, 'colorhex'

Monkey1_1_head = Texts("Tier 1_1 monkeys: ",
                       (100, 100),  # pos X,Y
                       64,)  # size, 'colorhex'

Monkey1_1_buy = Texts("Press 1 to buy: ",
                      (100, 150),  # pos X,Y
                      32,)  # size, 'colorhex'

Monkey1_2_head = Texts("Tier 1_2 monkeys: ",
                       (100, 250),  # pos X,Y
                       64,)  # size, 'colorhex'

Monkey1_2_buy = Texts("Press 2 to buy: ",
                      (100, 300),  # pos X,Y
                      32,)  # size, 'colorhex'

for line in text_lines:
    line.set_output(0)


if __name__ == '__main__':
    print(f'lines stored: {len(text_lines)}')
    print(Cash.output)
    print(Cash.get_class(5).output)
