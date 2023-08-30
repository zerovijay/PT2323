import utime
from machine import I2C
from micropython import const


class PT2323:

    def __init__(self, port: I2C = None) -> None:
        """
        Initialize the PT2323 6-Channel Audio Selector IC using I2C communication.

        :param port: An instance of the I2C bus connected to the PT2323.
        :type port: I2C
        :raises ValueError: If the I2C object is not provided.
        """

        if port is None:
            raise ValueError("Oops! The I2C object is missing.")
        self.__I2C: I2C = port

        self.__PT2323_ADDR = const(0x94)  # Address of PT2323
        # Function definition bytes
        self.__INPUT_SWITCH = const(0xC0)
        self.__MASTER_MUTE = const(0xFE)
        self.__ENHANCE_SURROUND = const(0xD0)
        self.__CHANNEL_MIX = const(0x90)

        self.__INPUT_SOURCE: tuple = (  # Source index lookup.
            0x08,  # index 0: Input Stereo Group 1
            0x09,  # index 1: Input Stereo Group 2
            0x0A,  # index 2: Input Stereo Group 3
            0x0B,  # index 3: Input Stereo Group 4
            0x07,  # index 4: 6-Channel Input
        )
        self.__MUTE_REGISTERS: tuple = (  # Mute register lookup.
            0xF0,  # index 0: Channel 1 - Front Left mute register.
            0xF2,  # index 1: Channel 2 - Front Right mute register.
            0xF4,  # index 2: Channel 3 - Center mute register.
            0xF6,  # index 3: Channel 4 - Subwoofer mute register.
            0xF8,  # index 4: Channel 5 - Surround Left mute register.
            0xFA,  # index 5: Channel 6 - Surround Right mute register.
        )

        self.__init_pt2323()  # Initialize the PT2323 IC.

    def __write_pt2323(self, write_data: int) -> None:
        """
        Write an instruction to the PT2323.

        :param write_data: The instruction data to be written to PT2323.
        :type write_data: int
        :raises RuntimeError: If the PT2323 is not found on the I2C bus or if there is an I2C communication error.
        :return: None
        """

        try:
            self.__I2C.writeto(self.__PT2323_ADDR, bytearray([write_data]))
        except OSError as e:
            if e.args[0] == 5:
                raise RuntimeError(
                    "Oops! The PT2323 encountered a communication error while trying to perform the operation."
                )
            else:
                raise RuntimeError(
                    f"Sorry, there was a communication error with the PT2323. The error message: {e}"
                )

    def __init_pt2323(self) -> None:
        """
        Initialize the PT2323 by checking its presence on the I2C bus.

        :raises OSError: If the PT2323 is not found on the bus.
        :return: None
        """

        utime.sleep_ms(300)
        if self.__PT2323_ADDR not in self.__I2C.scan():
            raise OSError("PT2323 not found on the I2C bus!")

    def input_source(self, source: int) -> None:
        """
        Set the input source for the PT2323.

        :param source: The input source index. Should be an integer between 0 and 4.
        :type source: int
        :raises ValueError: If the input source index is outside the valid range.
        :return: None
        Example:
        To set the input source to the third stereo group:
        # pt2323.input_source(2)
        """

        if not 0 <= source <= 4:
            raise ValueError('Source index is invalid! The input source must be within the range of 0 to 4.')

        self.__write_pt2323(self.__INPUT_SWITCH | self.__INPUT_SOURCE[source])

    def master_mute(self, status: bool = False) -> None:
        """
        Enable or disable master mute for all channels.
        Note: Function by default False.

        :param status: True to mute all channels, False to un_mute.
        :type status: bool
        :return: None
        """

        self.__write_pt2323(self.__MASTER_MUTE | status)

    def channel_mute(self, channel: int, status: bool = False) -> None:
        """
        Enable or disable mute for a specific channel.
        Note: Function by default False.

        :param channel: The channel index to mute. Should be an integer between 0 and 5.
        :type channel: int
        :param status: True to mute the channel, False to un_mute.
        :type status: bool
        :raises ValueError: If the channel index is outside the valid range.
        :return: None
        """

        if not 0 <= channel <= 5:
            raise ValueError('Channel index is invalid! It should be within the range of 0 to 5.')

        self.__write_pt2323(self.__MUTE_REGISTERS[channel] | status)

    def enhance_surround(self, status: bool = False) -> None:
        """
        Enable or disable the surround functionality.
        Note: Function by default False.

        :param status: True to enable surround, False to disable.
        :type status: bool
        :return: None
        """

        self.__write_pt2323(self.__ENHANCE_SURROUND | (False if status else True))

    def mixed_channel(self, status: bool = False) -> None:
        """
        Enable or disable the 2-channel to 6-channel translation.
        Note: Function by default False

        :param status: True to enable translation, False to disable.
        :type status: bool
        :return: None
        """

        self.__write_pt2323(self.__CHANNEL_MIX | status)

    def __str__(self):
        description = (
            """
            Initialize the PT2323 6-Channel Audio Selector IC using I2C communication.

            :param port: An instance of the I2C bus connected to the PT2323.
            :type port: I2C
            :raises ValueError: If the I2C object is not provided.

            The PT2323 is a versatile 6-channel audio selector IC that allows you to manage audio sources.
            This class provides an interface to control the PT2323's input source selection,
            master mute, individual channel mute, enhance surround mode, and mixed channel setup. 
            It offers a convenient way to integrate audio source management into your projects,
            enhancing the user experience of audio playback.

            Public Methods:
            - __init__(self, port: I2C = None) -> None:
                Initialize the PT2323 instance.

            - input_source(source: int) -> None:
                Set the input source for the PT2323.

            - master_mute(status: bool = False) -> None:
                Enable or disable master mute for all channels.

            - channel_mute(channel: int, status: bool = False) -> None:
                Enable or disable mute for a specific channel.

            - enhance_surround(status: bool = False) -> None:
                Enable or disable the surround functionality.

            - mixed_channel(status: bool = False) -> None:
                Enable or disable the 2-channel to 6-channel translation.
            """
        )
        return description

    # The end
