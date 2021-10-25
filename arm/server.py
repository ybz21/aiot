from flask import Flask, request, render_template
import argparse
from control.arm import Arm

parser = argparse.ArgumentParser(description='The args')
parser.add_argument('-p', '--port', default=8888)
parser.add_argument('-tt', '--time_turn', default=0.8)
parser.add_argument('-tf', '--time_forward', default=1)
parser.add_argument('-s', '--speed', default=0.8)
parser.add_argument('-dt', '--distance_threshold', default=30.0)
parser.add_argument('-r', '--use_rule_action', default=True)
args = parser.parse_args()

arm = Arm()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def forward():
    print('start')
    arm.start
    return 'ok'

@app.route('/stop')
def stop():
    arm.stop()
    return 'ok'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port, debug=True)
