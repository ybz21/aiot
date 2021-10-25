from flask import Flask, request, render_template
import argparse
from control.car_speed import SpeedCar
from auto_car import AutoCar

parser = argparse.ArgumentParser(description='The args')
parser.add_argument('-p', '--port', default=8888)
parser.add_argument('-tt', '--time_turn', default=0.8)
parser.add_argument('-tf', '--time_forward', default=1)
parser.add_argument('-s', '--speed', default=0.8)
parser.add_argument('-dt', '--distance_threshold', default=30.0)
parser.add_argument('-r', '--use_rule_action', default=True)
args = parser.parse_args()

car = SpeedCar()
ac = AutoCar(enable_auto_drive=False,
             speed=args.speed,
             time_turn=args.time_turn,
             time_forward=args.time_forward,
             distance_threshold=args.distance_threshold,
             use_rule_action=args.use_rule_action)

ac.start()

app = Flask(__name__)


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
    return render_template('index.html')


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


@app.route('/param')
def set_param():
    global ac
    key = request.args.get('key')
    value = request.args.get('value')
    type_ = request.args.get('type')

    value = get_real_value(value, type_)
    ac.set_param(key, value)
    return 'ok'


def get_real_value(value, type_):
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False

    if '.' in value:
        return float(value)
    elif type_ == 'str':
        return value
    else:
        return int(value)


@app.route('/start_auto')
def enable_auto():
    global ac
    ac.set_enable_auto_drive(True)
    return 'ok'


@app.route('/stop_auto')
def disable_auto():
    global ac
    ac.set_enable_auto_drive(False)
    return 'ok'


@app.route('/c2l')
def change_to_left():
    global ac
    ac.change_to_left()
    return 'ok'


@app.route('/c2r')
def change_to_right():
    global ac
    ac.change_to_right()
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port, debug=True)
