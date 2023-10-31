import time
import asyncio
import requests

async def function1():

    print("func1")
    URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXCLNmhAwuwbU2_tfvDhF8AHYCRJddoyLnSQ&usqp=CAU"
    response = requests.get(URL)
    open("img1.jpg","wb").write(response.content)

    return "Anshu"

async def function2():

    print("func2")
    URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUvP-0YM9juj88rju0VdL45ccleYnkVmb38IokbdYKbXn2ZXVgtiy7sarNTMUDMoOp2PY&usqp=CAU"
    response = requests.get(URL)
    open("img2.jpg","wb").write(response.content)

    return "Harshit"

async def function3():

    print("func3")
    URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIasLRiQ5-GDbPAFwRuiP4XuqzJfN7dgXwXW0bRzuECvV5TOwh6Dt_M_8fBQ4jmtrUmyk&usqp=CAU"
    response = requests.get(URL)
    open("img3.jpg","wb").write(response.content)

    return "Professor"

async def main():

    # This will download images 1 by 1
    # await function1()
    # await function2()
    # await function3()

    # This will download images together
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

    print(L)

asyncio.run(main())
