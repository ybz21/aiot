FROM kumatea/pytorch:1.9.0-full

RUN apt-get update && apt-get install -y gcc-arm-linux-gnueabihf \
    python3 \
    python3-dev \
    python3-pip \
    vim \
    python3-opencv

RUN pip3 install Jetson.GPIO \
    flask \
    highway-env \
    stable-baselines3 -i https://pypi.tuna.tsinghua.edu.cn/simple

