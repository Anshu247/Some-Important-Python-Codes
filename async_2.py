import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("func1")

    return "Anshu"

async def function2():
    await asyncio.sleep(1)
    print("func2")

    return "Harshit"

async def function3():
    await asyncio.sleep(4)
    print("func3")

    return "Professor"

async def main():

    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

    print(L)

asyncio.run(main())
