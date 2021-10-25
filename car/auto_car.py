from observe.lidar import get_distance
from orient.observation import generate_obs

from decision.decision import Decision
from control.car_speed import SpeedCar

import time
import os
import threading

current_dir = os.path.dirname(__file__)


class AutoCar(threading.Thread):
    def __init__(self, enable_auto_drive=False,
                 speed=0.5,
                 time_turn=1,
                 time_forward=2,
                 distance_threshold=35.0,
                 use_rule_action=True):
        threading.Thread.__init__(self)
        self.enable_auto_drive = enable_auto_drive
        self.now_lane = 'right'
        self.decision = Decision()
        self.car = SpeedCar()

        self.speed = speed
        self.time_turn = time_turn
        self.time_forward = time_forward
        self.distance_threshold = distance_threshold
        self.use_rule_action = use_rule_action

    def set_param(self, key, value):
        self.__dict__[key] = value
        print(f'__dict__: {self.__dict__}')

    def set_enable_auto_drive(self, auto):
        self.enable_auto_drive = auto
        if not auto:
            self.car.stop()

    def run(self):
        while True:
            if self.enable_auto_drive:
                self.auto_drive()
            else:
                time.sleep(5)
                print('---sleep ')

    def auto_drive(self):
        print('---auto drive1')
        while self.enable_auto_drive:
            print('---auto drive2')

            distances = []
            for i in range(3):
                distance = get_distance()
                distances.append(distance)

            distance = sum(distances) / 3.0
            print("distance: %.1f cm" % distance)

            if self.use_rule_action:
                action = self.get_rule_action(distance)
            else:
                action = self.get_rl_action(distance)

            print(f'action: {action}')

            # TODO: move this in control
            if action == 'changeLeft':
                print('changeLeft')
                self.change_to_left()

            elif action == 'changeRight':
                print('changeRight')
                self.change_to_right()

            else:
                print('forward')
                self.car.forward(self.speed)

    def change_to_left(self):
        self.car.stop()
        self.car.left(self.speed)
        time.sleep(self.time_turn)
        self.car.stop()

        self.car.forward(self.speed)
        time.sleep(self.time_forward)
        self.car.stop()

        self.car.right(self.speed)
        time.sleep(self.time_turn)
        self.car.stop()
        self.now_lane = 'left'

    def change_to_right(self):
        self.car.stop()
        self.car.right(self.speed)
        time.sleep(self.time_turn)
        self.car.stop()

        self.car.forward(self.speed)
        time.sleep(self.time_forward)
        self.car.stop()

        self.car.left(self.speed)
        time.sleep(self.time_turn)
        self.car.stop()
        self.now_lane = 'right'

    def get_rule_action(self, distance):
        if distance < self.distance_threshold and self.now_lane == 'right':
            return 'changeLeft'
        elif distance < self.distance_threshold and self.now_lane == 'left':
            return 'changeRight'
        else:
            return 'forward'

    def get_rl_action(self, distance):
        obs = generate_obs(distance, self.now_lane, threshold=self.distance_threshold)
        action, raw_action = self.decision.get_action(obs)
        print(f'rl raw_action:{raw_action}')
        return action

# if __name__ == '__main__':
#     ac = AutoCar()
#     ac.start()
