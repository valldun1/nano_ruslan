"""
VK (ВКонтакте) channel — бот для сообществ ВК.

Требует: pip install vk-api
Настройка:
  1. Создай сообщество ВК
  2. Получи токен сообщества (настройки → работа с API)
  3. Включи Long Poll API (настройки → работа с API → Long Poll)
  4. Добавь в config.json:

```json
{
  "channels": {
    "enabled": ["vk"]
  },
  "vk": {
    "token": "vk1.a...",
    "groupId": 123456789
  }
}
```
"""

from __future__ import annotations

import asyncio
from typing import Any

from loguru import logger

from nanobot.channels.base import BaseChannel
from nanobot.bus.events import InboundMessage


class VkChannel(BaseChannel):
    name = "vk"
    display_name = "ВКонтакте"
    send_progress = False

    def __init__(self, config: Any, bus):
        super().__init__(config, bus)
        self.token = getattr(config, "token", "") or ""
        self.group_id = getattr(config, "groupId", "") or ""
        self._running = False

    async def start(self) -> None:
        if not self.token:
            logger.warning("[vk] no token configured")
            return
        self._running = True
        logger.info("[vk] бот запущен")
        # TODO: реализовать Long Poll
        # self._poll_loop()

    async def stop(self) -> None:
        self._running = False
        logger.info("[vk] бот остановлен")

    def _process_message(self, user_id: int, text: str) -> None:
        """Create an InboundMessage and publish to bus."""
        msg = InboundMessage(
            channel=self.name,
            chat_id=str(user_id),
            user_id=str(user_id),
            text=text,
            raw={},
        )
        self.bus.publish(msg)

    async def send_message(self, message) -> None:
        """Send reply back to VK."""
        # TODO: реализовать отправку через VK API
        pass
