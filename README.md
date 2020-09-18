# Connect Four RL Experiment

I wanted to learn a little about how to use OpenAI `gym` environments so I implemented the game Connect Four.


## How to install

Install the package using `pip install -e .` in the top level directory.

## Basic Info

* Play as the majestic hero `X` against the dastardly evil villain `O`.
* Only the end of the game will give a reward.
  * `X` wins gives `reward = 100.0`
  * `O` wins gives `reward = -100.0`
  * Draw gives `reward = -50.0`
  * While the game is still going, `reward = 0.0`

## Using the environment

To create an environment:

```python
>>> import gym
>>> import connect_four

>>> env = gym.make('connect-four-v0')
```

To render the board:

```python
>>> env.render()
 0 1 2 3 4 5 6
| | | | | | | |
| | | | | | | |
| | | |X| | | |
| | | |O| |X| |
| | |O|O|O|X| |
|O| |O|X|X|X| |

It's X's turn.
```
