import random


class Gamer:
    count = 0
    lost_game = False

    def __init__(self, appeal, n=None):
        self.appeal = appeal
        if n is None:
            n = []
        self.card = n
        temp = [i for i in range(1, 91)]
        for i in range(15):
            self.card.append((temp.pop(random.randint(0, len(temp) - 1))))
        self.card.sort()



    def print_card(self):
        print(self.appeal)
        print('-' * 27)
        print(' '.join(map(str, self.card[0:5])))
        print(' '.join(map(str, self.card[5: 10])))
        print(' '.join(map(str, self.card[10:15])))


    def next_step(self, barrel, answer=None):
        if barrel in self.card:
            self.card[self.card.index(barrel)] = '--'
            self.count += 1
            if answer == 'y' or None:
                return True
            elif answer == 'n':
                self.lost_game = True
        else:
            if answer == 'y':
                self.lost_game = True


class Barrel:
    options = [i for i in range(1, 91)]

    def throw(self):
        z = random.randint(0, len(self.options) - 1)
        return self.options.pop(z)


gamer_1 = Gamer('----- ваша карточка ---')
computer = Gamer('--- карта компьютера ---')
b = Barrel()
while gamer_1.count != 15 and computer.count != 15 and not gamer_1.lost_game:
    k = b.throw()
    print(f'Новый боченок: {k} (осталось {len(b.options)})')
    gamer_1.print_card()
    computer.print_card()
    gamer_1.next_step(k, input('-' * 27 + '\n' + 'Зачеркнуть цифру? (y/n)\n'))
    computer.next_step(k)
if gamer_1.count == 15:
    print('you win')
elif gamer_1.lost_game is True or computer.count == 3:
    print('game over')
