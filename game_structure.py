import random


class BasicMode:
    def __init__(self, player_first):
        self.number = 0
        self.turn = 0
        self.first = player_first

    def player_turn(self):
        self.turn = int(input('''Your turn!: '''))
        while (self.turn > 3) or (self.turn < 1):
            print("The number of counts needs to be 1, 2, or 3!")
            self.turn = int(input('''Choose different number of counts: '''))
        for x in range(self.turn):
            self.number += 1
            print(self.number)
            if self.number == 31:
                print("Sorry, you lost:(")
                break

    def comp_turn(self):
        counts = random.randrange(1, 4)
        print("Computer's turn")

        for i in range(counts):
            self.number += 1
            print(self.number)
            if self.number == 31:
                break

    def start_game(self):
        print('''OK, let's start!''')

        while self.number < 31:
            if self.first:
                self.first = False
            else:
                self.comp_turn()

            if self.number == 31:
                print("Congrats!! You won!")
                break
            else:
                self.player_turn()


class NormalMode(BasicMode):
    def comp_turn(self):
        print("Computer's turn")
        if self.number >= 23:
            for i in range(3):
                self.number += 1
                print(self.number)
                if self.number == 26 or self.number == 30:
                    break
                elif self.number == 31:
                    break
        else:
            counts = random.randrange(1, 4)
            for i in range(counts):
                self.number += 1
                print(self.number)
                if self.number == 31:
                    break


class DiffNode(BasicMode):
    def comp_turn(self):
        print("Computer's turn")
        if self.number == 0:
            self.number = 2
            print('1 \n2 ')
        else:
            if self.number == 1:
                self.number = 2
                print('2')
            elif self.number == 3:
                self.number = 6
                print('4 \n5 \n6')
            elif ((self.number + 2) % 4) != 0:
                for i in range(4 - self.turn):
                    self.number += 1
                    print(self.number)
                    if self.number == 31:
                        break
            else:
                self.number = self.number + 1
                print(self.number)
