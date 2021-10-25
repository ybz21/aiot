from flask import Flask, request, render_template

app = Flask(__name__)

hostname_dict = {}


@app.route('/ips', methods=['POST'])
def ips():
    global hostname_dict

    content = request.json
    hostname = content['hostname']
    # ips = content['ips']
    ips = request.remote_addr
    hostname_dict[hostname] = ips
    print(hostname_dict)

    return 'ok'


@app.route('/')
def index():
    global hostname_dict
    return hostname_dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8333, debug=True)
