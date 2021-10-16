from flask import Flask, request, render_template
import argparse
import base64
import os
import csv

from model import FaceDoor

current_path = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description='The args')
parser.add_argument('-p', '--port', default=8888)
args = parser.parse_args()

app = Flask(__name__)

csv_path = os.path.join(current_path, 'results/face.csv')


@app.route('/')
def index():
    fds = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            fd = FaceDoor(row['name'], row['time'], row['image'])
            fds.append(fd)
    fds.reverse()
    return render_template('index.html', entries=fds)
    # return render_template('index.html')


def return_img_stream(img_local_path):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream


@app.route('/image')
def image_detail():
    name = request.args.get("name")
    img_path = os.path.join(current_path, 'results', name)
    img_stream = return_img_stream(img_path)
    return render_template('detail.html', img_stream=img_stream)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port, debug=True)
