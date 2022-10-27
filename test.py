import asyncio


async def async_func():
    print("Velotio ...")
    await asyncio.sleep(1)
    print("... Technologies!")
    return 4


a = asyncio.run(async_func())
print(a)
