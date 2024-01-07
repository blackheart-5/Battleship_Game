#################################################################
# 
#Part One
# In the first part of the game, each player places ships on their board. Ships may be placed
# horizontally or vertically (but not diagonally). Additionally, ships may not overlap each other.

#Part Two
# Once both players have placed their ships on their boards, they will take turns making guesses.
# The goal of the game is to guess the positions of your opponent’s ships, without being able to see the opponent’s
# board. A single guess is a coordinate (row, col) of a position on the opponents board. A guess that is at the
# location of a ship is called a hit. Otherwise, the guess is a miss. Players cannot guess the same position twice
# (this would also be a waste of a turn). If a ship has been hit in all of its positions, then it is considered sunk.
# The game ends when one player sinks all of another player’s ships.
#################################################################
from board_class import Ship, Board

from board_class import Ship, Board #important for the project
from game_class import Player, BattleshipGame #important for the project


def main():
    # initaialize board size and ship list
    board_size = 5
    ship_list = [5, 4, 3, 3, 2]

    # initialize board for each player
    player1_board = Board(board_size)
    player2_board = Board(board_size)

    # create a palyer instance of each player
    player1 = Player('Player 1', player1_board, ship_list)
    player2 = Player('Player 2', player2_board, ship_list)

    # play game from batttleship by calling an instance
    BattleshipGame(player1, player2).play()


if __name__ == "__main__":
    main()
