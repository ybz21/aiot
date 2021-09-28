from flask import Flask
import argparse

from car import Car

parser = argparse.ArgumentParser(description='The args')
parser.add_argument('-p', '--port', default=8888)
args = parser.parse_args()

app = Flask(__name__)
car = Car()


@app.route('/forward')
def forward():
    car.forward()
    return 'ok'


@app.route('/backward')
def backward():
    car.backward()
    return 'ok'


@app.route('/left')
def left():
    car.left()
    return 'ok'


@app.route('/right')
def right():
    car.right()
    return 'ok'


@app.route('/stop')
def stop():
    car.stop()
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port)
