from aiogram import executor
from misc import dp
import asyncio
import handlers
from handlers .commands_start import sender


async def on_startup(x):
    asyncio.create_task(sender())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)