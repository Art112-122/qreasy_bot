# 📱 QReasy Bot

**QReasy Bot** — це Telegram-бот для швидкої генерації QR-кодів. Простий у використанні, інтуїтивно зрозумілий та корисний у повсякденному житті.

## ⚙️ Функціональність

- 🔳 Генерація QR-кодів з тексту або посилань
- Підтримка Doker

## 🛠 Технології

- **Мова**: Python 3.12+
- **Фреймворк**: [aiogram](https://aiogram.dev)
- **Бібліотеки**:
  - `pyqrcode` — створення QR-кодів
  - `validators` — cnd
  - `dotenv` — робота з токенами

## 🚀 Запуск проєкту

### 1. Клонування репозиторію

```bash
git clone https://github.com/Art112-122/qreasy_bot.git
cd qreasy_bot
```

2. Встановіть залежності:

```bash
pip install -r requirements.txt
```

3. Створіть файл `.env` та додайте токен вашого бота:

```env
BOT_TOKEN=ваш_токен_бота
```

4. Запустіть бота:

```bash
python main.py
```

## 🗂 Структура проєкту

```
qreasy_bot/
├── app/
│   ├── main/       # Точка запуску
│   ├── state/         # FSM-стани
|   ├── .env/          # Приклад конфігураційного файлу
│   └── /         
├── docker-compose.yml 
├── Dockerfile
├── requirements.txt    # Залежності      
```

## 🛠 Використані технології

- Python 3.12+
- [aiogram](https://github.com/aiogram/aiogram)
- python-dotenv
