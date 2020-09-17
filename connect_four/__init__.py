from gym.envs.registration import register

register(id="connect-four-v0", entry_point="connect_four.env:ConnectFourGame")
