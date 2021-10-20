import gym
import highway_env
import time

obs_length = 5




def test_env():
    env = gym.make("two-way-v0")
    env.reset()
    print(env.action_space)
    print(env.observation_space)

    while True:
        action = env.action_space.sample()
        obs, _, _, _ = env.step(0)
        print(f'---action: {action}')
        print(f'---obs: {obs}')

        env.render()
        time.sleep(10)

        obs, _, _, _ = env.step(2)
        time.sleep(10)
        env.render()
        print(f'---action: {action}')
        print(f'---obs: {obs}')


def generate_obs(has_car, now_lane):
    current_lane = [0] * obs_length

    if has_car:
        current_lane[1] = 1

    if now_lane == 'right':
        left_lane = [0] * obs_length
        right_lane = [1] * obs_length
    else:
        left_lane = [1] * obs_length
        right_lane = [0] * obs_length

    all_lanes = [
        left_lane,
        current_lane,
        right_lane
    ]

    full = [
        all_lanes,
        all_lanes,
        all_lanes
    ]

    print(full)
    return full


def main():
    generate_obs(True, 'right')

    generate_obs(False, 'right')

    generate_obs(True, 'left')

    generate_obs(False, 'left')


if __name__ == '__main__':
    main()
