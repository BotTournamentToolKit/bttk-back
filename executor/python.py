from executor import Executor
import aiofiles
import asyncio
from pathlib import Path


class PythonFileExecutor(Executor):
    def __init__(self, path: str):
        super(PythonFileExecutor, self).__init__(path)

    async def turn(self, field: str) -> str:
        parent_path = Path(self.file_path).parent
        file_path = Path(self.file_path).name

        # Write a field into a file.
        async with aiofiles.open(f"{parent_path}/field.txt", mode="w") as f:
            await f.write(field)

        # Run a program with time out
        proc = await asyncio.create_subprocess_shell(
            f"python {file_path}", cwd=parent_path
        )

        try:
            await asyncio.wait_for(proc.communicate(), timeout=5.0)
        except:
            proc.kill()
            raise TimeoutError()

        if proc.returncode != 0:
            raise RuntimeError()

        # Read a turn from a file
        async with aiofiles.open(f"{parent_path}/turn.txt", mode="r") as f:
            result = await f.read()

        # Return turn
        return result
