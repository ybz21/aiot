import gym
from stable_baselines3 import PPO
import highway_env
import time
import os

current_dir = os.path.dirname(__file__)


class Decision:
    def __init__(self):
        model_path = os.path.join(current_dir, 'highway_ppo/model')
        self.model = PPO.load(model_path)

    def get_raw_action(self, obs):
        action, _ = self.model.predict(obs)
        return action

    def get_action(self, obs):
        # https://highway-env.readthedocs.io/en/latest/actions/index.html#discrete-meta-actions
        action = self.get_raw_action(obs)
        if action == 0:
            return 'changeLeft',action
        elif action == 2:
            return 'changeRight',action
        else:
            return 'forward',action


def main():
    d = Decision()
    d.get_action([])


if __name__ == '__main__':
    main()
