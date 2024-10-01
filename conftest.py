import pytest
from communication import SerialCommunication


def pytest_addoption(parser):
    parser.addoption(
        "--usbport", action="store", default="/dev/ttyUSB0", help="USB port"
    )
    parser.addoption(
        "--board", action="store", required=True, help="Espressif devkit"
    )


@pytest.fixture(scope="session", name="target")
def serial_comm_fixture(request):
    serial = SerialCommunication(request.config.getoption("--usbport"))
    yield serial
    serial.close()


@pytest.fixture(scope="session", name="board")
def board_name(request):
    yield request.config.getoption("--board")
