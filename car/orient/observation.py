# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2021/10/20 6:02 下午
# @Author       : yanbingzheng@4paradigm.com
# @File         : orient.py
# @Description  : xxxxx

obs_length = 5


def generate_obs(distance, now_lane, threshold=35):
    has_car = False
    if distance < threshold:
        has_car = True

    current_lane = [0] * obs_length

    if has_car:
        current_lane = [1] * obs_length
        current_lane[0] = 0

    if now_lane == 'right':
        left_lane = [0] * obs_length
        right_lane = [1] * obs_length
        if not has_car:
            left_lane = [1] * obs_length
    else:
        left_lane = [1] * obs_length
        right_lane = [0] * obs_length
        if not has_car:
            right_lane = [1] * obs_length

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


def test_generate_obs():
    generate_obs(10, 'right')

    generate_obs(100, 'right')

    generate_obs(10, 'left')

    generate_obs(100, 'left')


if __name__ == '__main__':
    test_generate_obs()
