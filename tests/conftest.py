import pytest
import platform
import asyncio


@pytest.fixture
def event_loop():
    if platform.system() == "Windows":
        loop = asyncio.ProactorEventLoop()
    else:
        loop = asyncio.get_event_loop()
    yield loop
    loop.close()
