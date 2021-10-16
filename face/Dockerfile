FROM python:3.8

RUN apt-get update && apt-get install  -y --fix-missing \
                                          libopencv-dev \
                                          python3-opencv \
                                          vim \
                                          build-essential \
                                          cmake \
                                          gfortran \
                                          git \
                                          wget \
                                          curl \
                                          graphicsmagick \
                                          libgraphicsmagick1-dev \
                                          libatlas-base-dev \
                                          libavcodec-dev \
                                          libavformat-dev \
                                          libgtk2.0-dev \
                                          libjpeg-dev \
                                          liblapack-dev \
                                          libswscale-dev \
                                          pkg-config \
                                          python3-dev \
                                          python3-numpy \
                                          software-properties-common \
                                          zip \
                                          && apt-get clean

RUN pip install face_recognition flask -i https://pypi.tuna.tsinghua.edu.cn/simple