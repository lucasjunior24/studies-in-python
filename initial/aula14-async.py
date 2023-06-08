import asyncio, time

async def funcao1():
    print("funcao 1")
    await asyncio.sleep(2)
    print("TERMINOU funcao 1")

async def funcao2():
    print("funcao 2")
    await asyncio.sleep(3)
    print("TERMINOU funcao 2")

async def run_f():
    print(f"INICIO: {time.strftime('%X')}")
    task = asyncio.create_task(funcao1())
    task2 = asyncio.create_task(funcao2())

    await task
    await task2
    print(f"termino: {time.strftime('%X')}")


asyncio.run(run_f())