#!/bin/bash

nohup python3 face_server.py > face_server.log 2>&1 &
python3 face_door.py