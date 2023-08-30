from machine import Pin, I2C

from PT2323 import PT2323

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

pt2323 = PT2323(port=i2c)


def main():
    ...
    while True:
        ...


if __name__ == '__main__':
    main()
