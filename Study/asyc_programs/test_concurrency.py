'''
Concurrency:
    Threading
    Async IO
    Parallelism
        multiporcessing

Parallelism: (for CPU-bound tasks)
    perform multiple operations at the same time.
    multiprocessing
Concurrency:
    multiple tasks have the ability to run in an overlapping manner.
Threading: (for IO-bound tasks)
    concurrent executing model
    multiple threads take turns executing tasks.
Asynchronous routine
    able to pause while waiting on its ultiate result and let other routines run 
    in the meantime facilitates concurrent execution.

A program's event loop comunicates with multiple tasks 
to let each take turns running at the optimal time.

<aync/await syntax and native coroutines>

Corouine:
    A specialized version of a Python generator function

The Rules of Async IO
    asyc def: introduces a native coroutine or an asynchronous generator
    await: passes function control back to the event loop
    it is less common to use yiedl in an async def block
    await f():
        f() should be an awiatable object
        a corutine or
        an object definition an .__await() method that returns an iterator
    @asyncio.coroutine: a generator-based coroutine: outdated
    
'''

import asyncio
import random

c = (
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m"
)


async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low: retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"----> Finished: makerandom({idx}) == {i}" + c[0])
    return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")


'''
async def count():
    print('One')
    await asyncio.sleep(1)
    print('Two')


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed: 0.2f} seconds.")
'''
