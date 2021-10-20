from observe.lidar import get_distance
from orient.observation import generate_obs

from decision.decision import Decision
from control.car_speed import SpeedCar

import time

TIME_TURN = 1
TIME_FORWARD = 1
SPEED = 0.5
USE_RULE_ACTION = True


def get_rule_action(distance, now_lane):
    if distance < 30.0 and now_lane == 'right':
        return 'changeLeft'
    elif distance < 30.0 and now_lane == 'left':
        return 'changeRight'
    else:
        return 'forward'


def get_rl_action(decision, distance, now_lane):
    obs = generate_obs(distance, now_lane)
    action, raw_action = decision.get_action(obs)
    print(f'rl raw_action:{raw_action}')
    return action


def main():
    now_lane = 'right'
    decision = Decision()
    car = SpeedCar()

    while True:
        distances = []
        for i in range(10):
            distance = get_distance()
            distances.append(distance)

        distance = sum(distances) / 10.0
        print("distance: %.1f cm" % distance)

        if USE_RULE_ACTION:
            action = get_rule_action(distance, now_lane)
        else:
            action = get_rl_action(decision, distance, now_lane)

        print(f'action: {action}')
        if action == 'changeLeft':
            print('changeLeft')
            car.stop()
            car.left()
            time.sleep(TIME_TURN)
            car.stop()

            car.forward()
            time.sleep(TIME_FORWARD)
            car.stop()

            car.right()
            time.sleep(TIME_TURN)
            car.stop()
            now_lane = 'left'

        elif action == 'changeRight':
            print('changeRight')
            car.stop()
            car.right()
            time.sleep(TIME_TURN)
            car.stop()

            car.forward()
            time.sleep(TIME_FORWARD)
            car.stop()

            car.left()
            time.sleep(TIME_TURN)
            car.stop()
            now_lane = 'right'
        else:
            print('forward')
            car.forward()
            # time.sleep(1)

        # time.sleep(5)


if __name__ == '__main__':
    main()
