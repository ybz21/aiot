from flask import Flask, request,render_template
import argparse
from car_speed import SpeedCar

parser = argparse.ArgumentParser(description='The args')
parser.add_argument('-p', '--port', default=8888)
args = parser.parse_args()

app = Flask(__name__)
car = SpeedCar()

def get_speed():
    speed = request.args.get('speed')
    if speed is None:
        speed = 1.0
    else:
        speed = float(speed)

    print(f'speed: {speed}')
    return speed

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/forward')
def forward():
    print('forward')
    speed = get_speed()
    car.forward(speed=speed)
    return 'ok'


@app.route('/backward')
def backward():
    speed = get_speed()
    car.backward(speed=speed)
    return 'ok'


@app.route('/left')
def left():
    speed = get_speed()
    car.left(speed=speed)
    return 'ok'


@app.route('/right')
def right():
    speed = get_speed()
    car.right(speed=speed)
    return 'ok'


@app.route('/stop')
def stop():
    car.stop()
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port, debug=True)
