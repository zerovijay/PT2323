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

        # Function definition registers.
        self.__INPUT_SWITCH = const(0xC0)
        self.__MASTER_MUTE = const(0xFE)
        self.__ENHANCE_SURROUND = const(0xD0)
        self.__CHANNEL_MIX = const(0x90)

        # Source index lookup.
        self.__INPUT_SOURCE: tuple = (
            0x08,  # index 0: Input Stereo Group 1
            0x09,  # index 1: Input Stereo Group 2
            0x0A,  # index 2: Input Stereo Group 3
            0x0B,  # index 3: Input Stereo Group 4
            0x07,  # index 4: 6-Channel Input
        )

        # Mute registers lookup.
        self.__MUTE_REGISTERS: tuple = (
            0xF0,  # index 0: Channel 1
            0xF2,  # index 1: Channel 2
            0xF4,  # index 2: Channel 3
            0xF6,  # index 3: Channel 4
            0xF8,  # index 4: Channel 5
            0xFA,  # index 5: Channel 6
        )

        # Initialize the PT2323 IC.
        self.__init_pt2323()

    def __write_pt2323(self, write_data: int) -> None:
        """
        Write an instruction to the PT2323.

        Note: This method is not intended for public use.

        :param write_data: The instruction data to be written to PT2323.
        :type write_data: int
        :raises RuntimeError: If the PT2323 is not found on the I2C bus or if there is an I2C communication error.
        :return: None
        """

        try:
            self.__I2C.writeto(self.__PT2323_ADDR, bytearray([write_data]))
        except OSError as error:
            if error.args[0] == 5:
                raise RuntimeError(
                    "Oops! The PT2323 encountered a communication error while trying to perform the operation."
                )
            else:
                raise RuntimeError(
                    f"Sorry, there was a communication error with the PT2323. The error message: {error}"
                )

    def __init_pt2323(self) -> None:
        """
        Initialize the PT2323 by checking its presence on the I2C bus.

        Note: This method is not intended for public use.

        :raises OSError: If the PT2323 is not found on the bus.
        :return: None
        """

        utime.sleep_ms(300)
        if self.__PT2323_ADDR not in self.__I2C.scan():
            raise OSError("Oops! PT2323 not found on the I2C bus.")

    def input_source(self, source: int) -> None:
        """
        Set the input source for the PT2323.

        :param source: The input source index. Should be an integer between 0 and 4.
        :type source: int
        :raises ValueError: If the input source index is outside the valid range.
        :return: None
        """

        if not 0 <= source <= 4:
            raise ValueError('Oops! Source index is invalid. The input source must be within the range of 0 to 4.')

        self.__write_pt2323(self.__INPUT_SWITCH | self.__INPUT_SOURCE[source])

    def master_mute(self, status: bool = False) -> None:
        """
        Enable or disable master mute for all channels.

        Note: Function by default False.

        :param status: True to mute all channels, False to un_mute.
        :type status: bool
        :raises ValueError: If the provided status is not a boolean value.
        :return: None
        """

        if not isinstance(status, bool):
            raise ValueError("Oops! Invalid master mute status value. It should be a boolean (True or False).")

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
        :raises ValueError: If the provided status is not a boolean value.
        :return: None
        """

        if not 0 <= channel <= 5:
            raise ValueError('Oops! Channel index is invalid. It should be within the range of 0 to 5.')

        if not isinstance(status, bool):
            raise ValueError("Oops! Invalid channel mute status value. It should be a boolean (True or False).")

        self.__write_pt2323(self.__MUTE_REGISTERS[channel] | status)

    def enhance_surround(self, status: bool = False) -> None:
        """
        Enable or disable the surround functionality.

        Note: Function by default False.

        :param status: True to enable surround, False to disable.
        :type status: bool
        :raises ValueError: If the provided status is not a boolean value.
        :return: None
        """

        if not isinstance(status, bool):
            raise ValueError("Oops! Invalid enhance surround status value. It should be a boolean (True or False).")

        self.__write_pt2323(self.__ENHANCE_SURROUND | (not status))

    def mixed_channel(self, status: bool = False) -> None:
        """
        Enable or disable the 2-channel to 6-channel translation.

        Note: Function by default False

        :param status: True to enable translation, False to disable.
        :type status: bool
        :raises ValueError: If the provided status is not a boolean value.
        :return: None
        """

        if not isinstance(status, bool):
            raise ValueError("Oops! Invalid mixed channel status value. It should be a boolean (True or False).")

        self.__write_pt2323(self.__CHANNEL_MIX | status)

    # The end.
