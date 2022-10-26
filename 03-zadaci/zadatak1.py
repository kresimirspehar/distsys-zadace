import asyncio
import os

async def afun1(param_list):
    await asyncio.sleep(0.2)
    return [{"naziv": i, "velicina ": os.path.getsize(i) } for i in param_list]

def fun2(datoteka):
    for i in datoteka:
        x = open(i, "w")
        for a in range(1, 10000):
            x.write(str(a))
        x.close()

async def main():
    datoteke = ["datoteka1", "datoteka2", "datoteka3"]
    for i in datoteke:
            fp = open(i, 'w')
            fp.close()
    var1 = asyncio.create_task(afun1(datoteke))
    print(fun2(datoteke))
    await var1
    print(var1.result())
    
if __name__ == "__main__":
    asyncio.run(main())

