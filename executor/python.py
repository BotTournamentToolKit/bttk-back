from executor import Executor
import aiofiles
import asyncio


class PythonFileExecutor(Executor):
    async def turn(self, field: str) -> str:

        # Write a field into a file.
        async with aiofiles.open(f"{self.parent_path}/field.txt", mode="w") as f:
            await f.write(field)

        # Run a program with time out
        proc = await asyncio.create_subprocess_shell(
            f"python {self.file_name}", cwd=self.parent_path
        )

        try:
            await asyncio.wait_for(proc.communicate(), timeout=self.timeout)
        except asyncio.futures.TimeoutError:
            proc.kill()
            raise TimeoutError()

        if proc.returncode != 0:
            raise RuntimeError()

        # Read a turn from a file
        async with aiofiles.open(f"{self.parent_path}/turn.txt", mode="r") as f:
            result = await f.read()

        # Return turn
        return result
