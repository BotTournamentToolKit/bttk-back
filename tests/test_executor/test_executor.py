import pytest
from executor import Executor


@pytest.mark.asyncio
async def test_executor_interface():
    ex = Executor("foo")
    with pytest.raises(NotImplementedError):
        await ex.turn("bar")
