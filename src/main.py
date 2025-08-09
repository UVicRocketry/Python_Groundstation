#written by Khephren Gould for Uvic Rocketry June 25, 2025
import logger as log
import asyncio

async def monitor_user_input():
    while True:
        user_input = await asyncio.to_thread(input)
        if user_input.lower() == "save":
            return True
        else:
            continue


async def main():
    telemetry_logger = log.logger()
    task = asyncio.create_task(telemetry_logger.run_logger())

    while True:
        save = await monitor_user_input()
        if save:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                print("Logger stopped safely.")
            break

if __name__ == "__main__":
    asyncio.run(main())
