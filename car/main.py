from observe.lidar import get_distance
from orient.observation import generate_obs

from decision.decision import Decision
from control.car_speed import SpeedCar

import time

TIME_TURN = 1
TIME_FORWARD = 1


def main():
    now_lane = 'right'
    decision = Decision()
    car = SpeedCar()

    while True:
        distance = get_distance()

        obs = generate_obs(distance, now_lane)

        action = decision.get_action(obs)
        print(f'---distance: {distance}, action: {action}')

        if action == 'changeLeft':
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
            car.forward()


if __name__ == '__main__':
    main()
