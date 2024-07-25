import sys
import asyncio
from loguru import logger
from aiologger import Logger as AsyncLogger
from aiologger.handlers.files import AsyncFileHandler

class Logger:
    def __init__(self, log_format=("<green>[{time:YYYY-MM-DD HH:mm:ss.SSS}]</green> "
                                  "<level>[{level}]</level> "
                                  "<cyan>[{name}:{function}:{line}]</cyan> "
                                  "<level>{message}</level>")):
        self.logger = logger
        self.async_logger = AsyncLogger.with_default_handlers(name='async_logger')
        self.log_format = log_format

        # Remove default handlers and add custom ones
        self.logger.remove()
        self.logger.add(
            sink=sys.stdout,
            format=log_format,
            level="INFO"
        )

        # Add async file handler to loguru logger
        async_file_handler = AsyncFileHandler("async_log.log")
        self.logger.add(
            sink=async_file_handler.emit,
            format=log_format,
            level="DEBUG"
        )

    async def async_info(self, message):
        await self.async_logger.info(message)

    async def async_error(self, message):
        await self.async_logger.error(message)

    def getLogger(self):
        return self.logger

    async def shutdown_async_logger(self):
        await self.async_logger.shutdown()

# Example usage
async def main():
    custom_logger = Logger()
    logger = custom_logger.getLogger()
    logger.info("This is a synchronous info message")

    # Using async logging
    await custom_logger.async_info("This is an asynchronous info message")
    await custom_logger.async_error("This is an asynchronous error message")

    # Shutdown async logger properly
    await custom_logger.shutdown_async_logger()

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())
