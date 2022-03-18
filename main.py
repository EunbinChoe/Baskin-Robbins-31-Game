import discord

TOKEN = '--'

client = discord.Client()

# implementation of the game to Discord
# in the process of developing

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'baskin-robins-31-game':
        channel = message.channel

        if user_message.lower() == "help":
            h = str("How to play: \nFirst, choose whether to start first or not.\n"
                    "Next, you and the computer each say 1-3 consecutive numbers at their turn starting with 1.\n"
                    "On your turn, to type how many numbers you want to say. From 1-3\n"
                    "If the computer says 31, you win.\n"
                    "If you say 31, you lose.\n"
                    "Enjoy the game!!")
            await channel.send(h)
            return

        if user_message.lower() == "start":
            await channel.send(str("Choose level "
                                   "\n\"1\" for basic mode "
                                   "\n\"2\" for normal mode "
                                   "\n\"3\" for difficult mode"))

            def l_check(m):
                return (m.content == '1' or m.content == '2' or m.content == '3') and m.channel == channel

            l_msg = await client.wait_for('message', check=l_check)
            level = int(l_msg.content)
            await channel.send(str("Would you like to go first? "
                                   "(\"1\" to go first, \"0\" to go second)"))

            def f_check(m):
                return (m.content == '1' or m.content == '2' or m.content == '3') and m.channel == channel

            f_msg = await client.wait_for('message', check=f_check)
            first = bool(f_msg.content)

            if level == 1:
                await channel.send('yay'.format(l_msg))
                start = game.BasicMode(first)
                start.start_game()
            elif level == 2:
                await channel.send('hh'.format(l_msg))
                start = game.NormalMode(first)
                start.start_game()
            else:
                await channel.send('gg'.format(l_msg))
                start = game.DiffNode(first)
                start.start_game()

            return

        # else:
        #     await channel.send(str("Sorry didn't understand that. Try again"))
        #     return

        # if user_message.lower() == 'hello':
        #     await channel.send(f'hello {username}!')
        #     return

    if user_message.lower() == '!anywhere':
        await channel.send('This can be used anywhere!')
        return


class BasicMode:
    def __init__(self, player_first):
        self.number = 0
        self.turn = 0
        self.first = player_first

    def player_turn(self):
        await ms.channel.send(str('Your turn!: '))

        def p_check(m):
            return (m.content == '1' or m.content == '2' or m.content == '3') and m.channel == channel

        p_msg = await client.wait_for('message', check=p_check)
        self.turn = int(p_msg.content)

        # while (self.turn > 3) or (self.turn < 1):
        #     print("The number of counts needs to be 1, 2, or 3!")
        #     self.turn = int(input('''Choose different number of counts: '''))

        numbers = ''
        for x in range(self.turn):
            self.number += 1
            numbers = numbers + str(self.number) + '\n'
            if self.number == 31:
                await ms.channel.send(str("Sorry, you lost:("))
                break
        await ms.channel.send(numbers)

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


client.run(TOKEN)
