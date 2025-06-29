import asyncio

async def async_function():
    # step1
    print("Starting sync process...for egg boiling timer")

    #step2
    
    await asyncio.sleep(10)  # boiling time for egg is 10 seconds
    print("Boiling eggs...please wait")
    #step3
async def async_function1():    
    print("Boiling eggs...please wait 5 seconds more")
    await asyncio.sleep(5)  # wait for 2 seconds more for eggs to boil more

    #step4
async def async_function2():   
    print("Eggs are boiled...please wait 1 second more to cool down")
    await asyncio.sleep(1)  # wait for 1 seconds more for eggs to boil more


async def main():
    await asyncio.gather(
        async_function(),
        async_function1(),
        async_function2()
    )

asyncio.run(main())

print("Eggs are ready! Enjoy your meal!")
print("ASync process completed.")

