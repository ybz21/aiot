import gym
from stable_baselines3 import PPO

import highway_env


def serve():
    model = PPO.load("highway_ppo/model")
    env = gym.make("two-way-v0")
    for _ in range(5):
        obs = env.reset()
        done = False
        while not done:
            action, _ = model.predict(obs)
            print(f'obs: {obs}')
            print(f'action: {action}')
            # time.sleep(5)
            obs, reward, done, info = env.step(action)
            env.render()


if __name__ == "__main__":
    serve()
