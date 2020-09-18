import gym
import numpy as np
from gym import spaces
from scipy.signal import convolve2d


def check_four_in_a_row(board):
    """
    Check to see if there are any four in a rows in this board

    If one player has a four in a row, return that number.
    If no player does, return 0
    """
    kernels = np.ones((4, 1)), np.ones((1, 4)), np.eye(4), np.eye(4)[::-1]

    for player in (1, 2):
        for k in kernels:
            conv = convolve2d(board == player, k)
            if (conv == 4).any():
                return player

    return 0


class ConnectFourGame(gym.Env):
    """Connect Four Game"""

    metadata = {"render.modes": ["human"]}

    def __init__(self):
        self.action_space = spaces.Discrete(7)
        self.observation_space = None
        self.reset()

    def step(self, action):
        assert self.action_space.contains(action)

        column = self.board[:, action]
        open_spots = 6 - (column != 0).sum()

        if open_spots == 0:
            raise ValueError("Not a valid move.")

        val = 1 if self.turn == "X" else 2
        self.board[open_spots - 1, action] = val

        self.turn = "O" if self.turn == "X" else "X"

        return self._observation(), self._reward, self.done, {}

    def render(self, mode="human", close=False):
        board_string = str(self.board.reshape(6, 7))

        board_string = board_string.replace("[[", "|")
        board_string = board_string.replace("]]", "|")
        board_string = board_string.replace("]", "|")
        board_string = board_string.replace(" [", "|")
        board_string = board_string.replace(" ", "|")
        board_string = board_string.replace("0", " ")
        board_string = board_string.replace("1", "X")
        board_string = board_string.replace("2", "O")

        print(" 0 1 2 3 4 5 6")
        print(board_string)
        print()
        print(f"It is {self.turn}'s turn")

    def reset(self):
        self.board = np.zeros((6, 7), dtype=np.int8)
        self.turn = "X"
        self.done = False

    def _observation(self):
        return self.board

    def _reward(self):
        return 0.0
