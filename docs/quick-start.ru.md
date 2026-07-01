# NanoRuslan

🐈🇷🇺 Лёгкий, открытый AI-агент на Python для русскоязычных пользователей.

**Форк:** [HKUDS/nanobot](https://github.com/HKUDS/nanobot) (MIT License)

## Быстрый старт

```bash
pip install nanoruslan
nanoruslan onboard --provider openrouter --model deepseek/deepseek-chat
nanoruslan gateway
```

После этого:
1. Открой браузер → `http://localhost:8765` — WebUI
2. Или пиши в Telegram, если настроил бота
3. Или просто `nanoruslan agent -m "привет"` — в терминале

## Что умеет

- 🤖 **Agent loop** — диалог с LLM, память, инструменты
- 💬 **18 каналов** — Telegram, Discord, Slack, Email, WhatsApp, Matrix и другие
- 🖥 **WebUI** — встроенный дашборд в браузере
- 🔧 **Инструменты** — файлы, терминал, веб-поиск, MCP, код
- 🧠 **30+ провайдеров** — любые OpenAI-совместимые + YandexGPT, GigaChat
- 🎤 **Голос** — распознавание речи (Whisper)
- 🖼 **Картинки** — мультимодальные модели (Kimi, GPT-4o, Claude)

## Конфигурация

```json
{
  "provider": {
    "id": "openrouter",
    "model": "deepseek/deepseek-chat",
    "apiKey": "sk-or-v1-..."
  },
  "telegram": {
    "token": "123456:ABC...",
    "allowedUsers": "username"
  }
}
```

Конфиг лежит в `~/.nanoruslan/config.json`. Создаётся автоматически при `nanoruslan onboard`.

## Каналы связи

Из коробки: Telegram, Discord, Slack, Email, Matrix, Signal, WhatsApp, 
WeChat, WebSocket, CLI, и другие.

## Ссылки

- **GitHub:** https://github.com/valldun1/nanoruslan
- **Оригинал:** https://github.com/HKUDS/nanobot
- **Документация:** https://nanobot.wiki (англ.)

---

**Экосистема Руслан:**

| Проект | Назначение |
|--------|-----------|
| [Руслан](https://github.com/valldun1/ruslan) | Полноценный агент (форк Hermes) |
| [GoRuslan](https://github.com/valldun1/go_ruslan_team) | Лёгкое ядро на Go |
| NanoRuslan | Лёгкий Python-агент для всех |
