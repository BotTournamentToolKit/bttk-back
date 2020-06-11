from executor.python import PythonFileExecutor
import pytest


def test_create():
    this_executor = PythonFileExecutor("test.py")
    assert this_executor.file_path == "test.py"


@pytest.mark.asyncio
async def test_execute():
    this_executor = PythonFileExecutor("testing_bot.py")
    assert await this_executor.turn("1") == "2"
