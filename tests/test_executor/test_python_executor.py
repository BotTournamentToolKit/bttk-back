from executor.python import PythonFileExecutor
import pytest
import platform
import asyncio


def test_create():
    this_executor = PythonFileExecutor("test.py")
    assert this_executor.file_path == "test.py"


@pytest.mark.asyncio
async def test_execute():
    print(platform.system())
    this_executor = PythonFileExecutor("testing_bot.py")
    assert await this_executor.turn("1") == "2"
