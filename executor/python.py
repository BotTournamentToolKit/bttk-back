from executor import Executor
import aiofiles
import asyncio


class PythonFileExecutor(Executor):
    def __init__(self, path: str):
        super(PythonFileExecutor, self).__init__(path)

    async def turn(self, field: str) -> str:
        # Write a field into a file.
        async with aiofiles.open("field.txt", mode="w") as f:
            await f.write(field)

        # Run a program with time out
        proc = await asyncio.create_subprocess_shell(f"python {self.file_path}")

        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=5.0)

        if proc.returncode != 0:
            raise NotImplementedError()

        # Read a turn from a file
        async with aiofiles.open("turn.txt", mode="r") as f:
            result = await f.read()

        # Return turn
        return result
