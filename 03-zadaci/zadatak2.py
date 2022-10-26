import asyncio
import numpy
import psutil

from time import sleep

async def afunc1():
    for i in range(10):
        numpy.random.normal(loc=0.0, scale=1.0, size=1000000)
        await asyncio.sleep(0.9)

async def afunc2():
   x = psutil.cpu_percent(10)
   return x

async def main():
    var1 = asyncio.create_task(afunc1())
    var2 = asyncio.create_task(afunc2())
    await var1
    var3 = await var2
    print(var3)    

if __name__ == "__main__":
    asyncio.run(main())

