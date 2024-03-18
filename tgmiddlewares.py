from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
import logging
from aiogram.types import TelegramObject

logging.basicConfig(level=logging.INFO, filename="bot_log.log", filemode="w")


class IsBannedMiddleware:
    pass


class LoggingMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        logging.info(f"User ID: {event.from_user.id}, Message: {event.text}, Date: {event.date}")
        await handler(event, data)