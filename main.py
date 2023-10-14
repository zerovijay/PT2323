import utime
from machine import Pin, I2C

from PT2323 import PT2323

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

pt2323 = PT2323(port=i2c)


# Example function: to configer the channels as a 2.1 audio setup
def channel_config() -> None:
    """
    This function simulate the channels. like 2.1, 4.1 or stereo.

    :return: None
    """
    pt2323.channel_mute(channel=2, status=True)  # channel CT Muted
    pt2323.channel_mute(channel=4, status=True)  # channel SL Muted
    pt2323.channel_mute(channel=5, status=True)  # channel SR Muted


if __name__ == '__main__':
    print("Hello, World!")
    utime.sleep(1)
    # select the audio sources from 4 Input Stereo Group or one 6 channel input
    print("Source: Stereo Group 1 was selected.")
    pt2323.input_source(0)  # Input Stereo Group 1 was selected
    utime.sleep(1)

    # Enable or disable the 2channel to 6channel translate
    print("Enable the 2 channel to 6channel translate")
    pt2323.mixed_channel(status=True)
    utime.sleep(1)
    print("Disable the 2 channel to 6channel translate")
    pt2323.mixed_channel(status=False)

    print("Checking as a 2.1.")
    pt2323.mixed_channel(status=True)
    channel_config()  # Make the audio output as a 2.1
    utime.sleep(2)

    print("Checking as 5.1.")
    for channel in range(6):
        pt2323.channel_mute(channel=channel, status=False)  # Un_mute all channels
        pt2323.input_source(4)  # select the audio sources 6 channel input
    utime.sleep(2)

    print("Enable surround sound.")
    pt2323.enhance_surround(status=True)
    utime.sleep(1)
    print("Disable surround sound.")
    pt2323.enhance_surround(status=False)

    while True:
        # Main code here.
        utime.sleep(0.1)
