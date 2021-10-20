import gym
from stable_baselines3 import PPO
import highway_env
import time


class Decision:
    def __init__(self):
        self.model = PPO.load("highway_ppo/model")
        obs = self.env.reset()

    def get_raw_action(self, obs):
        action, _ = self.model.predict(obs)
        return action

    def get_action(self, obs):
        action = self.get_raw_action(obs)
        if action == 0:
            return 'changeLeft'
        elif action == 2:
            return 'changeRight'
        else:
            return 'forward'


def main():
    d = Decision()
    d.get_action([])


if __name__ == '__main__':
    main()
