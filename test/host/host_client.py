import socket
import os
import requests

current_path = os.path.dirname(__file__)


def main():
    hostname = socket.gethostname()

    path = os.path.join(current_path, '_temp.txt')
    os.remove(path)
    cmd = f'ifconfig |grep 10.100 > {path}'
    os.system(cmd)
    with open(path) as f:
        ips = f.read()

    info = {'hostname': hostname, 'ips': ips}
    print(f'info: {info}')
    requests.post("http://172.27.69.60:8333/ips", json=info)


if __name__ == '__main__':
    main()
