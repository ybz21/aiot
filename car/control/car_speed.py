import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


class SpeedCar:
    def __init__(self, left_motor=[35, 36], right_motor=[37, 38], left_pwm=32, right_pwm=33):
        self.left_motor = left_motor
        self.right_motor = right_motor

        GPIO.setup(left_pwm, GPIO.OUT)
        GPIO.setup(right_pwm, GPIO.OUT)
        self.pwm = [GPIO.PWM(left_pwm, 100), GPIO.PWM(right_pwm, 100)]

        GPIO.setup(self.left_motor[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.right_motor[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.left_motor[1], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.right_motor[1], GPIO.OUT, initial=GPIO.LOW)

        self.left_speed = 0
        self.right_speed = 0

        self.pwm[0].start(100)
        self.pwm[1].start(100)

    def set_motors(self, left_speed=1.0, right_speed=1.0):
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        self.left_speed = ((left_speed - (-1)) / 2) * 100
        self.right_speed = ((right_speed - (-1)) / 2) * 100
        print()
        print()
        self.pwm[0].ChangeDutyCycle(self.left_speed)
        self.pwm[1].ChangeDutyCycle(self.right_speed)

    def forward(self, speed=1.0, duration=None):
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        GPIO.output(self.left_motor[1], GPIO.LOW)
        GPIO.output(self.right_motor[1], GPIO.LOW)

        self.speed = ((speed - (-1)) / 2) * 100
        self.pwm[0].ChangeDutyCycle(self.speed)
        self.pwm[1].ChangeDutyCycle(self.speed)

    def backward(self, speed=1.0):
        GPIO.output(self.left_motor[0], GPIO.LOW)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        GPIO.output(self.left_motor[1], GPIO.HIGH)
        GPIO.output(self.right_motor[1], GPIO.HIGH)

        self.speed = ((speed - (-1)) / 2) * 100
        self.pwm[0].ChangeDutyCycle(self.speed)
        self.pwm[1].ChangeDutyCycle(self.speed)

    def right(self, speed=1.0):
        GPIO.output(self.left_motor[0], GPIO.LOW)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        GPIO.output(self.left_motor[1], GPIO.HIGH)
        GPIO.output(self.right_motor[1], GPIO.LOW)

        self.speed = ((speed - (-1)) / 2) * 100
        self.pwm[0].ChangeDutyCycle(self.speed)
        self.pwm[1].ChangeDutyCycle(self.speed)

    def left(self, speed=1.0):
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        GPIO.output(self.left_motor[1], GPIO.LOW)
        GPIO.output(self.right_motor[1], GPIO.HIGH)

        self.speed = ((speed - (-1)) / 2) * 100
        self.pwm[0].ChangeDutyCycle(self.speed)
        self.pwm[1].ChangeDutyCycle(self.speed)

    def stop(self):
        GPIO.output(self.left_motor[0], GPIO.LOW)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        GPIO.output(self.left_motor[1], GPIO.LOW)
        GPIO.output(self.right_motor[1], GPIO.LOW)

        self.left_speed = 0
        self.right_speed = 0
        self.pwm[0].ChangeDutyCycle(self.left_speed)
        self.pwm[1].ChangeDutyCycle(self.right_speed)


def main():
    r = SpeedCar()

    print('forward')
    r.forward()
    time.sleep(5)

    print('forward-0.2')
    r.forward(speed=0.2)
    time.sleep(5)

    print('backward')
    r.backward()
    time.sleep(5)

    print('left')
    r.left()
    time.sleep(5)

    print('right')
    r.right()
    time.sleep(5)

    print('stop')
    r.stop()
    time.sleep(5)


if __name__ == '__main__':
    main()
