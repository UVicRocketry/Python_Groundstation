#written by Khephren Gould for Uvic Rocketry June 25, 2025
import logger as log
import asyncio
async def main():
    telemetry_logger = log.logger()
    await telemetry_logger.run()

if __name__ == "__main__":
    asyncio.run(main())