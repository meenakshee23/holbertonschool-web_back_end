# python_async_function

- Async -> a special function that can pause and resume

- Await -> pauses execution until a task is done

- Asyncio -> is the library used to run async code

- Multiple coroutines can run concurrently (at the same time) 

- asyncio.sleep() -> is non blocking (doesn't stop the whole program)

- asyncio.as_completed() -> returns as tasks finish 

Useful for tasks like waiting, downloading or handling many operations efficiently



Async defines coroutine, 
Await is used to wait for it to finish.

## How to execute an async program with asyncio?

- Use asyncio.run() to start and run your async function.

## How to run concurrent coroutines ?

- Launch multiple coroutines at once so they run together instead of one by one.

## How to create asyncio tasks:
-> Asyncio.create_task() to schedule coroutines to run in the background.


## How to use the random module:

Generate random values, like delays, using functions such as random.uniform()

