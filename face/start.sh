#!/bin/bash
set -ex

CAMERA_NO=$1

nohup python3 face_server.py > face_server.log 2>&1 &

if [ ! -n "$CAMERA_NO" ];then
  python3 face_door.py
else
  python3 face_door.py --camera_no=$CAMERA_NO
fi