import numpy as np
import pytest

from connect_four.environment import ConnectFourGame
from connect_four.environment.connect_four_env import check_four_in_a_row


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

    # Do some stuff
    under_test.step(1)
    under_test.step(2)
    under_test.step(1)
    under_test.step(4)

    under_test.reset()

    assert np.array_equal(under_test.board, expected)


def test_check_four_in_a_row_empty_board():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    )

    expected = 0

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_horizontal_winner():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 2, 2, 2],
        ]
    )

    expected = 1

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_vertical_winner():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
        ]
    )

    expected = 1

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_diagonal_winner():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 0],
            [1, 2, 1, 2, 1, 0, 0],
        ]
    )

    expected = 1

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_off_diagonal_winner():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 2, 0, 0],
            [0, 0, 1, 2, 2, 0, 0],
            [0, 1, 2, 2, 1, 1, 0],
        ]
    )

    expected = 1

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_player_two_wins():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 1, 1, 1, 0, 0],
        ]
    )

    expected = 2

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_step_return_values():
    under_test = ConnectFourGame()

    expected_observation = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
        ]
    )

    expected_reward = 0.0
    expected_done = False
    expected_info = {}

    observation, reward, done, info = under_test.step(0)

    assert np.array_equal(observation, expected_observation)
    assert expected_reward == reward
    assert expected_done == done
    assert expected_info == info


def test_step_return_values_win():
    under_test = ConnectFourGame()

    under_test.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
        ]
    )

    expected_observation = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0],
        ]
    )

    expected_reward = 100.0
    expected_done = True
    expected_info = {}

    observation, reward, done, info = under_test.step(3)

    assert np.array_equal(observation, expected_observation)
    assert expected_reward == reward
    assert expected_done == done
    assert expected_info == info


def test_step_return_values_loss():
    under_test = ConnectFourGame()

    under_test.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0, 0],
        ]
    )
    under_test.turn = "O"

    expected_observation = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0, 0],
        ]
    )

    expected_reward = -100.0
    expected_done = True
    expected_info = {}

    observation, reward, done, info = under_test.step(1)

    assert np.array_equal(observation, expected_observation)
    assert expected_reward == reward
    assert expected_done == done
    assert expected_info == info


def test_step_return_values_draw():
    under_test = ConnectFourGame()

    under_test.board = np.array(
        [
            [0, 1, 2, 2, 1, 2, 1],
            [2, 1, 2, 2, 1, 2, 1],
            [2, 1, 2, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2],
            [1, 2, 1, 1, 2, 1, 1],
            [1, 2, 1, 1, 2, 1, 2],
        ]
    )
    under_test.turn = "O"

    expected_observation = np.array(
        [
            [2, 1, 2, 2, 1, 2, 1],
            [2, 1, 2, 2, 1, 2, 1],
            [2, 1, 2, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2],
            [1, 2, 1, 1, 2, 1, 1],
            [1, 2, 1, 1, 2, 1, 2],
        ]
    )

    expected_reward = -50.0
    expected_done = True
    expected_info = {}

    observation, reward, done, info = under_test.step(0)

    assert np.array_equal(observation, expected_observation)
    assert expected_reward == reward
    assert expected_done == done
    assert expected_info == info


def test_get_valid_moves():
    under_test = ConnectFourGame()

    expected = [0, 1, 2, 3, 4, 5, 6]

    actual = under_test.get_valid_moves()

    assert actual == expected


def test_get_valid_moves_with_some_columns_full():
    under_test = ConnectFourGame()
    under_test.board = np.array(
        [
            [1, 0, 2, 0, 2, 0, 0],
            [1, 0, 2, 0, 1, 0, 0],
            [2, 0, 1, 0, 2, 0, 0],
            [1, 0, 2, 0, 1, 0, 0],
            [1, 0, 2, 0, 2, 0, 1],
            [1, 0, 2, 0, 1, 1, 2],
        ]
    )

    expected = [1, 3, 5, 6]

    actual = under_test.get_valid_moves()

    assert actual == expected


def test_is_draw():
    under_test = ConnectFourGame()
    under_test.board = np.array(
        [
            [2, 1, 2, 2, 1, 2, 1],
            [2, 1, 2, 2, 1, 2, 1],
            [2, 1, 2, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2],
            [1, 2, 1, 1, 2, 1, 2],
            [1, 2, 1, 1, 2, 1, 2],
        ]
    )

    assert under_test.is_draw()


def test_not_is_draw():
    under_test = ConnectFourGame()
    under_test.board = np.array(
        [
            [1, 0, 2, 0, 2, 0, 0],
            [1, 0, 2, 0, 1, 0, 0],
            [2, 0, 1, 0, 2, 0, 0],
            [1, 0, 2, 0, 1, 0, 0],
            [1, 0, 2, 0, 2, 0, 1],
            [1, 0, 2, 0, 1, 1, 2],
        ]
    )

    assert not under_test.is_draw()


def test_not_is_draw_with_full_board_and_winner():
    under_test = ConnectFourGame()
    under_test.board = np.array(
        [
            [2, 1, 2, 2, 1, 2, 1],
            [2, 1, 2, 2, 1, 2, 1],
            [2, 1, 2, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 1, 2],
            [1, 2, 1, 1, 2, 1, 1],
            [1, 2, 1, 1, 2, 1, 2],
        ]
    )

    assert not under_test.is_draw()
