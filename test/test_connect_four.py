import numpy as np

from connect_four.env import ConnectFourGame


def test_step():
    under_test = ConnectFourGame()

    expected = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
        ]
    )

    under_test.step(0)

    assert np.array_equal(under_test.board, expected)
    assert under_test.turn == "O"


def test_step_two_turns():
    under_test = ConnectFourGame()

    expected = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
        ]
    )

    under_test.step(0)
    under_test.step(1)

    assert np.array_equal(under_test.board, expected)
    assert under_test.turn == "X"
