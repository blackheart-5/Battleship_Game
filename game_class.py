from board_class import Ship,  Board # important for the project

# # Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
import sys
def input( prompt=None ):
   if prompt != None:
       print( prompt, end="" )
   aaa_str = sys.stdin.readline()
   aaa_str = aaa_str.rstrip( "\n" )
   print( aaa_str )
   return aaa_str


class Player(object):
    """
        This class represents a player model
    """
    def __init__(self, name: str, board: Board, ship_list: list):
        """
            create a player instance using this constructor
            take three arguments and initialize these attributes with self
            initialize guesses to empty list
        """
        self.name = name
        self.board = board
        self.ship_list = ship_list
        # self.board.ships = ship_list
        self.guesses = list()

    def validate_guess(self, guess):
        """
           try and except to catch invalid guess from player
           Raise Error:
              if guess in list of guesses
              if guess at index 0 or 1 are greater than the length of the board

        """
        try:
            x, y = guess
            # print(guess)
            # print(self.board.board[x-1][y-1])
            if guess in self.guesses:
                raise RuntimeError("This guess has already been made!")
            # -1 to account for the indexing
            if x > len(self.board.board) or y > len(self.board.board):
                raise RuntimeError("Guess is not a valid location!")
        except RuntimeError as error:
            print(f'{error}')

    def get_player_guess(self):
        """
          loop until you get a valid guess from player
          call validate method and apply the guess method on the board
          and return the guess of player
        """
        while True:
            try:
                guess = input("Enter your guess: ")
                play = (int(guess[0]), int(guess[3]))
                self.validate_guess(play)
                self.board.apply_guess(play)

            except RuntimeError as error:
                print({error})
                continue
            else:
                return play

    def set_all_ships(self):
        """
            Set the positions of all ships on the player's board.
            Iterates through the ship list, prompting the user to input
            coordinates and orientation for each ship. It creates a Ship instance and
            attempts to validate and place the ship on the player's board. If an error
            occurs, it prints the error message and prompts the user to try again.
            Raises RuntimeError If there is an issue with the entered coordinates
        """
        for ship in self.ship_list:
            while True:
                try:
                    coordinates = input(f"Enter the coordinates of the ship of size {ship}: ")
                    orientation = input(f"Enter the orientation of the ship of size {ship}: ").lower()
                    coordinate = tuple(coordinates.split(','))
                    ship_instance = Ship(ship, coordinate, orientation)
                    player_board = self.board
                    player_board.validate_ship_coordinates(ship_instance)
                    # print('no error found')
                    player_board.place_ship(ship_instance)

                except RuntimeError as error:
                    print(f'{error}')
                    continue
                else:
                    break


class BattleshipGame(object):
    """
        This class represents how the Game model is played
    """

    def __init__(self, player1: Player, player2: Player):
        """
            create a BattleshipGame instance using this constructor
            take two arguments and initialize these attributes with self
        """
        self.player1 = player1
        self.player2 = player2

    def check_game_over(self):
        """
            Check if the game is over by evaluating the number of opponent pieces for each player.
            Returns a string of the name of the player who won, or an empty string if the game is not over.
        """
        # check player1
        player1_lst = self.player1.board.board
        player2_lst = self.player2.board.board
        count = 0
        o_count1 = 0
        c1 = 0
        for row in player1_lst:
            for index in row:
                if index != " ":
                    c1 += 1
                    if index == 'H' or index == 'M':
                        count += 1
                    else:
                        o_count1 += 1

        # check player2
        count2 = 0
        o_count2 = 0
        c2 = 0
        for row in player2_lst:
            for index in row:
                if index != " ":
                    c2 += 1
                    if index == 'H' or index == 'M':
                        count2 += 1
                    else:
                        o_count2 += 1

        if o_count1 == 0:
            return self.player1.name
        elif o_count2 == 0:
            return self.player2.name
        else:
            return ''

    def display(self):
        """
            print board of each player
        """
        print("Player 1's board:")
        print(self.player1.board)

        print("Player 2's board:")
        print(self.player2.board)

    def play(self):
        """
            In Part 1:
               each player places all their ships

            In Part 2:
              the boards of the players is displayed
              each player is asked to input their guess
              at each turn the check_game_over method is called
                if check_game_over is '' then player 2 continues
                else:
                  find winner and break
              after player 2 continues,
                check check_game_over and if no winner then ask
                if they want to continue
        """
        while True:
            # Part1
            self.player1.set_all_ships()
            self.player2.set_all_ships()

            #print("Done with Part 1")
            #print()

            # self.player1.board.place_ship(ship)
            # self.player2.board.place_ship(ship)

            while True:
                # Part2
                self.display()
                print("Player 1's turn.")
                self.player1.get_player_guess()
                if self.check_game_over() == '':
                    print("Player 2's turn.")
                    self.player2.get_player_guess()
                else:
                    winner = self.check_game_over()
                    print(f'{winner} wins!')
                    break

                # check game over
                if self.check_game_over() == '':
                    command = input("Continue playing?: ").lower()
                    if command == 'q':
                        break
                    else:
                        continue
                else:
                    winner = self.check_game_over()
                    print(f'{winner} wins!')
                    break
            break


