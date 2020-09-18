# Connect Four RL Experiment

I wanted to learn a little about how to use OpenAI `gym` environments so I implemented the game Connect Four.


## How to install

Install the package using `pip install -e .` in the top level directory.

## Using the environment

To create an environment

```python
>>> import gym
>>> import connect_four

>>> env = gym.make('connect-four-v0')
```
