# pytest-nuttx-testing-sample
This repository contains sample code for testing NuttX applications using pytest.

Link to the complete article regarding this example:

# What's in here

- **communication.py**: wraps the pyserial package in a simple serial communication that is used by pytest.
- **conftest.py**: general pytest setup and configuration.
- **test_\*.py**: test files.

# Setting up the environment
Follow those steps to bring up the test environment:

1. Create a Python virtual environment
    
    `$ python3 -m venv venv`
2. Activate the virtual environment

    `$ source venv/bin/activate`
3. Install the required packages

    `$ pip3 install -r requirements.txt`

# Running Tests

Simply call pytest with the proper arguments defined in conftest. Make sure to enter your actual board name and correct serial port.

```$ pytest -v --board eps32h2-devkit --usbport /dev/tttyUSB0```
