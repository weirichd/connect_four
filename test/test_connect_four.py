import numpy as np
import pytest

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


def test_step_turns_in_same_col():
    under_test = ConnectFourGame()

    expected = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
        ]
    )

    under_test.step(0)
    under_test.step(0)

    assert np.array_equal(under_test.board, expected)
    assert under_test.turn == "X"


def test_error_if_col_full():
    under_test = ConnectFourGame()

    under_test.board = np.array(
        [
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
        ]
    )

    with pytest.raises(ValueError):
        under_test.step(0)


def test_reset():
    under_test = ConnectFourGame()

    expected = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    )

    under_test.step(1)
    under_test.step(2)
    under_test.step(1)
    under_test.step(4)

    under_test.reset()

    assert np.array_equal(under_test.board, expected)
