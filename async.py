import asyncio

async def p(x):
    print(x)

async def task(x):
    while True:
        await p(x)

loop = asyncio.get_event_loop()
loop.create_task(task(1))
loop.create_task(task(2))

# only 1 but never 2
loop.run_forever()
