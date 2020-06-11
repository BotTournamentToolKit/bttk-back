from executor.python import PythonFileExecutor
import pytest
import platform
import asyncio


def test_create():
    this_executor = PythonFileExecutor("test.py")
    assert this_executor.file_path == "test.py"


@pytest.fixture
def event_loop():
    if platform.system() == "Windows":
        loop = asyncio.ProactorEventLoop()
    else:
        loop = asyncio.get_event_loop()
    yield loop
    # loop.close()


@pytest.mark.asyncio
async def test_execute():
    this_executor = PythonFileExecutor("bots_for_testing/testing_bot.py")
    assert await this_executor.turn("1") == "2"


@pytest.mark.asyncio
async def test_timeout():
    this_executor = PythonFileExecutor("bots_for_testing/testing_recur.py", timeout=1.0)
    with pytest.raises(TimeoutError):
        await this_executor.turn("1")


@pytest.mark.asyncio
async def test_fail():
    this_executor = PythonFileExecutor("bots_for_testing/testing_fail.py")
    with pytest.raises(RuntimeError):
        await this_executor.turn("1")
