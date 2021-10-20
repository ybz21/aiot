import gym
import highway_env
from stable_baselines3 import PPO

env = gym.make("two-way-v0")

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=int(2e4))
model.save("highway_ppo/model")
