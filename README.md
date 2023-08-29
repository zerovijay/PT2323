# PT2323 6-Channel Audio Selector IC - Python Library

## Overview

The `PT2323` class provides a MicroPython implementation for controlling the PT2323 6-Channel Audio Selector IC using
I2C communication. This library offers an intuitive interface for managing audio sources, channel muting, master mute,
enhance surround mode, and mixed channel setups.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
    - [Initialization](#initialization)
    - [Setting Input Source](#setting-input-source)
    - [Master Mute](#master-mute)
    - [Channel Mute](#channel-mute)
    - [Enhance Surround](#enhance-surround)
    - [Mixed Channel Setup](#mixed-channel-setup)
- [Documentation](#documentation)
- [Getting Started](#getting-started)
- [Class API Reference](#class-api-reference)
- [Contributions](#contributions)
- [Requirements](#requirements)
- [Credits](#credits)
- [License](#license)

## Installation

1. Download the `pt2323.py` file from this [repository.]()
2. Copy the file to your MicroPython device, placing it in the same directory as your project.

## Usage

### Initialization

Import the `PT2323` class and initialize it with your I2C port:

```python
from PT2323 import PT2323
from machine import Pin, I2C

# Initialize the I2C port (replace with your pins)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Initialize the PT2323 instance
pt2323 = PT2323(port=i2c)
```

### Setting Input Source

Set the input source to route audio stereo group or the 6-channel input:

```python
# Set input source to the third stereo group (0-4)

pt2323.input_source(source=2)
```

### Master Mute

Enable or disable the master mute for all channels:

```python
# Mute all channels

pt2323.master_mute(status=True)

# Unmute all channels

pt2323.master_mute(status=False)  # or pt2323.master_mute()
```

### Channel Mute

Enable or disable mute for a specific channel (0-5):

```python
# Mute channel 2

pt2323.channel_mute(channel=1, status=True)

# Unmute channel 4

pt2323.channel_mute(channel=3, status=False)
```

### Enhance Surround

Enable or disable the surround sound enhancement:

```python
# Enable surround mode

pt2323.enhance_surround(status=True)

# Disable surround mode

pt2323.enhance_surround(status=False)
```

### Mixed Channel Setup

Enable or disable the 2-channel to 6-channel audio translation:

```python
# Enable mixed channel setup

pt2323.mixed_channel(status=True)

# Disable mixed channel setup

pt2323.mixed_channel(status=False)
```

## Documentation

For comprehensive details about the PT2323 functionality and usage, please refer to the
official [PT2323 documentation](/PT2323/PT2323_PrincetonTechnology.pdf).

The class documentation offers in-depth explanations, usage examples, and detailed parameter information for each
method.

## Getting Started

If you're new to the PT2323 6-Channel Audio Selector IC and its usage with the provided MicroPython code, here's how to
start:

- Clone or download this [repository]() to your local machine.
- Review the class documentation to understand available methods and usage.
- Utilize the ` __doc__` or `__str__` method to explore class details.
- Follow the example usage provided in the Usage section of this [README.md]() file to integrate the PT2323 class into
  your
  project.
- If you have any suggestions or find issues, feel free to contribute by creating issues or pull requests on
  the [repository.]()

## Class API Reference

The class methods are documented in the PT2258 class documentation. It includes the following methods:

- `__init__(self, port: I2C = None) -> None`: Initialize the PT2323 instance.
- `input_source(source: int) -> None`: Set the input source for the PT2323.
- `master_mute(status: bool = False) -> None`: Enable or disable master mute for all channels.
- `channel_mute(channel: int, status: bool = False) -> None`: Enable or disable mute for a specific channel.
- `enhance_surround(status: bool = False) -> None`: Enable or disable the surround functionality.
- `mixed_channel(status: bool = False) -> None`: Enable or disable the 2-channel to 6-channel translation.

## Contributions

If you find any issues or have suggestions for improvements, feel free to contribute by creating issues or pull requests
on the [repository.]()

## Requirements

- [Python](https://www.python.org/)
- [MicroPython](https://micropython.org/)
- [MicroPython Compatible Boards](https://micropython.org/download/)
- PT2323 6-Channel Audio Selector IC

## Credits

This code was created by [vijay](https://github.com/zerovijay) We appreciate your contributions to enhance this project!

## License

This project is licensed under the [MIT License.]()
