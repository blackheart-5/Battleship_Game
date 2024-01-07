class Ship(object):
    """
        This class represents a ship model.
    """
    def __init__(self, length: int, position: tuple, orientation: str):
        """
            create a ship instance using this constructor
            take three arguments and initialize these attributes with self
            initialize hit count to 0 and is sunk to False
        """
        self.length = length
        self.position = position
        self.orientation = orientation
        self.hit_count = 0
        self.is_sunk = False
        #self.positions = get_positions()

    def get_positions(self):
        """
            create an empty list called positions
            for each form of orientation
            loop i lenght times and change either the y and x coordinates
            depending on the form of orientation then append that change in coordinates to positions
            returns the list positions
        """
        positions = list()
        if self.orientation == 'h':
            for i in range(self.length):
                y = int(self.position[1]) + i
                positions.append((int(self.position[0]), y))
        elif self.orientation == 'v':
            # positions = list()
            for i in range(self.length):
                x = int(self.position[0]) + i
                positions.append((x, int(self.position[1])))

        return positions

    def get_orientation(self):
        """
            return the orientation of the coordinates
        """
        return self.orientation

    def apply_hit(self):
        """
            for each position from player
              check it in positions and increase count by 1 iof True
              if the hit count equals lenght of ship then is_sunk is True
        """
        if self.position in self.get_positions():
            self.hit_count += 1
            if self.hit_count == self.length:
                self.is_sunk = True


class Board(object):
    """
        This class represents a simple model of a board.
    """
    def __init__(self, size: int):
        """
            create a Board instance using this constructor
            take one arguments and initialize these attributes with self
            initialize ships to empty list
            initialize board to empty list and continuosly update it
        """
        self.size = size
        self.board = []
        for i in range(self.size):
            lst = []
            for e in range(self.size):
                lst.append(' ')
            self.board.append(lst)
        self.ships = list()

    def place_ship(self, ship):
        """
            add your method header here.
            append each ship to the ship attribute.
            get the positions of each ship object
            loop through positions and replace the board at that location to S
            this ship attribute is a list of each ship object of the ship class
        """
        self.ships.append(ship)
        positions = ship.get_positions()
        #print(positions)
        #print(self.board)
        for x, y in positions:
            self.board[x][y] = "S"
        # print(self.board)

    def apply_guess(self, guess):
        """
            add your method header here.
            take the list of ships
            loop through and check if guess in the positions of each ship
                then apply hit
                then change S to H at that guess
        """
        all_positions = list()
        for ship in self.ships:
            positions = ship.get_positions()
            for i in positions:
                all_positions.append(i)
        if guess in all_positions:
            #ship.apply_hit()
            x, y = guess
            self.board[x][y] = "H"
            print("Hit!")
        else:
            x, y = guess
            self.board[x][y] = "M"
            print("Miss!")
            #break

    def validate_ship_coordinates(self, ship):
        """
            get the positions of each ship
            loop through positions
              check if the position at index 0 and 1 is greater than the boards size
                 then raise an error

              check if the board location at that position is not of the form " "
                 then raise an error
        """
        positions = ship.get_positions()
        for i in positions:
            if i[0] > self.size or i[1] > self.size:
                raise RuntimeError("Ship coordinates are out of bounds!")
            # print(i)
            if self.board[i[0]][i[1]] != ' ':
                raise RuntimeError("Ship coordinates are already taken!")

    def __str__(self):
        """
          Represents the current state of the game board as a formatted string.
          Returns:
          str: A string representation of the current state of the game board, where:
        - '[ ]' represents an empty cell,
        - '[S]' represents a ship,
        - '[H]' represents a hit,
        - '[M]' represents a miss.
        so after each iteration, the current_board is editated based on this representations
        """
        current_board = ''
        for row in self.board:
            for element in row:
                if element == ' ':
                    current_board += '[ ]'
                elif element == 'S':
                    current_board += '[S]'
                elif element == 'H':
                    current_board += '[H]'
                elif element == 'M':
                    current_board += '[M]'
            current_board += '\n'
        #print(current_board)
        return current_board
