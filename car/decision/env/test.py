import time
from pygame_2d import PyGame2D
from env import CustomEnv
import numpy as np

def test_env():
    e=CustomEnv({})
    e.step(e.action_space.sample())
    e.render()
    time.sleep(199)


def test_game():
    a=PyGame2D(render=True)

    a.view()
    time.sleep(199)
    pass

if __name__=='__main__':
#     test_game()
    test_env()