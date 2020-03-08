class Game:
    def __init__(self):
        # Empty array with [0 ~ 8] index, ( 9 long )
        self.field = [' '] * 9  # Game Field

        # If this value is even, get_player() will set player as 'X'
        # If not, it will set as 'O'
        self.value = 0

        # This variable will be populated after the first execution
        # With either 'X' or 'O' values
        self.player = ''

    def show_field(self):
        # This variable is for aesthetic reasons only
        field = ''

        for i in range(len(self.field)):
            field += str(self.field[i]) + ' | '

            # Breaking the line, and cleaning the output
            if ((i + 1) % 3 == 0):  # If i equals (3, 6 or 9)
                print(field)
                field = ''

    def get_input(self):
        # Allow 1 ~ 9 index, instead of 0 ~ 8 index
        position = int(input('[1 ~ 9]: ')) - 1

        # Making sure the value of position is correct
        if (position >= 0 and position <= 8):

            # The user cannot replace the value inside the index
            if (self.field[position] == ' '):

                # get_player will return either 'X' or 'O' depending on self.value
                self.field[position] = self.get_player()

                # Value only increases if the player successfully plays
                self.value += 1

    def get_player(self):

        # If self.value is even, self.player is 'X'
        if (self.value % 2 == 0):
            self.player = 'X'

        # Else, self.player = 'O'
        else:
            self.player = 'O'

        return self.player

    def check_status(self):
        # Handful variables for winning checking
        win = counter = 0

        # Horizontal, indexes: (0, 1, 2), (3, 4, 5), (6, 7, 8)
        # Coefficient: 1
        for i in range(9):
            counter += 1

            if (self.field[i] == self.player):
                win += 1

                if (win >= 3):
                    return True

            if (counter >= 3):
                win = counter = 0

        win = counter = 0

        # Vertical, indexes: (0, 3, 6), (1, 4, 7), (2, 5, 8)
        # Coefficient: 3
        for i in range(3):

            # Prefixed_value is really smart
            # Since it's starting value is i ( 0, 1, 2 )
            # And it receives 3 ( the coefficient ) for each iteration on the second loop
            # It's size never get's bigger than the array's length
            # And it checks for every possible field index
            prefixed_value = i

            for i in range(3):

                if (self.field[prefixed_value] == self.player):
                    win += 1

                    if (win >= 3):
                        return True

                prefixed_value += 3

            win = 0

        # Crossed (0, 4, 8), (2, 4, 6)
        # Coefficient: 4, 2
        if (self.field[0] == self.player and self.field[4] == self.player and self.field[8] == self.player):
            return True
        elif (self.field[2] == self.player and self.field[4] == self.player and self.field[6] == self.player):
            return True

        for i in range(len(self.field)):
            if (self.field[i] == ' '):
                return False

            if (i == 8):  # If there is no free space available
                return True  # No one wons, it just restarts the game

        return False


game = Game()

while (game.check_status() == False):
    game.get_input()
    game.show_field()

print('{} WON!!'.format(game.player))
